# coding:UTF-8
import glob
import os
import MeCab
import random
import neologdn
import re
import emoji

import argparse


DATA_PATH = r'../train_data'
TRAIN_FILE = './train.txt'
TEST_FILE = './test.txt'
STOPWORDS = './JPN_stopwords.txt'

'''
10分の8の確率でテスト用ファイルにデータを書き込む
'''
def keitaiso(text):
    with open(STOPWORDS) as f:
        stopwords = f.read()
    m = MeCab.Tagger('-Owakati')
    #全角・半角の統一と重ね表現の除去
    text = neologdn.normalize(text)
    #URLを除去
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
    # 数字の置換
    text = re.sub(r'[0-9]', r' ', text)
    #記号の置き換え
    # 半角記号の置換
    text = re.sub(r'[!-/:-@[-`{-~]', r' ', text)
    # 全角記号の置換 (ここでは0x25A0 - 0x266Fのブロックのみを除去)
    text = re.sub(u'[■-♯]', ' ', text)
    #桁区切りの除去と数字の置換
    text = re.sub(r'(\d)([,.])(\d+)', r'\1\3', text)
    test = re.sub(r'\d+', '0', text)
    #絵文字を除去
    text = ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in text])
    text = text.replace("\r\n", "")
    text = text.replace("\n", "")
    text = text.replace("…","")
    text = text.replace("・","")
    text = text.replace("\u3000", "")
    #mecabで単語区切りにする
    text = m.parse(text)
    #stop words 
    newlist  = [word for word in text.split() if word not in stopwords ]
    text = " ".join(newlist)+"\n"
    return text

def fasttext_file(record):
    r = random.randint(1, 10)
    filename = TRAIN_FILE
    
    # if r > 8:
    #     filename = TEST_FILE
    
    with open(filename, 'a') as f:
        f.write(record)

# 名詞の抽出
def nouns_extract(text):
    tagger = MeCab.Tagger("-Ochasen")
    nouns = [line.split()[0] for line in tagger.parse(text).splitlines() if "名詞" in line.split()[-1]]
    return nouns

if __name__ == '__main__':
    
    # processing with argumentParser
    ap = argparse.ArgumentParser()
    # extract the nouns from dataset 
    ap.add_argument("-onlynoun",help="extract noun from dataset." ,action="store_true")
    args = ap.parse_args()

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    if os.path.exists(TRAIN_FILE):
        os.remove(TRAIN_FILE)

    
    # ../dataの下ディレクトリ一覧を取得する
    dir_list = glob.glob(os.path.join(DATA_PATH, "*"))

    for category_number, dir_name in enumerate(dir_list):
        # カテゴリ名にディレクトリの名前を使う
        category_name = dir_name.split("/")[-1]
        print("category:{}".format(category_name))
        
        #テキストファイル一覧取得
        file_list = glob.glob(os.path.join(dir_name,"*.txt"))
        for file_name in file_list:
            with open(file_name, "r", encoding="utf-8") as f:
                try:
                    text = f.read()
                    #形態素解析
                    text = keitaiso(text) 
                    #名詞の抽出
                    if args.onlynoun :
                        #名詞の抽出
                        text = " ".join( nouns_extract(text) ) +"\n" 
                    # fasttextが求める書式に直す
                    record = '__label__{} , {}'.format(category_name, text)
                    fasttext_file(record)

                except:
                    # 文字コード変換でエラーになったファイルは無視する
                    #print(text)
                    print("file name:{} error".format(file_name))
