from urllib import parse

from pymongo import MongoClient

from settings import config
from db.helps import create_index

host = config['db']['mongo']['host']
port = config['db']['mongo']['port']
username = config['db']['mongo']['username']
password = config['db']['mongo']['password']
dbname = config['db']['mongo']['dbname']
# fake%4023

if username and password:
  mongo_url = 'mongodb://{}:{}@{}:{}/'.format(username, parse.quote(password), host, port)
else:
  mongo_url = 'mongodb://{}:{}/'.format(host, port)

client = MongoClient(mongo_url)
# 数据库名, 存储所有的数据
db = client[dbname]

# item: 存放基本物品
coll_item = db['item']
create_index(coll_item, indexs={
  'name': {
    'key': 'name',
    'kwargs': {
      'unique': True
    }
  },
})

# legend: 传奇物品
coll_legend = db['legend']
create_index(coll_legend, indexs={
  'name': {
    'key': 'name',
    'kwargs': {
      'unique': True
    }
  },
})

if __name__ == '__main__':
  doc = coll_item.find_one({'name': '拳钉'})
  keys = ['_id', 'name', 'type', 'sub_type', 'update', 'url', 'img_url']
  result = {}
  text = []
  for key, value in doc.items():
    if key in keys:
      result[key] = str(value)
    else:
      if key == '物理伤害':
        text.append('{}: {}-{}'.format(key, value[0], value[1]))
      elif key == '效果':
        text += value
      else:
        text.append('{}: {}'.format(key, value))
  result['lines'] = text

  print(result)
