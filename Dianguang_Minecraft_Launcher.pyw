# [DML]Dianguang Minecraft Launcher
# by 二氧化碳已爆炸|mike20131214
# 未经允许|禁止商用
#Minecraft Launcher For Python
# 导入库
import tkinter as tk
from tkinter import messagebox
import dbm
import os
try:
    a = dbm['javalist'].decode('utf-8')
except:
    messagebox.showerror("提示", f"环境不完整，请求配置完整环境")
    print('We will downloads [PIL]Python_Imaging_Library')
    os.system('pip install pillow')
    print('We will downloads minecraft_launcher_lib')
    os.system('pip install minecraft_launcher_lib')
    with dbm.open('playerdata', 'c') as db: 
        db['playername'] = ''.encode('utf-8')
        db['gamev'] = ''.encode('utf-8')
        db['javalist'] = ''.encode('utf-8')
        db['gamelist'] = ''.encode('utf-8')
    messagebox.showerror("提示", f"配置环境成功")
import ctypes
from PIL import Image, ImageTk
import start


# 自定义函数
# [playername_ok_button]确定玩家名的调用函数
# 存字符串后加.encode('utf-8')编码,存数字先用str()将字符串转换成数字再用同样的方式编码
# 取字符串后加.decode('utf-8')解码,取数字先用int()转换成字符串再用同样的方式解码
# 注：因为是dbm库用了反人类的字节串而不是字符串存储数据，所以会出现这种情况
def playername_ok_button():
    try:
        with dbm.open('playerdata', 'c') as db: 
            db['playername'] = playername.get().encode('utf-8')
    except Exception as e:
        messagebox.showerror("错误", f"保存失败: {str(e)}")
# [startgame]MC，启动！的调用函数
def startgame():
    with dbm.open('playerdata', 'c') as db: 
        javalj = db['javalist'].decode('utf-8')
        gamelj = db['gamelist'].decode('utf-8')
        playernamedbm = db['playername'].decode('utf-8')
        gamev = db['gamev'].decode('utf-8')
    start.gamestart(player_name=playernamedbm,minecraft_dir=gamelj,minecraft_version=gamev,JVM="4G",JavaPath=javalj)
# [nopoint]千万别点的调用函数
def nopoint():
    try:
        os.system('python nopoint.py')
    except Exception as e:
        messagebox.showerror("错误", f"执行失败: {str(e)}")
# [setting]设置的调用函数
def setting():
    try:
        os.system('python setting.py')
    except Exception as e:
        messagebox.showerror("错误", f"执行失败: {str(e)}")
def alpha():
    start.download_minecraft_version(version_name = '1.8.9' , minecraft_dir = r'E:/dml')

# 主程序
# 设置任务名
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml.0.1")
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
dmltitle.pack()
dmltitle.place(x=50, y=25)
# [steve|playerimage]史蒂夫头像，纯装饰，无作用
# [origin_img|real_img|steve]转换图片格式
origin_img = Image.open("steve.gif")
real_img = origin_img.resize((64, 64))
steve = ImageTk.PhotoImage(real_img)
playerimage = tk.Label(root , image = steve)
playerimage.pack()
playerimage.place(x = 150 , y = 180)
# [playername_lable|playername]玩家名自定义
playername_lable = tk.Label(root , text = '请输入玩家名' , font = ('TkDefaultFont' , 20))
playername_lable.pack()
playername_lable.place(x = 100 , y = 250)
playername = tk.Entry(root)
playername.pack()
playername.place(x = 110 , y = 300)
# [playername_ok_button]确定玩家名
playername_ok_button = tk.Button(root , text = 'OK' , command = playername_ok_button)
playername_ok_button.pack()
playername_ok_button.place(x = 260 , y = 290)
# [startgame]MC，启动！
startgame = tk.Button(root , text = '启动Minecraft' , font = ('TkDefaultFont' , 40) , command = startgame)
startgame.pack(anchor = 'ne')
# [nopoint]千万别点
nopoint = tk.Button(root , command = nopoint)
nopoint.pack()
nopoint.place(x = 840 , y = 470)
# [setting]设置
setting = tk.Button(root , text = '设置' , command = setting)
setting.pack()
setting.place(x = 300 , y = 290)
# 测试
alpha = tk.Button(root , text = 'alpha' , command = alpha)
alpha.pack()
nopoint.place(x = 0 , y = 0)
root.mainloop()