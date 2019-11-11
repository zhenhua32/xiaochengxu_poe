import datetime

import pymongo
import requests
from bs4 import BeautifulSoup

from db.mongo import coll_item
from spiders.helps import base_url, get_top_urls, headers, json_url, field_handle


def parse_text(text: str) -> [str, str]:
  '''解析属性'''
  if ': ' in text:
    key = text.split(': ')[0].strip()
    value = text.split(': ')[1].strip()
    if key in field_handle:
      value = field_handle[key](value)
  elif '需求' in text:
    key = '需求'
    value = text.replace('需求', '').strip()
  else:
    key = '效果'
    value = text

  return key, value


def parse_html(html: str, atype: str, sub_type: str, img_url: str) -> dict:
  '''解析一条记录'''
  texts = html.replace('<br/>', '<br>').split('<br>')

  body = BeautifulSoup(texts[0], 'html5lib')
  name = body.a.get_text(strip=True)
  item_url = base_url + body.a['href']
  en_name = BeautifulSoup(texts[-1], 'html5lib').get_text(strip=True)

  doc = {
    'name': name,
    'type': atype,
    'sub_type': sub_type,
    'update': datetime.datetime.utcnow(),
    'url': item_url,
    'img_url': img_url,
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


def parse_page(url, atype, sub_type, save_in_db=True):
  resp = requests.get(url, headers=headers)
  data = resp.json()

  if not isinstance(data, dict):
    return

  for line in data['data']:
    img_url = BeautifulSoup(line[0], 'html5lib').img['src']
    doc = parse_html(line[1], atype, sub_type, img_url)
    print(doc)
    if save_in_db:
      try:
        coll_item.update_one({'name': doc['name']}, {'$set': doc}, upsert=True)
      except pymongo.errors.DuplicateKeyError:
        pass
      except Exception as e:
        raise e


def run():
  '''获取所有的基础物品'''
  urls = get_top_urls()
  for atype, items in urls.items():
    if atype in ['宝石']:
      continue
    for item in items:
      url = json_url + item['url'].split('?')[-1]
      parse_page(url, atype, item['name'], save_in_db=True)


if __name__ == '__main__':
  run()
