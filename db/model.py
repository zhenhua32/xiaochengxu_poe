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
  'url': str,
  'img_url': str,
  'tags': [],
  '物理伤害': [int, int],
  '攻击暴击率': Decimal128,
  '每秒攻击次数': Decimal128,
  '武器范围': Decimal128,
  '护具': int,
  '闪避值': int,
  '能量护盾': int,
  '格挡几率': Decimal128,
  '效果': [],
  '需求': str,
  '英文名': str,
}

item_宝石 = {
  'name': str,
  'type': '宝石',
  'sub_type': TYPE_宝石,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  'tags': [],
  'color': COLOR,
}

item_单手武器 = {
  'name': str,
  'type': '单手武器',
  'sub_type': TYPE_单手武器,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
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
  'img_url': str,
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
  'img_url': str,
  '护具': int,
  '闪避值': int,
  '能量护盾': int,
  '格挡几率': Decimal128,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_护具 = {
  'name': str,
  'type': '护具',
  'sub_type': TYPE_护具,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  '需求': str,
  '效果': [],
  '英文名': str,
  '护具': int,
  '闪避值': int,
  '能量护盾': int,
}

item_饰品 = {
  'name': str,
  'type': '饰品',
  'sub_type': TYPE_饰品,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_药剂 = {
  'name': str,
  'type': '药剂',
  'sub_type': TYPE_药剂,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_其他 = {
  'name': str,
  'type': '其他',
  'sub_type': TYPE_其他,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  '需求': str,
  '效果': [],
  '英文名': str,
}

item_帝王迷宫 = {
  'name': str,
  'type': '帝王迷宫',
  'sub_type': TYPE_帝王迷宫,
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  '需求': str,
  '效果': [],
  '英文名': str,
}

legend_type = {
  'name': str,
  'type': TYPE,
  'sub_type': '',
  'update': datetime.datetime.utcnow(),
  'url': str,
  'img_url': str,
  'tags': [],
  '需求': str,
  '英文名': str,
  '默认效果': [],
  '附加效果': [],
  '遗产': [],
  '特殊': [],
}
