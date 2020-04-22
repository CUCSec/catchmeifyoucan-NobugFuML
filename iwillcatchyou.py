import struct
import os
from pathlib import Path

root = input('请输入你要遍历的目录: ')
# 遍历用户指定的目录，如果想偷懒，可以用 Path.rglob('*')
# Path.rglob('*') 相当于自动给参数加上 '**/' 的 glob
files = Path(root).glob('**/*')
a=b'\xff\xd8'
b=b'\x89PNG'
c=b'BM'
d=b'%PDF'
e=b'PK\x03\x04'
f=b'PK\x03\x04'
g=b'MZ'  ##这样写好像简单点
catch_dict={".jpg":a,".png":b,'.bmp':c,'.pdf':d,'.docx':e,'.pptx':f,'.exe':g} 

path = Path.cwd() ##获取当前路径

Path(path/'异常').mkdir(exist_ok=True)
Path(path/'正常').mkdir(exist_ok=True)
##创建新目录在当前路径

#遍历文件
for file in files:
    if Path(file).is_file():
        suffix=file.suffix #获取后缀
        with open(file, 'rb') as f:#读取文件
            file_header = f.read(len(catch_dict[suffix]))#判断正常异常
        if file_header == catch_dict[suffix] :#转移文件
            file.rename(path/'正常'/(file.stem+file.suffix))
        else :
            file.rename(path/'异常'/(file.stem+file.suffix))
        
print('已结束操作')