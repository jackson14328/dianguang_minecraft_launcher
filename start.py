import minecraft_launcher_lib
import subprocess
import os
from tkinter import messagebox
 
class DownloadProgress:
    def __init__(self):
        self.current_max = 0
        self.current_progress = 0
    
    def set_status(self, status: str):
        print(f"📦 {status}")
    
    def set_progress(self, progress: int):
        if self.current_max > 0:
            self.current_progress = progress
            percentage = (progress / self.current_max) * 100
            print(f"进度: {progress}/{self.current_max} ({percentage:.1f}%)")
    
    def set_max(self, new_max: int):
        self.current_max = new_max
        print(f"总任务数: {new_max}")

current_max = 0
 
 
def set_status(status: str):
    print(status)
 
 
def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")
 
 
def set_max(new_max: int):
    global current_max
    current_max = new_max
 
 
def mkdir(path):
    folder = os.path.exists(path)
 
    if not folder:
        os.makedirs(path)
 
    else:
        pass
 

def gamestart(player_name="str", minecraft_dir= "str", minecraft_version="str", JVM='str', JavaPath = "str"):
    minecraft_launcher_lib.install.install_minecraft_version(minecraft_version, minecraft_dir)
    options = minecraft_launcher_lib.utils.generate_test_options()
    Xmx = "-Xmx" + JVM
    player_name = str(player_name)
    JavaPath = JavaPath + "/bin/java.exe"
    options['jvmArguments'] = [Xmx]
    options['username'] = player_name
    options['executablePath'] = JavaPath
    options["launcherName"] = 'DML'# 启动器名
    options["launcherVersion"] = '0.1'# 版本
    # 启动命令
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(minecraft_version, minecraft_dir, options)
    subprocess.run(minecraft_command)


import minecraft_launcher_lib
import os
from pathlib import Path

import minecraft_launcher_lib
import os

def download_minecraft_version(version_name: str, minecraft_dir: str):
    """
    下载指定版本的 Minecraft
    
    Args:
        version_name (str): Minecraft 版本名，如 "1.20.1", "1.19.2"
        minecraft_dir (str): .minecraft 文件夹路径
    """
    try:
        # 检查版本是否可用
        available_versions = minecraft_launcher_lib.utils.get_available_versions(minecraft_dir)
        version_names = [v['id'] for v in available_versions]
        
        if version_name not in version_names:
            print(f"版本 '{version_name}' 不在可用版本列表中")
            print(f"可用版本: {', '.join(version_names)}")
            return False
        
        # 下载版本
        print(f"开始下载 Minecraft {version_name}...")
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version_name,
            minecraft_directory=minecraft_dir
        )
        
        messagebox.showinfo('提示' , '下载成功')
        return True
        
    except Exception as e:
        messagebox.showerror("错误", '下载失败')
        return False

# 使用示例
if __name__ == "__main__":
    # 示例用法
    version = "1.20.1"
    minecraft_path = os.path.join(os.getenv('APPDATA'), '.minecraft')  # Windows 默认路径
    # 或者指定自定义路径: minecraft_path = "C:/path/to/.minecraft"
    
    download_minecraft_version(version, minecraft_path)