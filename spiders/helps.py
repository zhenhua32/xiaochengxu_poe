'''
辅助函数
'''

import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
base_url = 'http://poedb.tw/cn/'


def get_top_urls(index=0):
  '''
  获取首页的连接, index=0 返回物品页, index=1 返回传奇页
  '''
  url = 'http://poedb.tw/cn/item.php'
  resp = requests.get(url, headers=headers)
  body = BeautifulSoup(resp.text, 'html5lib')

  data = {}  # 保存数据

  panel = body.select('.panel-body')[index].ul
  titles = panel.select('li.double_th')
  subs = panel.select('ul')

  for title, sub in zip(titles, subs):
    name = title.get_text(strip=True).replace('：', '')
    values = []
    for li in sub.select('li'):
      v_name = li.get_text(strip=True)
      v_url = base_url + li.a['href']
      values.append({
        'name': v_name,
        'url': v_url,
      })
    data[name] = values

  return data


if __name__ == '__main__':
  get_top_urls()
