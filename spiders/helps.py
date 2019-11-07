'''
辅助函数
'''

import requests
from bs4 import BeautifulSoup
from bson import Decimal128

headers = {
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
base_url = 'http://poedb.tw/cn/'
json_url = 'http://poedb.tw/cn/json.php/item_class?'

field_handle = {
  '物理伤害': lambda value: [int(x) for x in value.split('-')],
  '攻击暴击率': lambda value: Decimal128(value[:-1]),
  '每秒攻击次数': Decimal128,
  '武器范围': int,
  '护具': int,
  '闪避值': int,
  '能量护盾': int,
  '格挡几率': lambda value: Decimal128(value[:-1]),
}


def get_top_urls(index=0) -> dict:
  '''
  获取首页的链接, index=0 返回物品页, index=1 返回传奇页
  key: [{'name', 'url'}]
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


def count_fields(urls):
  '''统计字段'''
  fields = set()

  for item in urls:
    url = json_url + item['url'].split('?')[-1]
    resp = requests.get(url, headers=headers)
    data = resp.json()

    for line in data['data']:
      texts = line[1].replace('<br/>', '<br>').split('<br>')
      for html in texts[2:-1]:
        body = BeautifulSoup(html, 'html5lib')
        text = body.get_text(strip=True)
        if ': ' in text:
          fields.add(text.split(': ')[0].strip())

  print(fields)


if __name__ == '__main__':
  get_top_urls()
