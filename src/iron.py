from mcpi.minecraft import Minecraft
from mcpi import block
import time
# 连接到 Minecraft 服务器
mc = Minecraft.create()

# 获取玩家的当前位置
x, y, z = mc.player.getTilePos()

# 生成铁傀儡的结构
# 放置铁块形成 T 形
time.sleep(1)
mc.setBlock(x, y, z, block.IRON_BLOCK.id)
time.sleep(1)          # 身体
mc.setBlock(x, y + 1, z, block.IRON_BLOCK.id) 
time.sleep(1)     # 身体
mc.setBlock(x - 1, y + 1, z, block.IRON_BLOCK.id) 
time.sleep(1) # 左臂
mc.setBlock(x + 1, y + 1, z, block.IRON_BLOCK.id)  # 右臂

# 放置南瓜头
time.sleep(2)
mc.setBlock(x, y + 2, z, block.PUMPKIN.id)  # 南瓜头（可以是雕刻的南瓜）

print("铁傀儡生成完毕！")
