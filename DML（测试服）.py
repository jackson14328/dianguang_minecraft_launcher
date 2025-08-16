# [DML]Dianguang Minecraft Launcher
# by 二氧化碳已爆炸|mike20131214
# 未经允许|禁止商用
# Minecraft Launcher For Python
import tkinter as tk
from tkinter import messagebox
import dbm
import ctypes
import os
import random
from PIL import Image, ImageTk  # 导入Pillow库，务必先安装：pip install pillow

# 全局变量：存储当前壁纸状态
current_wallpaper_img = None  # 用于保持 PhotoImage的引用
is_original = True            # 标记是否为“原版”纯色壁纸

# 自定义函数：确认玩家名
def playername_ok_button():
    try:
        with dbm.open('playerdata', 'c') as db:
            db['playername'] = playername.get().encode('utf-8')
    except Exception as e:
        messagebox.showerror("错误", f"保存失败: {str(e)}")

# 自定义函数：启动游戏（占位）
def startgame():
    messagebox.showinfo("提示", "游戏启动功能尚未实现")

# 自定义函数：彩蛋按钮（占位）
def nopoint1():
    print('没做好')
def nopoint():
    try:
        os.system('python nopoint.py')
    except Exception as e:
        messagebox.showerror("错误", f"执行失败: {str(e)}")

# 回声洞功能类
class EchoCave:
    def __init__(self, master):
        self.master = master
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)

        # 标题与提示
        self.title_label = tk.Label(self.main_frame, text="回声洞", font=("SimHei", 16, "bold"))
        self.title_label.pack(anchor="w", pady=(0, 10))
        self.tip_label = tk.Label(self.main_frame, text="反复点击查看留言！", font=("SimHei", 10), wraplength=450)
        self.tip_label.pack(anchor="w", pady=(0, 10))

        # 交互按钮
        self.interact_btn = tk.Button(self.main_frame, text="点击查看", font=("SimHei", 12), command=self.show_echo_content)
        self.interact_btn.pack(anchor="w", pady=(0, 20))

        # 内容显示
        self.content_frame = tk.Frame(self.main_frame, height=100)
        self.content_frame.pack(fill="x", anchor="w")
        self.content_label = tk.Label(self.content_frame, text="", font=("SimHei", 10), wraplength=450, anchor="w")
        self.content_label.pack(fill="x", anchor="w")

        # 加载文本
        self.all_texts = []
        self.load_text_files()
        self.is_showing = False

    def load_text_files(self):
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "say")
        if not os.path.exists(folder_path):
            messagebox.showerror("报错", "未找到\"say\"文件夹")
            return
        for i in range(1, 13):
            file_path = os.path.join(folder_path, f"say{i}.txt")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        self.all_texts.append(content)
            except Exception as e:
                print(f"读取 {file_path} 出错：{str(e)}")

    def show_echo_content(self):
        if not self.all_texts:
            messagebox.showinfo("提示", "无内容可显示")
            return
        if self.is_showing:
            return
        if self.tip_label.winfo_exists():
            self.tip_label.destroy()
        self.content_label.config(text="")
        self.is_showing = True
        self.current_text = random.choice(self.all_texts)
        self.current_char_index = 0
        self.show_next_char()

    def show_next_char(self):
        if not self.is_showing:
            return
        if self.current_char_index < len(self.current_text):
            current_text = self.content_label.cget("text") + self.current_text[self.current_char_index]
            self.content_label.config(text=current_text)
            self.current_char_index += 1
            self.master.after(30, self.show_next_char)
        else:
            self.is_showing = False

# 核心功能：更换壁纸（使用bg=None修复透明背景错误）
def change_wallpaper(absolute_path, is_original_wallpaper):
    global current_wallpaper_img, is_original, background_label
    
    if is_original_wallpaper:
        # 处理“原版”纯色壁纸（保持白色背景）
        background_label.config(image="", bg="white")
        # 恢复元素白色背景
        dmltitle.config(bg="white")
        playerimage.config(bg="white")
        playername_lable.config(bg="white")
        playername.config(bg="white")  # 输入框恢复白色背景
        startgame_btn.config(bg=root.cget("bg"))
        setting_btn.config(bg=root.cget("bg"))
        playername_ok_button.config(bg=root.cget("bg"))
        nopoint_btn.config(bg=root.cget("bg"))
        is_original = True
        messagebox.showinfo("提示", "已更换为原版壁纸（纯白色）")
        return
    
    try:
        # 1. 验证文件是否存在
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"文件不存在，请检查路径：{absolute_path}")
        
        # 2. 用Pillow加载并预处理图片（完全覆盖窗口）
        pil_image = Image.open(absolute_path)
        pil_image = pil_image.convert("RGB")  # 统一格式
        
        # 获取窗口大小
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        
        # 计算缩放比例（保持宽高比，完全覆盖窗口）
        img_width, img_height = pil_image.size
        scale = max(window_width / img_width, window_height / img_height)
        
        # 按比例缩放图片（确保填满窗口无留白）
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)  # 高质量缩放
        
        # 3. 转换为Tkinter可用格式并保持引用
        current_wallpaper_img = ImageTk.PhotoImage(pil_image)
        
        # 4. 更新背景（完全覆盖窗口，无留白）
        background_label.config(image=current_wallpaper_img, bg=None)
        
        # 关键修复：使用bg=None替代systemTransparent，避免颜色名称错误
        dmltitle.config(bg=None)
        playerimage.config(bg=None)
        playername_lable.config(bg=None)
        playername.config(bg=None)  # 输入框透明背景
        startgame_btn.config(bg=None)
        setting_btn.config(bg=None)
        playername_ok_button.config(bg=None)
        nopoint_btn.config(bg=None)
        
        messagebox.showinfo("提示", f"已更换为全屏壁纸\n路径：{absolute_path}")
        
    except Exception as e:
        messagebox.showerror("错误", f"更换失败：{str(e)}")
        print(f"详细错误：{e}")  # 控制台打印详细信息

# 打开壁纸设置窗口
def open_wallpaper_settings():
    wallpaper_window = tk.Toplevel(root)
    wallpaper_window.title("更换壁纸")
    wallpaper_window.geometry("300x250")
    wallpaper_window.resizable(False, False)

    tk.Label(wallpaper_window, text="选择壁纸", font=("SimHei", 12, "bold")).pack(pady=10)
    
    # 壁纸绝对路径（请确保与实际文件位置完全一致）
    wallpaper_paths = {
        "jojo": r"\background_image\jojo.jpg",
        "原神": r"\background_image\genshin_impact.jpg",
        "火影": r"\background_image\naruto.jpg",
        "原版": ""
    }

    for name in ["jojo", "原神", "火影", "原版"]:
        btn = tk.Button(
            wallpaper_window,
            text=name,
            font=("SimHei", 10),
            width=15,
            command=lambda path=wallpaper_paths[name], is_orig=(name=="原版"): [
                change_wallpaper(path, is_orig), 
                wallpaper_window.destroy()
            ]
        )
        btn.pack(pady=5)

# 设置按钮逻辑
def setting():
    global settings_window
    try:
        if settings_window and settings_window.winfo_exists():
            settings_window.lift()
            return
    except:
        pass
    settings_window = tk.Toplevel(root)
    settings_window.title("设置")
    settings_window.geometry("400x300")
    settings_window.resizable(False, False)

    # 壁纸设置区
    tk.Label(settings_window, text="个性化设置", font=("SimHei", 11, "bold")).pack(pady=10)
    tk.Button(
        settings_window,
        text="更换壁纸",
        font=("SimHei", 10),
        command=open_wallpaper_settings
    ).pack(pady=5)
    tk.Label(settings_window, text="", height=1).pack()  # 分隔线

    # 回声洞区
    tk.Label(settings_window, text="其他功能", font=("SimHei", 11, "bold")).pack(pady=10)
    tk.Button(
        settings_window,
        text="回声洞",
        font=("SimHei", 12),
        command=open_echo_cave,
        width=20,
        height=2
    ).pack(pady=5)

# 打开回声洞窗口
def open_echo_cave():
    global settings_window
    if 'settings_window' in globals() and settings_window.winfo_exists():
        settings_window.destroy()
    echo_window = tk.Toplevel(root)
    echo_window.title("回声洞")
    echo_window.geometry("500x300")
    echo_window.resizable(False, False)
    EchoCave(echo_window)

# 主程序入口
if __name__ == "__main__":
    # 设置任务栏图标（增加异常处理，兼容非Windows系统）
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml.0.1")
    except:
        pass
    
    # 初始化主窗口
    root = tk.Tk()
    root.title('DML 0.1')
    root.geometry('850x480')
    try:
        root.iconbitmap('icon.ico')  # 图标不存在时不报错
    except:
        pass
    root.resizable(0, 0)

    # 背景标签（核心：用于显示壁纸，完全覆盖窗口）
    background_label = tk.Label(root)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # 完全铺满窗口

    # 标题（初始白色背景，切换壁纸后透明）
    dmltitle = tk.Label(root, text='''    ____  __  _____ 
   /__  \/  | / / /
/ / / / /|_/ / /
 / /_/ / /  / / /___
/_____/_/  /_/_____/''', font=('TkDefaultFont', 20), bg='white')
    dmltitle.place(x=50, y=25)

    # 史蒂夫头像（初始白色背景，切换壁纸后透明）
    try:
        steve = tk.PhotoImage(file='steve.gif')
        playerimage = tk.Label(root, image=steve, bg='white')
        playerimage.place(x=150, y=180)
        playerimage.image = steve  # 保持引用
    except Exception as e:
        messagebox.showwarning("提示", f"史蒂夫头像加载失败：{str(e)}")
        playerimage = tk.Label(root, text="头像丢失", bg='white')
        playerimage.place(x=150, y=180)

    # 玩家名输入（初始白色背景，切换壁纸后透明）
    playername_lable = tk.Label(root, text='请输入玩家名', font=('TkDefaultFont', 20), bg='white')
    playername_lable.place(x=100, y=250)
    playername = tk.Entry(root, bg='white')  # 初始白色背景
    playername.place(x=110, y=300)
    playername_ok_button = tk.Button(root, text='OK', command=playername_ok_button)
    playername_ok_button.place(x=260, y=290)

    # 启动游戏按钮（初始默认背景，切换壁纸后透明）
    startgame_btn = tk.Button(root, text='启动Minecraft', font=('TkDefaultFont', 40), command=startgame)
    startgame_btn.pack(anchor='ne')

    # 彩蛋按钮（初始默认背景，切换壁纸后透明）
    nopoint_btn = tk.Button(root, text='这真的不是彩蛋', command=nopoint1)
    nopoint_btn.place(x=840, y=470)

    # 设置按钮（初始默认背景，切换壁纸后透明）
    setting_btn = tk.Button(root, text='设置', command=setting)
    setting_btn.place(x=300, y=290)

    # 强制刷新窗口以获取正确尺寸
    root.update_idletasks()
    
    root.mainloop()
