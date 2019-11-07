'''
生成 enum 代码
'''

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from spiders.helps import get_top_urls

dir_path = Path(__file__).parent.parent / 'templates'
env = Environment(loader=FileSystemLoader(dir_path.as_posix()), trim_blocks=True)

# 获取数据
data = get_top_urls(index=0)
legend = get_top_urls(index=1)

# 生成代码
template = env.get_template('enums.py.jinja')
print(template.render(data=data, legend=legend))
with open('db/enums.py', 'w', encoding='utf-8') as f:
  f.write(template.render(data=data, legend=legend))

print('成功生成: db/enums.py')
