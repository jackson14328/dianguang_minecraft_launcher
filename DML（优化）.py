# [DML]Dianguang Minecraft Launcher
# by 二氧化碳已爆炸|mike20131214
# 未经允许|禁止商用
#Minecraft Launcher For Python
# 导入库
import tkinter as tk
from tkinter import messagebox
import dbm
import ctypes
import os
import random

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
    print('123abc')
    print('you can\'t startgame')
    messagebox.showinfo("提示", "游戏启动功能尚未实现")

# [nopoint]千万别点的调用函数
def nopoint1():
    print('没做好')
def nopoint():
    try:
        os.system('python nopoint.py')
    except Exception as e:
        messagebox.showerror("错误", f"执行失败: {str(e)}")

# 回声洞功能类（新增）
class EchoCave:
    def __init__(self, master):
        self.master = master
        
        # 创建主容器
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)
        
        # 标题
        self.title_label = tk.Label(
            self.main_frame,
            text="回声洞",
            font=("SimHei", 16, "bold")
        )
        self.title_label.pack(anchor="w", pady=(0, 10))
        
        # 提示文本（点完消失）
        self.tip_label = tk.Label(
            self.main_frame,
            text="反复点击这里可以查看DML作者乱七八糟的留言！",
            font=("SimHei", 10),
            wraplength=450,
            justify="left"
        )
        self.tip_label.pack(anchor="w", pady=(0, 10))
        
        # 回声洞交互按钮
        self.interact_btn = tk.Button(
            self.main_frame,
            text="点击查看",
            font=("SimHei", 12),
            command=self.show_echo_content
        )
        self.interact_btn.pack(anchor="w", pady=(0, 20))
        
        # 内容显示区域
        self.content_frame = tk.Frame(self.main_frame, height=100)
        self.content_frame.pack(fill="x", anchor="w")
        
        self.content_label = tk.Label(
            self.content_frame,
            text="",
            font=("SimHei", 10),
            wraplength=450,
            justify="left",
            anchor="w"
        )
        self.content_label.pack(fill="x", anchor="w")
        
        # 文本内容存储
        self.all_texts = []
        self.load_text_files()
        
        # 显示状态控制
        self.is_showing = False
    
    def load_text_files(self):
        """加载同级"话"文件夹中的文本文件"""
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "话")
        
        # 检查文件夹，不存在就警告
        if not os.path.exists(folder_path):
            messagebox.showerror("报错", "未找到同级目录的\"话\"文件夹")
            return
        
        # 加载话1到话12
        for i in range(1, 13):
            file_name = f"话{i}.txt"
            file_path = os.path.join(folder_path, file_name)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        self.all_texts.append(content)
            except FileNotFoundError:
                print(f"警告：未找到文件 {file_path}")
            except Exception as e:
                print(f"读取 {file_path} 出错：{str(e)}")
    
    def show_echo_content(self):
        """点击按钮后显示内容"""
        if not self.all_texts:
            messagebox.showinfo("提示", "没有可显示的内容")
            return
        
        if self.is_showing:
            return
            
        # 首次点击时隐藏提示文本
        if self.tip_label.winfo_exists():
            self.tip_label.destroy()
        
        # 重置显示内容
        self.content_label.config(text="")
        self.is_showing = True
        
        # 随机选择一个文本
        self.current_text = random.choice(self.all_texts)
        self.current_char_index = 0
        
        # 开始逐字显示
        self.show_next_char()
    
    def show_next_char(self):
        """逐字显示文本内容"""
        if not self.is_showing:
            return
            
        if self.current_char_index < len(self.current_text):
            # 添加下一个字
            current_text = self.content_label.cget("text")
            current_text += self.current_text[self.current_char_index]
            self.content_label.config(text=current_text)
            self.current_char_index += 1
            
            # 30毫秒后显示下一个字
            self.master.after(30, self.show_next_char)
        else:
            # 显示完可以再点
            self.is_showing = False

# [setting]设置的调用函数（完善实现）
def setting():
    # 防止重复创建弹窗
    global settings_window
    try:
        if settings_window and settings_window.winfo_exists():
            settings_window.lift()
            return
    except:
        pass

    # 创建设置弹窗
    settings_window = tk.Toplevel(root)
    settings_window.title("设置")
    settings_window.geometry("400x300")  # 弹窗大小
    settings_window.resizable(False, False)

    # 在弹窗中添加回声洞按钮
    echo_cave_btn = tk.Button(
        settings_window,
        text="回声洞",
        font=("SimHei", 12),
        command=open_echo_cave,
        width=20,
        height=2
    )
    echo_cave_btn.pack(pady=50)

    # 其他设置项占位
    settings_label = tk.Label(
        settings_window,
        text="其他设置选项可以在这里添加",
        font=("SimHei", 10)
    )
    settings_label.pack(pady=20)

# 打开回声洞窗口（新增）
def open_echo_cave():
    # 关闭设置弹窗
    global settings_window
    if settings_window and settings_window.winfo_exists():
        settings_window.destroy()

    # 创建回声洞窗口
    echo_window = tk.Toplevel(root)
    echo_window.title("回声洞")
    echo_window.geometry("500x300")
    echo_window.resizable(False, False)

    # 初始化回声洞功能
    EchoCave(echo_window)

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
steve = tk.PhotoImage(file='steve.gif')
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

# [startplay]MC，启动！
startgame = tk.Button(root , text = '启动Minecraft' , font = ('TkDefaultFont' , 40) , command = startgame)
startgame.pack(anchor = 'ne')

# [nopoint]千万别点
nopoint = tk.Button(root , text = '这真的不是彩蛋' , command = nopoint1)
nopoint = tk.Button(root , text = '这真的不是彩蛋' , command = nopoint)
nopoint.pack()
nopoint.place(x = 840 , y = 470)

# [setting]设置
setting_btn = tk.Button(root , text = '设置' , command = setting)
setting_btn.pack()
setting_btn.place(x = 300 , y = 290)

root.mainloop()
