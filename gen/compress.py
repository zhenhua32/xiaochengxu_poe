'''
压缩图片
'''

import subprocess
from pathlib import Path
import os
import glob

data_dir = Path(__file__).parent.parent / 'data'
pngquant = Path(__file__).parent.parent / 'libs' / 'pngquant' / 'pngquant.exe'
pngquant_cmd = pngquant.as_posix()


def compress(path, out_path):
  '''
  pngquant 不支持中文路径, 只能从 stdin 中读取了
  '''
  with open(path, 'rb') as stdin:
    with open(out_path, 'wb') as stdout:
      subprocess.run([pngquant_cmd, '-'], stdin=stdin, stdout=stdout)


def compress_dir(last_dir_name):
  img_dir = data_dir / 'img' / last_dir_name
  out_dir = data_dir / 'compress' / last_dir_name
  os.makedirs(out_dir, exist_ok=True)

  files = glob.glob(img_dir.as_posix() + '/*.png')
  files = [os.path.basename(x) for x in files]

  for file in files:
    filename = os.path.basename(file)
    print(filename)

    path = (img_dir / filename).as_posix()
    out_path = (out_dir / filename).as_posix()
    compress(path, out_path)


if __name__ == '__main__':
  compress_dir(last_dir_name='传奇')
