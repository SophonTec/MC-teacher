import requests
from mcpi.minecraft import Minecraft
from mcpi import vec3
import time
import os
from dotenv import load_dotenv
from javascript import require, On, console

load_dotenv()

# 载入 mineflayer 模块
mineflayer = require("mineflayer")
# import mineflayer from 'mineflayer'

BOT_NAME = "test_ironman"
DEBUG = True
COMMAND_TAG = "$"

# 配置服务器信息
HOST = '127.0.0.1'  # 替换为你的服务器地址
PORT = 25565        # 替换为你的服务器端口
USERNAME = BOT_NAME

# 创建 mineflayer 机器人
bot = mineflayer.createBot({
    'host': HOST,
    'port': PORT,
    'username': USERNAME,
    'version': '1.19.4',  # 确保版本与服务器匹配
})

# OpenAI API 配置
API_KEY = os.environ["OPENAI_API"]
print(API_KEY)
API_URL = 'https://api.openai.com/v1/chat/completions'  # GPT-4 Chat API

def get_chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': 'gpt-4o',  # GPT-4 模型
        'messages': [
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 3000
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception: {str(e)}"

previous_messages = set()

@On(bot, 'spawn')
def handle_spawn(*args):
    print("Bot spawned successfully")
    bot.chat("你好！我是一个机器人。")

@On(bot, 'chat')
def handle_chat(this, username, message, *args):
    if username == bot.username:
        return
    
    if DEBUG:
        print(f"USER: {message}")

    if message.startswith(COMMAND_TAG):  # user command
        message = message[1:].lower()
        print(f"USER Com: {message}")
        if message.startswith("ironman"):
            generate_ironman()
    else:  # user dialog
        previous_messages.add(message)
        response = get_chatgpt_response(message)
        if DEBUG:
            print(f"GPT: {response}")
        bot.chat(f"{BOT_NAME}: {response}")

@On(bot, 'end')
def handle_end(*args):
    print("Bot ended")

@On(bot, 'error')
def handle_error(*args):
    print("An error occurred:", args)

def generate_ironman():
    from mcpi.minecraft import Minecraft
    from mcpi import block
    import time
    # 连接到 Minecraft 服务器
    mc = Minecraft.create()

    # 获取玩家的当前位置
    x, y, z = mc.player.getTilePos()

    # new position
    x, y, z = x, y, z + 2
    # 生成铁傀儡的结构
    # 放置铁块形成 T 形
    mc.setBlock(x, y, z, block.IRON_BLOCK.id)  # 身体
    time.sleep(1)
    mc.setBlock(x, y + 1, z, block.IRON_BLOCK.id)  # 身体
    time.sleep(1)
    mc.setBlock(x - 1, y + 1, z, block.IRON_BLOCK.id)  # 左臂
    time.sleep(1)
    mc.setBlock(x + 1, y + 1, z, block.IRON_BLOCK.id)  # 右臂

    # 放置南瓜头
    time.sleep(2)
    mc.setBlock(x, y + 2, z, block.PUMPKIN.id)  # 南瓜头（可以是雕刻的南瓜）

    print("铁傀儡生成完毕！")
