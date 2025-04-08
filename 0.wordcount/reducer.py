# cat text.txt | python3 mapper.py | sort 정렬해서 같은 단어들끼리를 모아줌
# cat text.txt | python3 mapper.py | sort | python3 reducer.py 정렬후 reducer.py 실행해 count 하기

#!/usr/bin/env python3

import sys

# apple 1
# apple 1
# hello 1
# hello 1
# 이런식으로 같은 단어끼리 줄세우기 (정렬)

# 필요한 변수 선언
last_word = None # 글자가 바뀌는 시점을 찾기 위한 변수
total_count = 0

for line in sys.stdin:
    word, value = line.split('\t') # tab 기준으로 나누기
    value = int(value)
    
    if last_word == word: # 글자가 바뀌지 않았다면
        total_count += value
    else: 
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word
        total_count = value # 글자가 바뀌었다면 total_count를 value로 초기화 (새로운 숫자 1부터 다시 시작하겠다.)
if last_word == word:
    print(f'{last_word}\t{total_count}') # 마지막 단어 출력