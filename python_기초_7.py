# price 변수에는 날짜와 종가정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1::])

# 1부터 10까지 변수가 차례대로 들어있는 배열이 존재할때, 홀수만 출력하기
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

#짝수만 출력하기
print(nums[1::2])

#리스트의 숫자를 역방향으로 출력하기
print(nums[::-1])

#interest 리스트에는 아래의 데이터가 바인딩 되어 있다.
interest = ['삼성전자', 'LG전자', 'naver']
print(interest[0], interest[2])

interest = ['삼성전자', 'LG전자', 'naver', 'SK하이닉스', '미래에셋대우']
# interest의 모든 요소를 순서대로 출력하기
print(' '.join(interest))

# 모든요소를 사이에 / 를 두고 출력하기
print('/'.join(interest))

# 모든요소를 줄바꿈하여 출력하기
print('\n'.join(interest))

# 회사이름이 슬래시("/")로 구분되어 하나의 문자열로 구성되어 있을때, 리스트로 분리 바인딩하기
string = "삼성전자/LG전자/Naver"
print(string.split('/'))

# 리스트정렬
data = [2, 4, 3, 1, 5, 10, 9]

# 오름차순으로 정렬
# 1.
data.sort()
print(data)

# 2.
data2 = sorted(data)
print(data2)

