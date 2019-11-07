'''
定义数据库存储的结构
'''

import datetime
from bson import Decimal128
from db.enums import (
  TYPE,
  TYPE_其他,
  TYPE_副手,
  TYPE_单手武器,
  TYPE_双手武器,
  TYPE_宝石,
  TYPE_帝王迷宫,
  TYPE_护具,
  TYPE_药剂,
  TYPE_饰品,
  COLOR,
)

item_type = {
  'name': str,
  'type': TYPE,
  'sub_type': '',
  'update': datetime.datetime.utcnow(),
}

item_宝石 = {
  'name': str,
  'type': '宝石',
  'sub_type': TYPE_宝石,
  'update': datetime.datetime.utcnow(),
  'required_level': int,
  'tags': [],
  'color': COLOR,
  'url': str,
  'img_url': str,
}

item_单手武器 = {
  'name': str,
  'type': '单手武器',
  'sub_type': TYPE_单手武器,
  'update': datetime.datetime.utcnow(),
  'url': str,
  '物理伤害': [int, int],
  '攻击暴击率': Decimal128,
  '每秒攻击次数': Decimal128,
  '武器范围': int,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_双手武器 = {
  'name': str,
  'type': '双手武器',
  'sub_type': TYPE_双手武器,
  'update': datetime.datetime.utcnow(),
  'url': str,
  '物理伤害': [int, int],
  '攻击暴击率': Decimal128,
  '每秒攻击次数': Decimal128,
  '武器范围': int,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_副手 = {
  'name': str,
  'type': '副手',
  'sub_type': TYPE_副手,
  'update': datetime.datetime.utcnow(),
  'url': str,
  '护具': int,
  '闪避值': int,
  '能量护盾': int,
  '格挡几率': Decimal128,
  '需求': str,
  '效果': [],
  '英文名': str,
}
