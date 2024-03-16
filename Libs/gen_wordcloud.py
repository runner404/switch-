from collections import defaultdict
from PIL import Image
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt

def generate_word_cloud(table_list, background_image_path="background.jpg"):
    """
    生成并展示一个词云
    参数:
    table_list -- 包含游戏名称和评分的元组列表。
    background_image_path -- 背景图片的路径，默认为 "background.jpg"。
    """
    # 计算总分
    total_score = sum(game_info[1] for game_info in table_list)
    # 每个游戏评分占比字典
    score_counts = {game_name: critic_score/total_score for game_name,critic_score in table_list}

    # 设置背景图形状
    img = Image.open(background_image_path)
    img_array = np.array(img)

    # 创建词云对象
    wordcloud = WordCloud(font_path='STHUPO.TTF',
                        background_color='white',
                        width=800, height=600,
                        random_state=629,
                        max_font_size=50,
                        mask=img_array).generate_from_frequencies(score_counts)

    # 使用matplotlib展示词云图
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # 关闭坐标轴
    plt.show()

# 示例使用
# table_list = [("游戏A", 90), ("游戏B", 85), ("游戏C", 95)]
# generate_word_cloud(table_list)