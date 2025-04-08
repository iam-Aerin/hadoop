import sys

current_movie_id = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    # mapper.py에서 출력한 데이터를 받아옴
    line.split('\t')
    # tab으로 구분된 데이터를 분리
    movie_id, rating = line.split()
    # movie_id와 rating을 분리
    
    try: 
        rating = float(rating)
    except:
        #첫줄이 숫자가 아니라, 지금 movieId는 각 숫자의 순서가 어떤 것을 알려주는 컬럼 설명글이 첫줄에 들어가있으므로
        # 그걸 무시해주라는 명령
        continue
    
    if current_movie_id == movie_id:
        current_count += 1
        current_sum += rating
    else:
        if current_movie_id is not None:
            current_avg = current_sum / current_count
            print(f'{current_movie_id}\t{current_avg}')
    
        # 새로운 movie_id를 만났으므로 초기화
        current_movie_id = movie_id
        # movie_id가 바뀌었으므로 초기화
        current_count = 1
        current_sum = rating
    # rating을 float로 변환
    # rating이 숫자가 아니라면 무시 
    
    #숫자가 변하는 순서 (movieId가 바뀌는 지점 까지의 숫자를 더해서 평균을 구해라)
current_avg = current_sum / current_count
print(f'{current_movie_id}\t{current_avg}')
# 마지막 movie_id에 대한 평균을 출력
# 