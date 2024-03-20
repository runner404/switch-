import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

"""各评分指标与游戏销售数量的相关性分析"""

# 连接SQLite数据库
db_file = 'games.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 执行查询并获取结果
cursor.execute("SELECT game_name, vgchartz_score, total_shipped FROM vgc_info WHERE vgchartz_score and total_shipped IS NOT NULL")
vgchartz_info = cursor.fetchall()

cursor.execute("SELECT game_name, critic_score, total_shipped FROM vgc_info WHERE critic_score and total_shipped IS NOT NULL")
critic_info = cursor.fetchall()

cursor.execute("SELECT game_name, user_score, total_shipped FROM vgc_info WHERE user_score and total_shipped IS NOT NULL")
user_info = cursor.fetchall()


def rating_sales(game_info,rating_threshold=0.75,sales_threshold=0.75):
    
    df = pd.DataFrame(game_info, columns=['Game', 'Rating', 'Sales'])
    # 计算评分与总销售量的皮尔逊相关系数
    correlation = df['Rating'].corr(df['Sales'])
    # 打印相关系数
    print(f"The correlation coefficient between Rating and Sales is: {correlation}")

    # 定义高评分和高销量的阈值
    high_rating_threshold = df['Rating'].quantile(rating_threshold)  # 评分最高的25%
    high_sales_threshold = df['Sales'].quantile(sales_threshold)   # 销量最高的25%

    # 识别高评分高销量的游戏
    high_rating_high_sales = df[(df['Rating'] >= high_rating_threshold) & (df['Sales'] >= high_sales_threshold)]

    # 识别低评分高销量的游戏
    low_rating_high_sales = df[(df['Rating'] < high_rating_threshold) & (df['Sales'] >= high_sales_threshold)]

    # 计算各类游戏的数量
    high_rating_high_sales_count = high_rating_high_sales.shape[0]
    low_rating_high_sales_count = low_rating_high_sales.shape[0]

    # 将游戏名保存到列表中
    high_rating_high_sales_games = high_rating_high_sales['Game'].tolist()
    low_rating_high_sales_games = low_rating_high_sales['Game'].tolist()

    # 输出结果
    print(f"高评分高销量的游戏数量: {high_rating_high_sales_count}")
    print(f"低评分高销量的游戏数量: {low_rating_high_sales_count}")

    # 打印游戏名列表
    print("高评分高销量的游戏名:", high_rating_high_sales_games)
    print("低评分高销量的游戏名:", low_rating_high_sales_games)

    return high_rating_high_sales_games,low_rating_high_sales_games

vgchartz_high,vgchartz_low = rating_sales(vgchartz_info)
critic_high,critic_low = rating_sales(critic_info)
user_high,user_low = rating_sales(user_info)

set1 = set(vgchartz_high)
set2 = set(critic_high)
set3 = set(user_high)

# 找出set1和set2的交集
intersection12 = set1 & set2
print(f"交集{intersection12}")
# 找出intersection12和set3的交集
common_elements = intersection12 & set3

# 输出共同元素
print(common_elements)