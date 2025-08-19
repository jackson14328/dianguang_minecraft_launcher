# 新的设置，由二氧化碳已爆炸编写
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import ctypes
import java
import dbm

javalist = java.scan_java_installations_windows()
def hsd():
    sjs = random.randint(1, 13)
    say = open('say\say' + str(sjs) + '.txt', 'r' , encoding='utf-8')
    s = say.read()
    say.close()
    messagebox.showinfo('回声洞' , s)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml_setting.0.1")
def javaljok():
    with dbm.open('playerdata', 'c') as db: 
        db['javalj'] = javalj.get().encode('utf-8')
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
root.mainloop()