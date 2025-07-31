# [DML]Dianguang Minecraft Launcher
# by 二氧化碳已爆炸|mike20131214
# 未经允许|禁止商用
#Minecraft Launcher For Python
# 导入库
import tkinter as tk
import dbm
import ctypes
import os

# 自定义函数
# [playername_ok_button]确定玩家名的调用函数
# 存字符串后加.encode('utf-8')编码,存数字先用str()将字符串转换成数字再用同样的方式编码
# 取字符串后加.decode('utf-8')解码,取数字先用int()转换成字符串再用同样的方式解码
# 注：因为是dbm库用了反人类的字节串而不是字符串存储数据，所以会出现这种情况
def playername_ok_button():
    with dbm.open('playerdata', 'c') as db: 
        db['playername'] = playername.get().encode('utf-8')
# [startgame]MC，启动！的调用函数
def startgame():
    print('123abc')
# [nopoint]千万别点的调用函数
def nopoint1():
    print('没做好')

# 主程序
# 设置任务名
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("2am.dml.0.1")
# 主界面
root = tk.Tk()
root.title('DML 0.1')
root.geometry('850x480')
root.iconbitmap('icon.ico')
root.resizable(0 , 0)
# [dmltitle]DML标题
dmltitle = tk.Label(root , text = '''    ____  __  _____ 
   /__  \/  | / / /
/ / / / /|_/ / /
 / /_/ / /  / / /___
/_____/_/  /_/_____/''' , font = ('TkDefaultFont' , 20))
dmltitle.pack(anchor = 'w')
# [steve|playerimage]史蒂夫头像，纯装饰，无作用
steve = tk.PhotoImage(file='steve.gif')
playerimage = tk.Label(root , image = steve)
playerimage.pack(anchor = 'w')
# [playername_lable|playername]玩家名自定义
playername_lable = tk.Label(root , text = '请输入玩家名')
playername_lable.pack(anchor = 'w')
playername = tk.Entry(root)
playername.pack(anchor = 'w')
# [playername_ok_button]确定玩家名
playername_ok_button = tk.Button(root , text = 'OK' , command = playername_ok_button)
playername_ok_button.pack(anchor = 'w')
# [startplay]MC，启动！
startgame = tk.Button(root , text = '启动Minecraft' , font = ('TkDefaultFont' , 40) , command = startgame)
startgame.pack(anchor = 'ne')
# [nopoint]千万别点
nopoint = tk.Button(root , text = '千万别点' , command = nopoint1)
nopoint.pack()
root.mainloop()