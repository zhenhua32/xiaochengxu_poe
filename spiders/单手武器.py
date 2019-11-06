import datetime

import pymongo
import requests
from bs4 import BeautifulSoup
from bson import Decimal128

from db.enums import TYPE_单手武器
from db.mongo import coll_item
from spiders.helps import base_url, get_top_urls, headers

urls = get_top_urls()['单手武器']

json_url = 'http://poedb.tw/cn/json.php/item_class?'


def parse_text(text: str) -> [str, str]:
  '''解析属性'''
  if ': ' in text:
    key = text.split(': ')[0].strip()
    value = text.split(': ')[1].strip()
    if key == '物理伤害':
      value = [int(x) for x in value.split('-')]
    elif key == '攻击暴击率':
      value = Decimal128(value[:-1])
    elif key == '每秒攻击次数':
      value = Decimal128(value)
    elif key == '武器范围':
      value = int(value)
  elif '需求' in text:
    key = '需求'
    value = text.replace('需求', '').strip()
  else:
    key = '效果'
    value = text

  return key, value


def parse_html(html: str, sub_type: str) -> dict:
  '''解析一条记录'''
  texts = html.replace('<br/>', '<br>').split('<br>')

  body = BeautifulSoup(texts[0], 'html5lib')
  name = body.a.get_text(strip=True)
  item_url = base_url + body.a['href']
  en_name = BeautifulSoup(texts[-1], 'html5lib').get_text(strip=True)

  doc = {
    'name': name,
    'type': '单手武器',
    'sub_type': sub_type,
    'update': datetime.datetime.utcnow(),
    'url': item_url,
    '物理伤害': None,
    '攻击暴击率': None,
    '每秒攻击次数': None,
    '武器范围': None,
    '需求': None,
    '效果': [],
    '英文名': en_name,
  }

  for html in texts[2:-1]:
    body = BeautifulSoup(html, 'html5lib')
    text = body.get_text(strip=True)
    key, value = parse_text(text)
    if key == '效果':
      if value:
        doc[key].append(value)
    else:
      doc[key] = value

  return doc


def parse_page(url):
  resp = requests.get(url, headers=headers)
  data = resp.json()

  caption = data['caption'].split(' ')[0]
  sub_type = TYPE_单手武器(caption).value

  for line in data['data']:
    doc = parse_html(line[1], sub_type)
    print(doc)
    try:
      coll_item.update_one({'name': doc['name']}, {'$set': doc}, upsert=True)
    except pymongo.errors.DuplicateKeyError:
      pass
    except Exception as e:
      raise e


def run():
  for item in urls:
    url = json_url + item['url'].split('?')[-1]
    parse_page(url)


if __name__ == '__main__':
  run()
