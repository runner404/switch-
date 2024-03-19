from googletrans import Translator
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import sqlite3

def trans_element(element):
    try:
        translator = Translator()
        translation = translator.translate(element,dest='zh-cn')
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return element  # 返回原始行或适当的错误标记


def main():
    global table
    global tr_col
    global tot_col
    global translated_table
    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=1) as executor:
            # 使用列表推导式并行翻译指定列
            futures = [executor.submit(trans_element, element) for element in (table[i][tr_col - 1] for i in range(len(table)) if table[i][tr_col - 1] is not None)]
            translated_elements = [future.result() for future in tqdm(futures, desc='Translating', total=len(futures))]
            
            #构建翻译后的表格
            translated_table = []
            for i, row in enumerate(table):
                # 创建原始行的副本并转换为列表
                new_row = list(row)
                # 如果该行的指定列存在，则替换为翻译后的元素，否则保持原始元素
                if table[i][tr_col - 1] is not None:
                    new_row[tr_col - 1] = translated_elements[i]
                # 将修改后的列表转换为元组并添加到翻译后的表格中
                translated_table.append(tuple(new_row))
        print("翻译已完成")
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS game_release(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,release_date TEXT NOT NULL)")
        for tuple_data in translated_table:
            print(tuple_data)
            cursor.execute('INSERT INTO game_release (name, release_date) VALUES (?, ?)', tuple_data)
        print("数据已导入")

db_file = 'games.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("SELECT game_name,release_date FROM vgc_info WHERE release_date IS NOT NULL LIMIT 10")
table = cursor.fetchall()
tr_col = 1
translated_table=[]
tot_col = 2

if __name__ == "__main__":
    main()