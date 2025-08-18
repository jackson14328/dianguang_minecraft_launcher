import minecraft_launcher_lib
import subprocess
import os
 
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
 

def GameStart(player_name="str", minecraft_dir= "str", minecraft_version="str", JVM='str', JavaPath = "str"):
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

GameStart(
    player_name="player",# 玩家名
    minecraft_dir=r"E:\DML\minecraft",# 游戏目录
    minecraft_version="1.8.9",# 游戏版本
    JVM="4G",# 最大内存占用
    JavaPath=r"C:\Program Files\Java\jre1.8.0_461"# java路径
)
