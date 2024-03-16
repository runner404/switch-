import httpx
from bs4 import BeautifulSoup
import sqlite3

# 自定义的请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}

def process_page_data(url, cursor, table_name):
    """
    处理单个页面的数据提取和数据库插入操作。
    参数:
    url (str): 当前页面的完整URL。
    cursor (sqlite3.Cursor): SQLite数据库游标对象。
    table_name：数据库表格名
    """
    # 发送GET请求
    content = httpx.get(url=url, headers=headers, timeout=10, verify=False)
    # 解析HTML
    soup = BeautifulSoup(content, 'html.parser')
   # 查找所有具有特定样式的 <tr> 标签
    tr_large_tags = soup.find_all('tr', style='background-image:url(../imgs/chartBar_large.gif); height:70px')
    tr_alt_large_tags = soup.find_all('tr', style="background-image:url(../imgs/chartBar_alt_large.gif); height:70px")
    #提取出含有游戏数据的网页内容
    block_items = tr_large_tags + tr_alt_large_tags

    # 遍历每个blockItem元素，提取游戏名称和评分
    for item in block_items:
        #找到指定元素
        brother = item.find('td', width="100")
        brother1 = brother.next_sibling.next_sibling   
        brother2 = brother1.next_sibling.next_sibling
        brother3 = brother2.next_sibling.next_sibling
        brother4 = brother3.next_sibling.next_sibling
        brother5 = brother4.next_sibling.next_sibling
        brother6 = brother5.next_sibling.next_sibling
        game_info = {
                    'Game': item.find('a', style="color:#e60012").text.strip(),
                    #<img src="/images/consoles/NS_b.png" alt="NS">
                    'Console': item.find('img', src='/images/consoles/NS_b.png').get('alt'),
                    # <td width="100">Nintendo</td>
                    # <td align="center">N/A</td>
                    # <td align="center">9.3</td>
                    # <td align="center">N/A</td>
                    # <td align="center">60.58m</td>
                    # <td align="center" width="75">28th Apr 17</td>
                    # <td align="center" width="75">19th Nov 18</td
                    'Publisher': brother.text.strip(),
                    'VGChartz Score': brother1.text.strip(),
                    'Critic Score': brother2.text.strip(),
                    'User Score': brother3.text.strip(),
                    'Total Shipped': brother4.text.strip(),
                    'Release Date': brother5.text.strip(),
                    'Last Update': brother6.text.strip()
                }
        # 替换 "N/A" 为 None，替换m为数字
        for key in game_info:
            if game_info[key] == 'N/A':
                game_info[key] = None
            elif game_info[key][-1] == 'm' and key == 'Total Shipped':     #血泪教训，此处只能用elif不能用if
                game_info[key] = float(game_info[key].rstrip('m')) * 1000000

        # 插入数据的SQL语句
        insert_query = f"INSERT INTO {table_name} (game_name, console, publisher, vgchartz_score, critic_score, user_score, total_shipped, release_date, last_update) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # 执行SQL语句
        cursor.execute(insert_query, (
            game_info['Game'],
            game_info['Console'],
            game_info['Publisher'],
            game_info['VGChartz Score'],
            game_info['Critic Score'],
            game_info['User Score'],
            game_info['Total Shipped'],
            game_info['Release Date'],
            game_info['Last Update']
        ))


# 输入数据库文件名称
db_file = input("请输入数据库文件的名称（包括扩展名.db，例如 'games.db'）: ")
print(f"输入的数据库文件名称为: {db_file}")

# 打开数据库连接
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 输入表文件名称
table_name = input("请输入表的名称: ")
print(f"输入的表名称为: {table_name}")
try:
    cursor.execute(f"SELECT * FROM {table_name}")
    table = cursor.fetchone()
    should_delete = input(f"表 '{table_name}' 已存在。是否删除并重建？(y/n): ").lower()
    if should_delete == 'y':
        cursor.execute(f"DROP TABLE {table_name}")
        cursor.execute(f"SELECT * FROM {table_name}")
    else:
        print("操作已取消，将在原表基础上添加数据")
except sqlite3.OperationalError as e:
    print(f"开始创建新表“{table_name}”")
    # 创建新表的SQL语句
    create_table_sql = f'''
        CREATE TABLE {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_name TEXT,
        console TEXT,
        publisher TEXT,
        vgchartz_score REAL,
        critic_score REAL,
        user_score REAL,
        total_shipped REAL,
        release_date TEXT,
        last_update TEXT
        );
    '''
    # 执行SQL语句创建表
    cursor.execute(create_table_sql)
    print(f"新表 '{table_name}' 已成功创建。")



# 基础URL和页码范围
base_url = 'https://www.vgchartz.com/games/games.php'
end_url='&console=NS&order=Sales&ownership=Both&direction=DESC&showpublisher=1&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1'
page_range = range(1, 49)  # 获取第1页到第49页的数据
# 循环遍历页码范围，调用函数处理每个页面
for page_number in page_range:
    # 动态生成完整的URL
    url = f"{base_url}?page={page_number}{end_url}"
    # 调用提取数据的函数
    process_page_data(url, cursor,table_name)
    
    print(f"第{page_number}页网页已录入数据库")
    
# 提交更改
conn.commit()
# 查询数据库并打印结果
cursor.execute(f"SELECT * FROM {table_name}")
game_info_list = cursor.fetchall()
# 遍历查询结果并打印每个游戏的信息
# for game_info in game_info_list:
#     print(f"Game: {game_info[1]}, Console: {game_info[2]}, Publisher: {game_info[3]}, VGChartz Score: {game_info[4]}, Critic Score: {game_info[5]}, User Score: {game_info[6]}, Total Shipped: {game_info[7]}, Release Date: {game_info[8]}, Last Update: {game_info[9]}")

# 关闭游标和连接
cursor.close()
conn.close()
print("已完成")
