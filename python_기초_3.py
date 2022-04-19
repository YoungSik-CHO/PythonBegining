#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자 출력
#문자열을 변수에 바인딩하면 변수는 문자열 각 하나하나마다 배열로도 갖고 있는다.
# 파이썬의 인덱싱은 0부터 시작한다.
letters = 'python'
print(letters[0], letters[2])

#자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하기
# [N:] 으로 작성하면 해당 인덱스 부터 라는 의미임
# N을 음수로 두면 뒤에서 부터 인덱스를 찾는다.
licence_plate = "24가 2210"
print(licence_plate[4:])
print(licence_plate[-4:])

# 문자열 슬라이싱은 시작인덱스 : 끝인덱스 : 오프셋 구조를 가진다.
# string[1:10:2] => 인덱스1부터 인덱스10까지 2자리씩 가져옴
# 그리고 슬라이싱 할때 0은 생략가능
string = "홀짝홀짝홀짝"
print(string[::2])  #홀홀홀
print(string[2::2]) 
print(string[2::2])

#문자열 거꾸로 뒤집어 출력하기
# 오프셋 자리에 -1을 두면 뒤에서 부터 출력함
# 오프셋 자리에 -2을 두면 뒤에서 부터 두자리마다 하나씩 출력함
string = "PYTHON"
print(string[::-1])
print(string[::-2])

#문자열 치환하기
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-"," ")
# phone_number = phone_number.replace("-","")
print(phone_number)

# Url에 저장된 웹 페이지 주소에서 도메인 출력하기
url = "http://sharebook.kr"
# => 1. 문자열 잘라서 출력
# print(url[-2::])
# => 2. 문자열을 분리해서 배열에 넣고 출력
url_split = url.split('.')  
# url[0] => "http://sharebook"
# url[1] => "kr"
print(url_split[1])

'''
lang = 'python'
lang[0] = 'P'
print(lang)

=> 문자열은 수정 할 수 없습니다. 실행결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있음.
=> 'str' object does not support item assignment
'''

string = 'abcdefe2a354a32a'
print(string.replace('a', 'A'))

# replace 해도 선언한 변수에 넣지 않으면 값은 변하지 않음
string = 'abcd'
string.replace('b','B')
print(string)




