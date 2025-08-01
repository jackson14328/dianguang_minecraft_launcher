import tkinter as tk
import webbrowser

# 创建主窗口
root = tk.Tk()
root.title("警告")
root.geometry("500x300")  # 初始窗口大小为500*300
root.resizable(True, True)  # 允许调整窗口大小

# 定义点击按钮后的函数
def on_warning_click():
    # 创建新窗口
    new_window = tk.Toplevel(root)
    new_window.title("警告信息")
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
        new_window.destroy()  # 关闭当前窗口
    
    # 定义窗口旋转缩小动画函数 - 确保最终状态正向
    def rotate_shrink_and_close(window):
        nonlocal window_closed
        window_closed = True  # 标记为通过按钮关闭
        
        # 获取当前窗口大小作为动画起始尺寸
        start_width = window.winfo_width()
        start_height = window.winfo_height()
        end_width, end_height = 50, 50
        
        # 获取窗口当前位置并计算中心
        x, y = window.winfo_x(), window.winfo_y()
        center_x, center_y = x + start_width//2, y + start_height//2
        
        # 动画参数 - 确保总旋转角度是360的倍数，最终为正向
        total_rotation = 360 * 2  # 旋转2圈，确保最终角度为0
        steps = 60  # 动画步数，增加步数使旋转更平滑
        
        def update_animation(frame):
            # 计算当前角度（确保最终为0度）
            current_angle = (total_rotation * frame / steps) % 360
            
            # 计算当前大小（从当前尺寸缩小到50*50）
            current_width = int(start_width - (start_width - end_width) * frame / steps)
            current_height = int(start_height - (start_height - end_height) * frame / steps)
            
            # 计算新位置以保持中心不变
            new_x = int(center_x - current_width//2)
            new_y = int(center_y - current_height//2)
            
            # 设置窗口几何参数
            window.geometry(f"{current_width}x{current_height}+{new_x}+{new_y}")
            
            # 更新窗口标题以模拟旋转效果
            # 使用角度计算旋转符号数量，确保最后一步为0
            symbol_count = int(current_angle / 30) % 12
            window.title(f"警告信息 {chr(0x25CB) * symbol_count}")
            
            if frame < steps:
                # 继续动画
                window.after(20, update_animation, frame + 1)
            else:
                # 动画结束，确保窗口标题恢复正常
                window.title("警告信息")
                window.destroy()
        
        # 开始动画
        update_animation(0)
    
    # 创建按钮框架，使按钮在底部分散开
    button_frame = tk.Frame(new_window)
    button_frame.pack(side=tk.BOTTOM, pady=80, fill=tk.X, padx=50)  # 增加边距使按钮分散
    
    # 第一个按钮 - 跳转第一个链接
    link1 = "https://www.bilibili.com/video/BV1UT42167xb/?spm_id_from=333.337.search-card.all.click"
    btn1 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    command=lambda: open_link(link1))
    btn1.pack(side=tk.LEFT, expand=True)  # 扩展以填充空间
    
    # 第二个按钮 - 跳转第二个链接（红色按钮）
    link2 = "https://www.bilibili.com/video/BV1x5411o7Kn/?spm_id_from=333.337.search-card.all.click"
    btn2 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    bg="red", fg="white",  # 红色背景和白色文字
                    command=lambda: open_link(link2))
    btn2.pack(side=tk.LEFT, expand=True, padx=20)  # 中间增加额外间距
    
    # 第三个按钮 - 旋转缩小后消失
    btn3 = tk.Button(button_frame, text="确定", width=100//10, height=50//10,
                    command=lambda: rotate_shrink_and_close(new_window))
    btn3.pack(side=tk.LEFT, expand=True)  # 扩展以填充空间

# 创建"千万别点"按钮（100x50大小的红色按钮）
warning_btn = tk.Button(root, text="千万别点", 
                       width=100//10,  # 宽度大约100像素
                       height=50//10, # 高度大约50像素
                       bg="black", 
                       fg="red",
                       font=("Arial", 12),  # 增大字体
                       command=on_warning_click)
warning_btn.pack(expand=True)  # 居中显示

# 运行主循环
root.mainloop()
