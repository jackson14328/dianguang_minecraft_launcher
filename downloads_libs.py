# 下载依赖项
import os
yorn = input('Can we downloads libs from pypi?You need a network and pip(y/n)')
if yorn == 'y':
    print('We will downloads [PIL]Python_Imaging_Library')
    os.system('pip install pillow')
    print('We will downloads minecraft_launcher_lib')
    os.system('pip install minecraft_launcher_lib')
else:
    print('If you do not allow the download of dependencies, the program will not run properly')