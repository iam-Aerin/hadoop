import sys

last_hour = None
total_count = 0

# mapper에서 나눠놓은 데이터
# 03 1
# 03 1
# 03 1
# 04 1
# 04 1
# 를 받아서 코드를 실행
for line in sys.stdin:
    line = line.strip()
    
    hour, value = line.split()
    value = int(value)
    
    if last_hour == hour:
        total_count += value
    else:
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')
        last_hour = hour
        total_count = value
        # hour과 value를 분리
        # value는 int로 변환
        # hour이 같으면 count를 더하고, 다르면 count를 출력
        # hour을 바꾸고 count를 초기화
# 마지막 hour에 대한 count를 출력       
print(f'{last_hour}\t{total_count}') #마지막 hour에 대한 count를 출력 (비교 대상이 없으므로 따로 빼서 마지막 데이터를 출력해줘야함)
