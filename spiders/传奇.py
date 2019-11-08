import datetime
import requests
from bs4 import BeautifulSoup
import pymongo

from db.mongo import coll_legend
from spiders.helps import headers, get_top_urls, base_url


def count_span_class_name():
  '''统计 td > span 中可能出现的 class'''
  def parse(url):
    resp = requests.get(url, headers=headers)
    body = BeautifulSoup(resp.text, 'html5lib')
    for tr in body.select('tbody tr'):
      if len(tr.select('td')) != 2:
        continue
      td2 = tr.select('td')[1]

      for span in td2.select('td > span'):
        class_name = span.get('class')
        if class_name:
          if 'gem_red' in class_name:
            print(span)
          fields.add(class_name[0])

  fields = set()
  urls = get_top_urls(index=1)
  for items in urls.values():
    for item in items:
      print(item)
      parse(item['url'])
  print(fields)


def split_br(span: BeautifulSoup) -> list:
  texts = str(span).replace('<br/>', '<br>').split('<br>')
  return [BeautifulSoup(t, 'html5lib').get_text(strip=True) for t in texts]


class_name_handle = {
  'implicitMod': {
    'key': '默认效果',
    'func': split_br,
  },
  'explicitMod': {
    'key': '附加效果',
    'func': split_br,
  },
  'item_legacy': {
    'key': '遗产',
    'func': split_br,
  },
  'item_description': {
    'key': '英文名',
    'func': lambda span: split_br(span)[0],
  },
  'gem_red': {
    'key': '特殊',
    'func': split_br,
  },
}


def prase_html(tr: BeautifulSoup, atype: str, sub_type: str) -> dict:
  '''解析一条记录'''
  td1 = tr.select('td')[0]
  td2 = tr.select('td')[1]

  if td1.select('img'):
    img_url = td1.a.img['src']
  else:
    img_url = None
  name = td2.a.get_text(strip=True)
  item_url = base_url + td2.a['href']

  doc = {
    'name': name,
    'type': atype,
    'sub_type': sub_type,
    'update': datetime.datetime.utcnow(),
    'url': item_url,
    'img_url': img_url,
    'tags': [],
    '需求': None,
    '英文名': None,
    '默认效果': [],
    '附加效果': [],
    '遗产': [],
    '特殊': [],
  }

  for br in td2.select('td > br'):
    text = str(br.next_sibling)
    if '需求' in text:
      doc['需求'] = text.replace('需求', '').strip()

  for span in td2.select('td > span'):
    class_names = span.get('class', [])
    for cname in class_names:
      if cname in class_name_handle:
        key = class_name_handle[cname]['key']
        value = class_name_handle[cname]['func'](span)
        doc[key] = value

  return doc


def parse_page(url, atype, sub_type, save_in_db=True):
  resp = requests.get(url, headers=headers)
  body = BeautifulSoup(resp.text, 'html5lib')

  for tr in body.select('tbody tr'):
    if len(tr.select('td')) != 2:
      continue
    doc = prase_html(tr, atype, sub_type)
    print(doc)
    if save_in_db:
      try:
        coll_legend.update_one({'name': doc['name']}, {'$set': doc}, upsert=True)
      except pymongo.errors.DuplicateKeyError:
        pass
      except Exception as e:
        raise e


def run(save=True):
  urls = get_top_urls(index=1)
  for atype, items in urls.items():
    if atype in ['赛季']:
      continue
    for item in items:
      sub_type = item['name']
      if sub_type in ['所有']:
        continue
      url = item['url']
      parse_page(url, atype, sub_type, save_in_db=save)


def add_tags():
  '''增加赛季 tag'''
  items = get_top_urls(index=1)['赛季']
  for item in items:
    tag = item['name']
    url = item['url']

    resp = requests.get(url, headers=headers)
    body = BeautifulSoup(resp.text, 'html5lib')
    for tr in body.select('tbody tr'):
      if len(tr.select('td')) != 2:
        continue
      td2 = tr.select('td')[1]
      name = td2.a.get_text(strip=True)

      try:
        coll_legend.update_one({'name': name}, {'$addToSet': {'tags': tag}})
      except Exception as e:
        raise e


if __name__ == '__main__':
  # run(save=True)
  add_tags()
