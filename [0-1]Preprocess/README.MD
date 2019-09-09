# Preprocess

日本語のWordCut.  
  
* 形態素解析  
  
  
[LINK: 【技術解説】形態素解析とは？MeCabインストール手順からPythonでの実行例まで](https://mieruca-ai.com/ai/morphological_analysis_mecab/)  
[LINK: MeCab: Yet Another Part-of-Speech and Morphological Analyzer](https://taku910.github.io/mecab/)  
[LINK: MeCab-Pythonで分かち書きと形態素解析](http://testpy.hatenablog.com/entry/2016/10/04/010000)
  
  
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
import re

def wakati(input_str):
        '''分かち書き用関数
        引数 input_str : 入力テキスト
        返値 m.parse(wakatext) : 分かち済みテキスト'''
        wakatext = input_str
        m = MeCab.Tagger('-Owakati')
        #print(m.parse(wakatext))
        return m.parse(wakatext)


with open("sequence.txt") as seqtex, open("./input.txt",'w') as infile,\
 open("./output.txt",'w') as outfile:
    print("data writing...")
    for line in seqtex:
        if line.find("input:") != -1:   #input文の処理
            line = re.sub('input: ', '', line)
            wakati_in = wakati(line)
            infile.write(wakati_in)

        else:  #output文の処理
            line = re.sub('output: ', '', line)
            wakati_out = wakati(line)
            outfile.write(wakati_out)

print("finished.")
```
  
> from https://qiita.com/Pu-of-Parari/items/62d7226814a6aba98354#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%BA%96%E5%82%99  