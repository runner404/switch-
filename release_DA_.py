import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

"""分析各年度游戏发布数量的变化"""

# 连接SQLite数据库
db_file = 'games.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 执行查询并获取结果
cursor.execute("SELECT game_name, release_date FROM vgc_info WHERE release_date IS NOT NULL")
release_info = cursor.fetchall()

# 创建DataFrame，列名与查询结果匹配
release_df = pd.DataFrame(release_info, columns=['Game', 'Release_Date'])

# 将发布日期转换为日期时间对象，并提取年份
release_df['Release_Date'] = pd.to_datetime(release_df['Release_Date'])
release_df['Year'] = release_df['Release_Date'].dt.year

# 绘制折线图前去除2024年的数据
yearly_releases = release_df[release_df['Year'] != 2024].groupby('Year').size()
print(yearly_releases)

# 绘制折线图
plt.figure(figsize=(10, 6))
yearly_releases.plot(kind='line', marker='o')  # 使用折线图，带有圆点标记
plt.title('Annual Game Releases on Nintendo Switch (excluding 2024 data)')
plt.xlabel('Year')
plt.ylabel('Number of Games Released')
plt.xticks(rotation=45)  # 旋转x轴标签，以便更清晰地显示
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()

# 关闭数据库连接
conn.close()