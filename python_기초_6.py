"""
2016년 11월 영화 예매 순위 기준 top 3가 아래과 같음
영화 제목을 movie_rank 이름의 리스트에 저장해보세요

순위            영화
1               닥터 스트레인지
2               스플릿
3               럭키


"""
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]


# movie_rank 데이터에 "배트맨"을 추가하기
movie_rank.append("배트맨")

print(movie_rank)

# "슈퍼맨" 을 "닥터 스트레인지" 와 "스플릿" 사이에 추가하기

# movie_rank 리스트에 "1"번 순서에 "슈퍼맨" 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)



#movie_rank에서 "럭키" 를 삭제하기

# 명칭을 알고있을때
#movie_rank.remove("럭키")

# index로 지우고 싶을때
del movie_rank[3]
print(movie_rank)


"""
del을 이용하여 리스트에서 원소를 삭제할 수 있음.
리스트에서 어떤 값을 삭제하면 남은 값들로 새로 인덱싱됨.
여러값을 지울때는 어떤값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 고민하길. ..
"""
