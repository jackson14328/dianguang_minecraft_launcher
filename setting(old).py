import tkinter as tk
import random
import os
from tkinter import messagebox
import ctypes


# 回声洞
class EchoCave:
    def __init__(self, root):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dml.dml_setting.0.1")
        self.root = root
        root.title("设置")
        root.geometry("500x300")
        root.iconbitmap('icon.ico')

        # 构建回声洞交互界面
        self.build_echo_interface(root)

    def build_echo_interface(self, master):
        """构建回声洞交互内容"""
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
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "say")

        # 检查文件夹，不存在就警告
        if not os.path.exists(folder_path):
            messagebox.showerror("报错", "say文件夹丢失")
            return

        # 加载文本文件
        for i in range(1, 15):
            file_name = f"say{i}.txt"
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
        # 如果没有文本内容，提示报错并返回
        if not self.all_texts:
            messagebox.showinfo("提示", "没有可显示的内容")
            return

        # 防止重复点击导致显示鬼畜
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
            self.root.after(30, self.show_next_char)
        else:
            # 显示完可再次点击
            self.is_showing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = EchoCave(root)
    root.mainloop()