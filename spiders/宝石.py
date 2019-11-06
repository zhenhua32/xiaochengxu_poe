import datetime

import pymongo
import requests
from bs4 import BeautifulSoup

from db.enums import COLOR, TYPE_宝石
from db.mongo import coll_item
from spiders.helps import headers

active_url = 'http://poedb.tw/cn/gem.php?cn=Active+Skill+Gem'
support_url = 'http://poedb.tw/cn/gem.php?cn=Support+Skill+Gem'


def get_color(text):
  if 'gem_blue' in text:
    color = COLOR.BLUE.value
  elif 'gem_green' in text:
    color = COLOR.GREEN.value
  elif 'gem_red' in text:
    color = COLOR.RED.value
  else:
    color = COLOR.GREY.value

  return color


def parse_page(url, sub_type):
  resp = requests.get(url, headers=headers)
  body = BeautifulSoup(resp.text, 'html5lib')

  divs = body.select('.col-md-4')

  for div in divs:
    tbody = div.select('tbody')[0]
    for tr in tbody.select('tr'):
      td1 = tr.select('td')[0]
      td2 = tr.select('td')[1]

      img_url = td1.a.img['src']
      item_url = 'http://poedb.tw/cn/{}'.format(td1.a['href'])

      name = td2.a.get_text(strip=True)
      text = td2.get_text(strip=True).replace(name, '')
      required_level = text.split('(')[1].split(')')[0]
      tags = text.split(')')[-1].split(',')
      # print(name, required_level, tags)
      color = get_color(td2.a.get('class', ''))

      doc = {
        'name': name,
        'type': '宝石',
        'sub_type': sub_type,
        'update': datetime.datetime.utcnow(),
        'required_level': int(required_level),
        'tags': tags,
        'color': color,
        'url': item_url,
        'img_url': img_url,
      }
      print(doc)
      try:
        coll_item.insert_one(doc)
      except pymongo.errors.DuplicateKeyError:
        pass
      except Exception as e:
        raise e


if __name__ == '__main__':
  parse_page(active_url, TYPE_宝石.主动技能宝石.value)
  parse_page(support_url, TYPE_宝石.辅助技能宝石.value)
