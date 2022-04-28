# 튜플을 만들어보고 그 타입을 출력하기
my_variable = ()
print(type(my_variable))

# 2016년 11월 영화 예매 순위 기준 top3 는 다음과 같다. 영화 제목을 movie-rank 이름의 튜플에 저장하라. (순위정보는 저장하지 않는다)
#   순위        영화
#   1           닥터 스트레인지
#   2           스플릿
#   3           럭키

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 숫자 1이 저장된 튜플을 생성하라.
my_tuple = (1)
print (type(my_tuple))      # int
# 비록 1개의 데이터가 저장되더라도 튜플의 형식을 가지려면 쉼표(,)가 있어야합니다.

my_tuple = (1,)
print(type(my_tuple))

# tuple은 원소(element)의 값을 변경할 수 없습니다.
# 생성시 가지고있던 원소들로 고유함. => 배열과 가장 다른 차이점이 된다.


"""
t = (1,2,3)
t[0] = 'a'
print(t)
'tuple' object does not support item assignment
"""
###

# 쉼표가 있다면 튜플은 괄호 없이도 정의가 가능합니다.
t = 1,2,3,4
print(t)
print(type(t))

# 그렇다면 튜플 변수의 요소를 바꿀 방법은 없는것인가?
# 튜플의 원소를 변경하려면 새로운 튜플형태로 밖에 선언이 안됨.
t = ('a', 'b' ,'c')
t = ('A','b','c')
print(t)

# 다음 튜플을 리스트(Array)로 변환하기
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

# 아래와 같이 변수를 선언하면
# a에는 apple이 , b에는 banana가, c에는 cake가 string변수로 바인딩 됩니다.
temp = 'apple', 'banana', 'cake'
a,b,c = temp
print(a,b,c)


# 등차수열 함수를 tuple에 넣어서 변수를 선언할 수 있다.
t = tuple(range(2,100,2))
print(t)





