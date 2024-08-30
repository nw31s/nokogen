import random
import schedule
import os
import time

import Levenshtein
from difflib import SequenceMatcher

# 初期設定

def generate_text(CC):
    current_char = CC
    text = current_char
    while current_char != ' ':
        if current_char == 'し':
            next_char = random.choice(['か', 'た'])
        elif current_char == 'か':
            next_char = 'の'
        elif current_char == 'の':
            next_char = 'こ'
        elif current_char == 'こ':
            next_char = random.choices(['の', 'こ', 'し'], weights=[2, 1, 1])[0]
        elif current_char == 'た':
            next_char = 'ん'
        elif current_char == 'ん':
            next_char = random.choice([' ', 'た'])
        text += next_char
        current_char = next_char
    return text

def deerchecker(input):
    colorlist = ['0xf64666', '0x714a27', '0x96c022', '0x6d61ca', '0xfbaa09']
    
    length = len(input)

    gestalt = SequenceMatcher(None, 'しかのこのこのここしたんたん', input).ratio()
    levenshtein = Levenshtein.distance('しかのこのこのここしたんたん', input)
    #perf = input.count('しかのこのこのここしたんたん')
    tango_shikanoko = input.count('しかのこ')
    tango_nokonoko = input.count('のこのこ')
    tango_koshitantan = input.count('こしたんたん')
    char_shi = input.count('し')
    char_ka = input.count('か')
    char_no = input.count('の')
    char_ko = input.count('こ')
    char_ta = input.count('た')
    char_nn = input.count('ん')
    return gestalt, levenshtein, length, tango_shikanoko, tango_nokonoko, tango_koshitantan, char_shi, char_ka, char_no, char_ko, char_ta, char_nn

def nokogenPost():
    generatedtext = "しかのこのこのここしたんたん"
    gestalt_ans = deerchecker(generatedtext)[0]

    posttext = f"{generatedtext}\n一致率: {gestalt_ans}"
    print(f"{posttext}")

while True:
    nokogenPost()
    time.sleep(900000)