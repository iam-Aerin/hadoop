# hadoop 없이 linux 컴퓨터로 실행하는 방법법

#!/usr/bin/env python3


import sys

for line in sys.stdin:
    line = line.strip() #양 옆 공백 제거
    words = line.split() #공백 기준으로 단어 나누기
    # words 에는 리스트 형태로 단어들이 저장되게됨
    for word in words:
        print(f'{word}\t1')
        
# cat text.txt | python3 mapper.py 
#왼쪽의 파일을 오른쪽에 넣어주세요
