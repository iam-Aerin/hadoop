import sys

# 정규표현식
import re

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')
# 어떤 숫자이던지 2자리인 글자 패턴을 찾아라 \d = [0-9]

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    match = time_pattern.search(line)
    
    if match:
        hour = match.group(1)
        print(f'{hour}\t1')