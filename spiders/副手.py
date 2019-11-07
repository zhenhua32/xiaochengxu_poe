from db.enums import TYPE_副手
from spiders.helps import get_top_urls, json_url
from spiders.单手武器 import parse_page

urls = get_top_urls()['副手']


def run():
  for item in urls:
    url = json_url + item['url'].split('?')[-1]
    parse_page(url, TYPE_副手, '副手', save_in_db=True)


if __name__ == '__main__':
  run()
