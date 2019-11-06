from pymongo.collection import Collection


# 创建索引
def create_index(coll: Collection, indexs: dict):
  index_names = []
  for index in coll.index_information().values():
    for item in index['key']:
      index_names.append(item[0])

  for name in indexs.keys():
    if name not in index_names:
      key = indexs[name]['key']
      kwargs = indexs[name].get('kwargs', {})
      index_name = coll.create_index(key, **kwargs)
      print('在 {} 上创建索引 {}'.format(coll.full_name, index_name))
