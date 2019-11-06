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

# item: 存放所有的物品
coll_item = db['item']
create_index(coll_item, indexs={
  'name': {
    'key': 'name',
    'kwargs': {
      'unique': True
    }
  },
})
