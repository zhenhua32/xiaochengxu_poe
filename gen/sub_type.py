'''
生成 sub_type 的 json 文件
'''
import json

from spiders.helps import get_top_urls


def top_urls_to_json(index=0, filters=[]):
  '''将 sub_type 转换为 json 格式'''
  data = get_top_urls(index=index)
  result = dict()
  for key, value in data.items():
    if key in filters:
      continue
    result[key] = [x['name'] for x in value if x['name'] not in filters]
  return result


def run():
  base = top_urls_to_json(index=0)
  legend = top_urls_to_json(index=1, filters=['所有', '赛季'])
  two = {
    '基础': list(base.keys()),
    '传奇': list(legend.keys()),
  }
  three = {
    '基础': base,
    '传奇': legend,
  }
  data = {
    '1': list(two.keys()),
    '2': two,
    '3': three,
  }

  jsondata = json.dumps(data, ensure_ascii=False, indent=' ')
  with open('./log/sub_type_full.json', 'w', encoding='utf-8') as f:
    f.write(jsondata)


if __name__ == '__main__':
  run()
