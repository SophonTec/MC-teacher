import time
from mcpi.minecraft import Minecraft
from javascript import require, On

# 载入 mineflayer 模块
mineflayer = require("mineflayer")

# 配置服务器信息
HOST = '127.0.0.1'  # 替换为你的服务器地址
PORT = 25565        # 替换为你的服务器端口
USERNAME = 'test_sugarcane'

# 创建 mineflayer 机器人
bot = mineflayer.createBot({
    'host': HOST,
    'port': PORT,
    'username': USERNAME,
    'version': '1.19.4',  # 确保版本与服务器匹配
})

# 连接到 Minecraft 服务器
mc = Minecraft.create()

@On(bot, 'spawn')
def handle_spawn(*args):
    print("Bot spawned successfully")
    bot.chat("你好！我是一个机器人。")

@On(bot, 'chat')
def handle_chat(this, username, message, *args):
    if username == bot.username:
        return

    # 检测玩家是否在聊天中提到 "sugarcane"
    if "sugarcane" in message.lower():
        generate_sugarcane_machine()

def generate_sugarcane_machine():
    # 获取玩家当前位置
    x, y, z = mc.player.getTilePos()

    # 定义需要依次加载的结构文件
    schematics = ["test1", "test2", "test3", "test4"]

    # 循环加载并粘贴每个结构文件，确保顺序是 1 -> 2 -> 3 -> 4
    for schematic in schematics:
        # 加载结构文件
        bot.chat(f"//schematic load {schematic}")
        time.sleep(1)  # 等待加载完成

        # 粘贴结构
        bot.chat("//paste -a")
        time.sleep(2)  # 每个结构之间等待2秒，确保按顺序生成

    print("甘蔗机生成完毕！")

@On(bot, 'end')
def handle_end(*args):
    print("Bot ended")

@On(bot, 'error')
def handle_error(*args):
    print("An error occurred:", args)
