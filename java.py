import os
import subprocess
import winreg
from typing import List

def scan_java_installations_windows() -> List[str]:
    """
    扫描Windows系统中的Java安装路径
    
    返回:
        List[str]: 包含所有找到的Java路径的列表
    """
    java_paths = []
    
    # 1. 检查JAVA_HOME环境变量
    java_home = os.environ.get('JAVA_HOME')
    if java_home and os.path.isdir(java_home):
        java_paths.append(java_home)
    
    # 2. 检查注册表中的Java安装信息
    try:
        # 检查64位系统的注册表
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                               r"SOFTWARE\JavaSoft\Java Development Kit")
        for i in range(winreg.QueryInfoKey(reg_key)[0]):
            subkey_name = winreg.EnumKey(reg_key, i)
            subkey = winreg.OpenKey(reg_key, subkey_name)
            java_home = winreg.QueryValueEx(subkey, "JavaHome")[0]
            if os.path.isdir(java_home) and java_home not in java_paths:
                java_paths.append(java_home)
    except WindowsError:
        pass
    
    try:
        # 检查32位系统的注册表(在64位系统上)
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                               r"SOFTWARE\WOW6432Node\JavaSoft\Java Development Kit")
        for i in range(winreg.QueryInfoKey(reg_key)[0]):
            subkey_name = winreg.EnumKey(reg_key, i)
            subkey = winreg.OpenKey(reg_key, subkey_name)
            java_home = winreg.QueryValueEx(subkey, "JavaHome")[0]
            if os.path.isdir(java_home) and java_home not in java_paths:
                java_paths.append(java_home)
    except WindowsError:
        pass
    
    # 3. 扫描常见的Java安装目录
    common_paths = [
        r"C:\Program Files\Java",
        r"C:\Program Files (x86)\Java",
        r"C:\Java",
        r"D:\Java",
        r"D:\Program Files\Java"
    ]
    
    for path in common_paths:
        if os.path.isdir(path):
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    # 检查是否是有效的Java目录 (包含bin\java.exe)
                    java_exe_path = os.path.join(full_path, "bin", "java.exe")
                    if os.path.isfile(java_exe_path) and full_path not in java_paths:
                        java_paths.append(full_path)
    
    # 4. 使用where命令查找PATH中的java.exe
    try:
        result = subprocess.run(["where", "java"], capture_output=True, text=True)
        if result.returncode == 0:
            java_exe = result.stdout.strip().split('\n')[0]
            java_dir = os.path.dirname(os.path.dirname(java_exe))
            if os.path.isdir(java_dir) and java_dir not in java_paths:
                java_paths.append(java_dir)
    except:
        pass
    
    return java_paths
