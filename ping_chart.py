import re
import matplotlib.pyplot as plt

# 读取 ping 日志文件
with open('ping.log', 'r') as file:
    lines = file.readlines()

# 提取时间和延迟数据
times = []
delays = []

for line in lines:
    match = re.search(r'time=(\d+\.\d+) ms', line)
    if match:
        times.append(len(times) + 1)  # 使用行号作为时间轴
        delays.append(float(match.group(1)))

# 生成折线图
plt.plot(times, delays, marker='o')

# 添加标题和标签
plt.title('Ping Latency Over Time')
plt.xlabel('Ping Sequence')
plt.ylabel('Latency (ms)')

# 设置 y 轴从 0 开始
plt.ylim(bottom=0)

# 显示图表
plt.show()
