import asyncio

import requests
from bs4 import BeautifulSoup
from pyppeteer import launch

from spiders.helps import headers, get_top_urls, base_url


def parse_page(url):
  '''解析一页'''
  urls = dict()
  resp = requests.get(url, headers=headers)
  body = BeautifulSoup(resp.text, 'html5lib')

  for tr in body.select('tbody tr'):
    if len(tr.select('td')) != 2:
      continue
    td2 = tr.select('td')[1]
    name = td2.a.get_text(strip=True)
    item_url = base_url + td2.a['href']

    urls[item_url] = {'count': 0, 'name': name}

  return urls


async def capture(browser, url, name):
  '''获取截图'''
  page = await browser.newPage()
  # 设置设备模拟, 缩放为 200%
  await page.emulate(viewport={
    'isMobile': False,
    'height': 1920,
    'width': 1080,
    'deviceScaleFactor': 2,
  })
  await page.goto(url)
  # 获取名字
  img_path = './data/img/传奇/{}.png'.format(name)
  # 获取截图
  element = await page.querySelector('.itembox-gem')
  await element.screenshot({'path': img_path})
  await browser.close()


async def run():
  browser = await launch()

  # 结构为 url: {'count': 0, 'name': name}
  urls = dict()

  # 获取所有的页面链接
  data = get_top_urls(index=1)
  for items in data.values():
    for item in items:
      url = item['url']
      part = parse_page(url)
      for k, v in part.items():
        urls[k] = v

  print(len(urls.keys()))
  remain = urls

  async def run_loop():
    for url, name in [(k, v['name']) for k, v in remain.items() if -3 < v['count'] < 1]:
      try:
        await capture(browser, url, name)
        remain[url]['count'] = 1
      except Exception as e:
        remain[url]['count'] -= 1
        print(e)
        print(url)

  # 重试机制 3 次
  while True:
    remain_count = len([k for k, v in remain.items() if -3 < v['count'] < 1])
    print(remain_count)
    if remain_count == 0:
      break
    await run_loop()

  print('剩余无法获取的链接', [(k, v['name']) for k, v in remain.items() if v['count'] != 1])

  await browser.close()


if __name__ == '__main__':
  asyncio.run(run())
