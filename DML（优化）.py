# [DML]Dianguang Minecraft Launcher
# by 二氧化碳已爆炸|mike20131214
# 未经允许|禁止商用
# Minecraft Launcher For Python
# 导入库
import tkinter as tk
import dbm
import ctypes
import os
import webbrowser
import random
from tkinter import messagebox

# 自定义函数
# [playername_ok_button]确定玩家名的调用函数
def playername_ok_button():
    try:
        with dbm.open('playerdata', 'c') as db: 
            db['playername'] = playername.get().encode('utf-8')
        messagebox.showinfo("提示", "玩家名已保存")
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
    try:
        os.system('python nopoint.py')
    except Exception as e:
        messagebox.showerror("错误", f"执行失败: {str(e)}")

# 主程序
# 设置任务名
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml.0.1")
except AttributeError:
    print("非Windows系统，跳过任务名设置")

# 主界面
root = tk.Tk()
root.title('DML 0.1')
root.geometry('850x480')
try:
    root.iconbitmap('icon.ico')
except tk.TclError:
    print("图标文件icon.ico未找到，使用默认图标")
root.resizable(0 , 0)

# [dmltitle]DML标题
dmltitle = tk.Label(root , text = '''    ____  __  _____ 
/ / / / /|_/ / /
 / /_/ / /  / / /___
/_____/_/  /_/_____/''' , font = ('TkDefaultFont' , 20))
dmltitle.place(x=50, y=25)

# [steve|playerimage]史蒂夫头像，纯装饰，无作用
try:
    steve = tk.PhotoImage(file='steve.gif')
    playerimage = tk.Label(root , image = steve)
    playerimage.place(x = 150 , y = 180)
except tk.TclError:
    playerimage = tk.Label(root, text="史蒂夫头像", font=('TkDefaultFont', 12))
    playerimage.place(x=150, y=180)
    print("图片文件steve.gif未找到，使用文本替代")

# [playername_lable|playername]玩家名自定义
playername_lable = tk.Label(root , text = '请输入玩家名' , font = ('TkDefaultFont' , 20))
playername_lable.place(x = 100 , y = 250)

playername = tk.Entry(root)
playername.place(x = 110 , y = 300)

# [playername_ok_button]确定玩家名
playername_ok_btn = tk.Button(root , text = 'OK' , command = playername_ok_button)
playername_ok_btn.place(x = 260 , y = 290)

# [startplay]MC，启动！
startgame_btn = tk.Button(root , text = '启动Minecraft' , font = ('TkDefaultFont' , 40) , command = startgame)
startgame_btn.pack(anchor = 'ne', padx=50, pady=50)

# 千万别点&隐私设置
# 定义全局变量存储警告窗口，避免重复创建
warning_window = None

# 定义在新弹窗中显示"千万别点"按钮的函数
def show_warning_in_new_window():
    global warning_window
    # 检查窗口是否已存在，避免重复创建
    if warning_window is None or not warning_window.winfo_exists():
        # 创建新弹窗
        warning_window = tk.Toplevel(root)
        warning_window.title("提示")
        warning_window.geometry("500x300")  # 弹窗大小
        warning_window.resizable(False, False)
        # 居中显示弹窗
        warning_window.geometry("+%d+%d" % (root.winfo_rootx() + root.winfo_width()//2 - 150,
                                           root.winfo_rooty() + root.winfo_height()//2 - 75))
        
        # 在新弹窗中添加"千万别点"按钮
        warning_btn = tk.Button(warning_window, text="千万别点", 
                            width=15,
                            height=2,
                            bg="white", 
                            fg="red",
                            font=("Arial", 12),
                            command=on_warning_click)
        warning_btn.pack(expand=True)

# 定义隐私设置按钮的点击事件
def on_privacy_click():
    # 在新弹窗中显示"千万别点"按钮
    show_warning_in_new_window()
    # 隐藏隐私设置按钮
    if 'privacy_btn' in globals() and privacy_btn.winfo_exists():
        privacy_btn.destroy()

# 定义点击"千万别点"按钮后的函数
def on_warning_click():
    # 关闭警告窗口
    if warning_window is not None and warning_window.winfo_exists():
        warning_window.destroy()
    
    # 创建新窗口
    new_window = tk.Toplevel(root)
    new_window.title("发生一切情况DML概不负责")
    new_window.geometry("500x500")
    new_window.resizable(True, True)
    
    # 定义关闭窗口时的跳转链接
    close_link = "https://www.bilibili.com/video/BV1QLxqemE6w/?spm_id_from=333.337.search-card.all.click"
    window_closed = False
    
    # 重写窗口关闭事件
    def on_close():
        nonlocal window_closed
        if not window_closed:
            try:
                webbrowser.open(close_link)
            except Exception as e:
                messagebox.showerror("错误", f"无法打开链接: {str(e)}")
            for widget in root.winfo_children():
                if isinstance(widget, tk.Toplevel) and widget != new_window and widget.winfo_exists():
                    widget.destroy()
        new_window.destroy()
    
    new_window.protocol("WM_DELETE_WINDOW", on_close)
    
    # 添加红色文字
    label = tk.Label(new_window, text="DML作者不会受理由于点击千万别点造成的损失。", 
                    fg="red", font=("Arial", 12))
    label.pack(pady=80)
    
    # 定义打开链接的函数
    def open_link(link):
        nonlocal window_closed
        window_closed = True
        try:
            webbrowser.open(link)
        except Exception as e:
            messagebox.showerror("错误", f"无法打开链接: {str(e)}")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget != new_window and widget.winfo_exists():
                widget.destroy()
        new_window.destroy()
    
    # 定义主窗口先随机滑动再缩小消失的动画函数
    def slide_then_shrink_main_window():
        nonlocal window_closed
        window_closed = True
        new_window.destroy()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        start_width = root.winfo_width()
        start_height = root.winfo_height()
        end_width, end_height = 50, 50
        
        # 滑动动画
        slide_steps = 250
        slide_current_step = 0
        
        def slide_animation():
            nonlocal slide_current_step
            if not root.winfo_exists():
                return
                
            if slide_current_step < slide_steps:
                slide_current_step += 1
                
                max_x = max(0, screen_width - start_width)
                max_y = max(0, screen_height - start_height)
                new_x = random.randint(0, max_x)
                new_y = random.randint(0, max_y)
                
                try:
                    root.geometry(f"+{new_x}+{new_y}")
                except tk.TclError:
                    return
                
                root.after(20, slide_animation)
            else:
                shrink_animation()
        
        # 缩小动画
        shrink_steps = 250
        shrink_current_step = 0
        
        x, y = root.winfo_x(), root.winfo_y()
        center_x, center_y = x + start_width//2, y + start_height//2
        
        def shrink_animation():
            nonlocal shrink_current_step
            if not root.winfo_exists():
                return
                
            if shrink_current_step < shrink_steps:
                shrink_current_step += 1
                current_width = int(start_width - (start_width - end_width) * shrink_current_step / shrink_steps)
                current_height = int(start_height - (start_height - end_height) * shrink_current_step / shrink_steps)
                
                current_width = max(current_width, end_width)
                current_height = max(current_height, end_height)
                
                new_x = int(center_x - current_width//2)
                new_y = int(center_y - current_height//2)
                
                new_x = max(0, min(new_x, screen_width - current_width))
                new_y = max(0, min(new_y, screen_height - current_height))
                
                try:
                    root.geometry(f"{current_width}x{current_height}+{new_x}+{new_y}")
                except tk.TclError:
                    return
                
                root.after(20, shrink_animation)
            else:
                if root.winfo_exists():
                    root.destroy()
        
        slide_animation()
    
    # 创建按钮框架
    button_frame = tk.Frame(new_window)
    button_frame.pack(side=tk.BOTTOM, pady=80, fill=tk.X, padx=50)
    
    # 第一个按钮
    link1 = "https://www.bilibili.com/video/BV1UT42167xb/?spm_id_from=333.337.search-card.all.click"
    btn1 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    bg="red", fg="white",
                    command=lambda: open_link(link1))
    btn1.pack(side=tk.LEFT, expand=True)
    
    # 第二个按钮
    link2 = "https://www.bilibili.com/video/BV1x5411o7Kn/?spm_id_from=333.337.search-card.all.click"
    btn2 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    command=lambda: open_link(link2))
    btn2.pack(side=tk.LEFT, expand=True, padx=20)
    
    # 第三个按钮
    btn3 = tk.Button(button_frame, text="取消", width=100//10, height=50//10,
                    command=lambda: [tk.messagebox.showinfo("提示", "才怪"), 
                                     slide_then_shrink_main_window()])
    btn3.pack(side=tk.LEFT, expand=True)

# 创建右下角的"隐私设置"按钮
privacy_btn = tk.Button(root, text="隐私设置", 
                       width=10, height=2,
                       command=on_privacy_click)
privacy_btn.place(relx=0.9, rely=0.9, anchor="se")


root.mainloop()
    
