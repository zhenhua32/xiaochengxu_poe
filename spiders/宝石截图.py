import asyncio

import requests
from bs4 import BeautifulSoup
from pyppeteer import launch

from spiders.helps import headers

active_url = 'http://poedb.tw/cn/gem.php?cn=Active+Skill+Gem'
support_url = 'http://poedb.tw/cn/gem.php?cn=Support+Skill+Gem'


def parse_page(url):
  urls = set()
  resp = requests.get(url, headers=headers)
  body = BeautifulSoup(resp.text, 'html5lib')

  divs = body.select('.col-md-4')

  for div in divs:
    tbody = div.select('tbody')[0]
    for tr in tbody.select('tr'):
      td1 = tr.select('td')[0]

      item_url = 'http://poedb.tw/cn/{}'.format(td1.a['href'])
      urls.add(item_url)

  return urls


async def capture(url):
  browser = await launch()
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
  element = await page.querySelector('.ItemName')
  name = await page.evaluate('(element) => element.textContent', element)
  img_path = './data/img/宝石/{}.png'.format(name)
  # 获取截图
  element = await page.querySelector('.itembox-gem')
  await element.screenshot({'path': img_path})
  await browser.close()


async def run():
  urls = parse_page(active_url) | parse_page(support_url)
  print('urls: {}'.format(len(urls)))
  remain = {x: 0 for x in urls}

  async def run_loop():
    for url in [k for k, v in remain.items() if v == 0]:
      try:
        await capture(url)
        remain[url] = 1
      except Exception as e:
        remain[url] -= 1
        print(e)
        print(url)
        pass

  # 重试机制 3 次
  while True:
    remain_count = len([k for k, v in remain.items() if -3 < k < 1])
    print(remain_count)
    if remain_count == 0:
      break
    await run_loop()

  print('剩余无法获取的链接', [k for k, v in remain.items() if k != 1])


if __name__ == '__main__':
  asyncio.run(run())
