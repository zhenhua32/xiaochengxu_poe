from db.enums import TYPE_饰品
from spiders.helps import get_top_urls, json_url, count_fields
from spiders.单手武器 import parse_page

urls = get_top_urls()['饰品']


def fileds():
  count_fields(urls)


def run():
  for item in urls:
    url = json_url + item['url'].split('?')[-1]
    parse_page(url, TYPE_饰品, '饰品', save_in_db=True)


if __name__ == '__main__':
  run()
