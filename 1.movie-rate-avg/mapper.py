import sys

for line in sys.stdin:
    line = line.strip()
    
    fields = line.split(',')
    # ['1', '296', '5.0', '1132456432']의 리스트로 userid, movieId, rating, timestamp가 저장됨
    
    movie_id = fields[1]
    rating = fields[2]
    #내가 필요한 데이터를 분리
    
    print(f'{movie_id}\t{rating}')
    #tab으로 구분하여 movie_id와 rating을 출력함