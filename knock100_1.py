# coding: utf-8
# Alt+R
# Python3系であれば、ファイル→起動スクリプトでinit.coffeeファイルを開き
# process.env.PYTHONIOENCODING = "utf-8";

#00
str0 = 'stressed'  # ""はダメ
print(str0[::-1])  # list[start:end:step] stepがマイナスなら逆順

#01
str1 = 'パタトクカシー'
print(str1[::2])

#02
str2_1 = 'パトカー'
str2_2 = 'タクシー'
for a,b in zip(str2_1,str2_2):
    print(a+b, end='')
print()

#03
import re
str3 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str3 = re.sub('[,\.]', '', str3)  # ,と.を除去
str3_list = str3.split()  # スペースで区切って単語ごとのリストを作成
for i in str3_list:
    print(len(i),end='')
print()

#04
str4 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
split4 = str4.split()
one_ch4 = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 1文字を取り出す単語の番号リスト
ans4 = {}
for i,word in enumerate(split4):
    if i+1 in one_ch4:
        ans4[word[:1]] = i + 1
    else:
        ans4[word[:2]] = i + 1
print(ans4)

#05
# n-gram 文字列を頭から順にn個の文字で分割. 単語bi-gram，文字bi-gram
str5 = 'I am an NLPer'
split5 = str5.split()
def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1) ]

word_bi_gram = len(split5)-1
for i in range(word_bi_gram):
    print(split5[i:i+2], end='')
print()
str5 = re.sub('[ ]', '', str5)
print(n_gram(str5,2))
print()

#06
str6_1 = 'paraparaparadise'
str6_2 = 'paragraph'
X = set(n_gram(str6_1,2) )
Y = set(n_gram(str6_2,2) )
union = X | Y  # 集合の引数はset(集合)のみ。{}で表す。
intersection = X & Y
difference = X - Y

print('X:', X)
print('Y:', Y)
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)
print('Xにseが含まれるか:', {('se')} <= X)
print('Yにseが含まれるか:', {('se')} <= Y)

#07
def q7(x,y,z):
    # return str(x)+'時の'+y+'は'+str(z)
    return f'{x}時のとき{y}は{z}'  # formatで書式変換
    # return '{}時のとき{}は{}'.format(x,y,z)
print( q7(12,'気温',22.4) )

#08
# chr(文字化)　⇔  ord(コード化)
def cipher(str):
    ret = [chr(219 - ord(x)) if x.islower() else x for x in str]
    return ''.join(ret)
message = 'the quick brown fox jumps over the lazy dog'
print( cipher(message) )
print( cipher( cipher(message) ) )

#09
import random
def shuffle(words):
    split9 = words.split()
    if len(split9) > 4:
        return split9[:1] + random.sample(split9[1:-1], len(split9)-2) + split9[-1:]
words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
print( shuffle(words) )
