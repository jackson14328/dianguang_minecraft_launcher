# 下载依赖项
import os
yorn = input('Can we downloads libs from pypi?You need a network and pip(y/n)')
if yorn == 'y':
    print('We will downloads [PIL]Python_Imaging_Library')
    os.system('pip install pillow')
else:
    print('If you do not allow the download of dependencies, the program will not run properly')