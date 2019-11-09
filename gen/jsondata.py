'''
将 mongo express 中下载的 json 文件处理,
以便小程序的云开发能导入,
主要是处理 {"$numberDecimal":"6"}
'''

import argparse
import re

parser = argparse.ArgumentParser(description='转换 json line 文件')
parser.add_argument(
  '-i',
  action='append',
  type=str,
  help='输入文件的路径',
)
parser.add_argument(
  '-o',
  action='append',
  type=str,
  default=[],
  help='输出文件的路径',
)


def handle_line(line: str) -> str:
  new_line = re.sub(r'{"\$numberDecimal":"(\d*\.?\d+)"}', r'\1', line)
  return new_line


def handle_file(file_path: str, out_path):
  with open(file_path, 'r', encoding='utf-8') as fin, open(out_path, 'w', encoding='utf-8') as fout:
    for line in fin:
      new_line = handle_line(line)
      fout.write(new_line)


if __name__ == '__main__':
  args = parser.parse_args()
  print(args)
  fin = args.i
  fout = args.o
  if len(fin) != len(fout):
    Warning('--in 和 --out 数目不一致')
  for i, o in zip(fin, fout):
    handle_file(i, o)
