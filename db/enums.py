'''
WARNNING: 这是自动生成的文件
定义数据库存储的结构
'''

from enum import Enum, unique


@unique
class TYPE(Enum):
  宝石 = '宝石'
  单手武器 = '单手武器'
  双手武器 = '双手武器'
  副手 = '副手'
  护具 = '护具'
  饰品 = '饰品'
  药剂 = '药剂'
  其他 = '其他'
  帝王迷宫 = '帝王迷宫'


@unique
class TYPE_宝石(Enum):
  主动技能宝石 = '主动技能宝石'
  辅助技能宝石 = '辅助技能宝石'


@unique
class TYPE_单手武器(Enum):
  爪 = '爪'
  匕首 = '匕首'
  符文匕首 = '符文匕首'
  法杖 = '法杖'
  单手剑 = '单手剑'
  细剑 = '细剑'
  单手斧 = '单手斧'
  单手锤 = '单手锤'
  短杖 = '短杖'


@unique
class TYPE_双手武器(Enum):
  弓 = '弓'
  长杖 = '长杖'
  战杖 = '战杖'
  双手剑 = '双手剑'
  双手斧 = '双手斧'
  双手锤 = '双手锤'
  鱼竿 = '鱼竿'


@unique
class TYPE_副手(Enum):
  盾 = '盾'
  箭袋 = '箭袋'


@unique
class TYPE_护具(Enum):
  手套 = '手套'
  鞋子 = '鞋子'
  胸甲 = '胸甲'
  头部 = '头部'


@unique
class TYPE_饰品(Enum):
  项链 = '项链'
  戒指 = '戒指'
  腰带 = '腰带'


@unique
class TYPE_药剂(Enum):
  生命药剂 = '生命药剂'
  魔力药剂 = '魔力药剂'
  复合药剂 = '复合药剂'
  功能药剂 = '功能药剂'
  暴击药剂 = '暴击药剂'


@unique
class TYPE_其他(Enum):
  可堆叠通货 = '可堆叠通货'
  地图碎片 = '地图碎片'
  藏身处装饰 = '藏身处装饰'
  命运卡 = '命运卡'
  裂隙之石 = '裂隙之石'
  神灵之魂 = '神灵之魂'
  传奇装备碎片 = '传奇装备碎片'
  珠宝 = '珠宝'
  深渊珠宝 = '深渊珠宝'
  孕育石 = '孕育石'
  保险箱 = '保险箱'


@unique
class TYPE_帝王迷宫(Enum):
  迷宫物品 = '迷宫物品'
  迷宫饰品 = '迷宫饰品'
  异界迷宫物品 = '异界迷宫物品'


@unique
class COLOR(Enum):
  RED = '力量'
  GREEN = '敏捷'
  BLUE = '智慧'
  GREY = '普通'