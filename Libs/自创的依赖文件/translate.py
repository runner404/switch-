from googletrans import Translator,LANGUAGES
from tqdm import tqdm

def translate_dict(dict):
    tranlated_dict = {}
    tranlator = Translator
    for key,value in dict.items():
        #翻译键
        tranlated_key = tranlator.translate(key,dest='zh-cn').text
        if isinstance(value,str):
            #翻译值
            tranlated_value = tranlator.translate(value,dest='zh-cn').text
        else:
            tranlated_value = value
        tranlated_dict[tranlated_key] = tranlated_value
    
    #返回翻译后的字典
    return tranlated_dict

def translated_table(table,col):
    translated_table = []
    # 初始化翻译器
    translator = Translator()
    for table_tuple in tqdm(table, desc='Translating', total=len(table)):
        translated_list = []
        # 执行翻译
        for i in range(0,col):
            if isinstance(table_tuple[i],str):
                text_to_translate = table_tuple[i]
                #translation = translator.translate(text_to_translate,dest = 'zh-cn')
                translation = translator.translate(text_to_translate, dest="zh-cn")
                translated_list.append(translation.text)
            else:
                translated_list.append(table_tuple[i])  
        translated_table.append(tuple(translated_list))
    return translated_table