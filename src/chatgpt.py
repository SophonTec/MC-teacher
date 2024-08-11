import requests
from mcpi.minecraft import Minecraft
import time

# 连接到 Minecraft 服务器
mc = Minecraft.create()

# OpenAI API 配置
API_KEY = ''
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def get_chatgpt_response(prompt):
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return "Error: Unable to get response from ChatGPT"

def monitor_chat():
    previous_messages = set()
    while True:
        messages = mc.events.pollChatPosts()
        for message in messages:
            if message not in previous_messages:
                previous_messages.add(message)
                player_name = message.entityId
                player_message = message.message
                chatgpt_response = get_chatgpt_response(player_message)
                mc.postToChat(f"ChatGPT: {chatgpt_response}")
        time.sleep(1)

if __name__ == "__main__":
    monitor_chat()
