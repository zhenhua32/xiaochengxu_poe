from db.enums import TYPE_双手武器
from spiders.helps import get_top_urls, json_url
from spiders.单手武器 import parse_page

urls = get_top_urls()['双手武器']


def run():
  for item in urls:
    url = json_url + item['url'].split('?')[-1]
    parse_page(url, TYPE_双手武器, '双手武器')


if __name__ == '__main__':
  run()
