import tkinter as tk
import webbrowser
import random
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("千万别点")
root.geometry("500x300")  # 初始窗口大小为500*300
root.resizable(True, True)  # 允许调整窗口大小

# 定义点击按钮后的函数
def on_warning_click():
    # 创建新窗口
    new_window = tk.Toplevel(root)
    new_window.title("发生一切情况DML概不负责")
    new_window.geometry("500x500")  # 初始窗口大小为500*500
    new_window.resizable(True, True)  # 允许调整窗口大小
    
    # 定义关闭窗口时的跳转链接
    close_link = "https://www.bilibili.com/video/BV1QLxqemE6w/?spm_id_from=333.337.search-card.all.click"
    window_closed = False  # 标记窗口是否已通过按钮关闭
    
    # 重写窗口关闭事件
    def on_close():
        nonlocal window_closed
        if not window_closed:
            webbrowser.open(close_link)
            # 关闭除主窗口外的所有窗口
            for widget in root.winfo_children():
                if isinstance(widget, tk.Toplevel) and widget != new_window:
                    widget.destroy()
        new_window.destroy()
    
    new_window.protocol("WM_DELETE_WINDOW", on_close)
    
    # 添加红色文字
    label = tk.Label(new_window, text="DML作者不会受理由于点击千万别点造成的损失。", 
                    fg="red", font=("Arial", 12))
    label.pack(pady=80)  # 添加上边距
    
    # 定义打开链接的函数 - 跳转后关闭窗口
    def open_link(link):
        nonlocal window_closed
        window_closed = True  # 标记为通过按钮关闭
        webbrowser.open(link)
        # 关闭除主窗口外的所有窗口
        for widget in root.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget != new_window:
                widget.destroy()
        new_window.destroy()  # 关闭当前窗口
    
    # 定义主窗口先随机滑动再缩小消失的动画函数
    def slide_then_shrink_main_window():
        nonlocal window_closed
        window_closed = True  # 标记为通过按钮关闭
        new_window.destroy()  # 先关闭当前窗口
        
        # 获取屏幕尺寸，用于限制窗口移动范围
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # 获取主窗口初始大小
        start_width = root.winfo_width()
        start_height = root.winfo_height()
        end_width, end_height = 50, 50
        
        # 滑动动画参数（5秒）
        slide_steps = 250  # 滑动步数，约5秒(250*20ms)
        slide_current_step = 0
        
        # 滑动动画函数
        def slide_animation():
            nonlocal slide_current_step
            if slide_current_step < slide_steps:
                slide_current_step += 1
                
                # 随机计算新位置，确保窗口不会超出屏幕
                max_x = screen_width - start_width
                max_y = screen_height - start_height
                new_x = random.randint(0, max_x)
                new_y = random.randint(0, max_y)
                
                # 设置主窗口位置
                root.geometry(f"+{new_x}+{new_y}")
                
                # 继续滑动动画
                root.after(20, slide_animation)
            else:
                # 滑动结束，开始缩小动画
                shrink_animation()
        
        # 缩小动画参数
        shrink_steps = 250  # 缩小步数，约5秒(250*20ms)
        shrink_current_step = 0
        
        # 获取缩小开始时的窗口位置并计算中心
        x, y = root.winfo_x(), root.winfo_y()
        center_x, center_y = x + start_width//2, y + start_height//2
        
        # 缩小动画函数
        def shrink_animation():
            nonlocal shrink_current_step
            if shrink_current_step < shrink_steps:
                shrink_current_step += 1
                # 计算当前大小（从当前尺寸缩小到50*50）
                current_width = int(start_width - (start_width - end_width) * shrink_current_step / shrink_steps)
                current_height = int(start_height - (start_height - end_height) * shrink_current_step / shrink_steps)
                
                # 计算新位置以保持中心不变
                new_x = int(center_x - current_width//2)
                new_y = int(center_y - current_height//2)
                
                # 设置主窗口几何参数
                root.geometry(f"{current_width}x{current_height}+{new_x}+{new_y}")
                
                # 继续缩小动画
                root.after(20, shrink_animation)
            else:
                # 动画结束，关闭主窗口
                root.destroy()
        
        # 开始滑动动画
        slide_animation()
    
    # 创建按钮框架，使按钮在底部分散开
    button_frame = tk.Frame(new_window)
    button_frame.pack(side=tk.BOTTOM, pady=80, fill=tk.X, padx=50)  # 增加边距使按钮分散
    
    # 第一个按钮 - 跳转第一个链接（红色按钮）
    link1 = "https://www.bilibili.com/video/BV1UT42167xb/?spm_id_from=333.337.search-card.all.click"
    btn1 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    bg="red", fg="white",  # 红色背景和白色文字
                    command=lambda: open_link(link1))
    btn1.pack(side=tk.LEFT, expand=True)  # 扩展以填充空间
    
    # 第二个按钮 - 跳转第二个链接
    link2 = "https://www.bilibili.com/video/BV1x5411o7Kn/?spm_id_from=333.337.search-card.all.click"
    btn2 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    command=lambda: open_link(link2))
    btn2.pack(side=tk.LEFT, expand=True, padx=20)  # 中间增加额外间距
    
    # 第三个按钮 - 让主窗口先随机滑动5秒再缩小消失
    btn3 = tk.Button(button_frame, text="取消", width=100//10, height=50//10,
                    command=lambda: [tk.messagebox.showinfo("提示", "才怪"), 
                                     slide_then_shrink_main_window()])
    btn3.pack(side=tk.LEFT, expand=True)

# 创建"千万别点"按钮
warning_btn = tk.Button(root, text="千万别点", 
                       width=100//10,  # 宽度大约100像素
                       height=10//10, # 高度大约10像素
                       bg="white", 
                       fg="red",
                       font=("Arial", 12),  # 增大字体
                       command=on_warning_click)
warning_btn.pack(expand=True)  # 居中显示

# 运行主循环
root.mainloop()
