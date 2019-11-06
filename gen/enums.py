'''
生成 enum 代码
'''

import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

dir_path = Path(__file__).parent.parent / 'templates'
env = Environment(loader=FileSystemLoader(dir_path.as_posix()), trim_blocks=True)

# 获取数据
headers = {
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

url = 'http://poedb.tw/cn/item.php'
resp = requests.get(url, headers=headers)
body = BeautifulSoup(resp.text, 'html5lib')

data = {}  # 保存数据

panel = body.select('.panel-body')[0].ul
titles = panel.select('li.double_th')
subs = panel.select('ul')

for title, sub in zip(titles, subs):
  name = title.get_text(strip=True).replace('：', '')
  values = []
  for li in sub.select('li'):
    values.append(li.get_text(strip=True))
  data[name] = values

# 生成代码
template = env.get_template('enums.py.jinja')
print(template.render(data=data))
with open('db/enums.py', 'w', encoding='utf-8') as f:
  f.write(template.render(data=data))

print('成功生成: db/enums.py')
