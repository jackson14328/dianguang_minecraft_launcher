# 新的设置，由二氧化碳已爆炸编写
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import ctypes
import java
import dbm
import os


def hsd():
    sjs = random.randint(1, 13)
    say = open('say\say' + str(sjs) + '.txt', 'r' , encoding='utf-8')
    s = say.read()
    say.close()
    messagebox.showinfo('回声洞' , s)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml_setting.0.1")
def javaljok():
    with dbm.open('playerdata', 'c') as db: 
        db['javalist'] = javalj.get().encode('utf-8')
def listt(directory_path):
    try:
        # 获取目录下的所有条目
        entries = os.listdir(directory_path)
        
        # 筛选出文件夹
        folders = [entry for entry in entries 
                  if os.path.isdir(os.path.join(directory_path, entry))]
        
        return folders
    
    except FileNotFoundError:
        return ['error']
    except PermissionError:
        return ['error']
def gamevok():
    with dbm.open('playerdata', 'c') as db: 
        db['gamev'] = gamev.get().encode('utf-8')
def gamelistok():
    with dbm.open('playerdata', 'c') as db: 
        db['gamelist'] = gamelist.get().encode('utf-8')
javalist = java.scan_java_installations_windows()
with dbm.open('playerdata', 'c') as db: 
        gamel = db['gamelist'].decode('utf-8')
gamev = listt(gamel + '/versions')
# 主界面
root = tk.Tk()
root.title('DML setting')
root.geometry('850x480')
root.iconbitmap('icon.ico')
root.resizable(0 , 0)
# 回声洞
hsd = tk.Button(root , text = '回声洞' , command = hsd)
hsd.pack()
# 选择java路径
javalj = ttk.Combobox(root , values = javalist)
javalj.pack()
# 确定
javaljok = tk.Button(root , text = '确定Java路径' , command = javaljok)
javaljok.pack()
# 选择游戏版本
gamev = ttk.Combobox(root , values = gamev)
gamev.pack()
# 确定
gamevok = tk.Button(root , text = '确定游戏版本' , command = gamevok)
gamevok.pack()
# 选择游戏目录
gamelist = tk.Entry(root)
gamelist.pack()
# 确定
gamelistok = tk.Button(root , text = '确定游戏目录' , command = gamelistok)
gamelistok.pack()
root.mainloop()