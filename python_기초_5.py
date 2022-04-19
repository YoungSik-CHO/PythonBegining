# 문자열 대문자변경
ticker = "btc_krw"
print(ticker.upper())

#문자열 소문자변경
ticker = "BTC_KRW"
print(ticker.lower())

#capitalize 메서드 => 첫문자 대문자로 변경 나머지 소문자로 변경
string = "hello"
print(string.capitalize())

#endswith(str) => 해당 문자열이 str로 끝나는지 여부를 boolean으로 리턴
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
print(file_name.endswith("xls"))
# endswith 메서드에서 여러문자열을 OR 연산자로 검사하고 싶으면 튜플(1,2,3...)로 파라미터를 넣으면됨
# file_name 변수에 xlsx 또는 xls 문자로 끝나는지 여부를 boolean 으로 리턴
print(file_name.endswith(("xlsx", "xls")))



#startswith(str) 메서드 => 해당 문자열이 str로 시작하는지 여부를 boolean으로 리턴
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith('xlsx'))

#공백을 기준으로 문자열 split
# 문자열을 split으로 나누면 배열로 리턴
a = "hello world"
print(a.split(' '))
# split메서드에 아무것도 안넣으면 자동 분리자를 공백으로 보고 나눔
print(a.split())

ticker = "btc_krw"
print(ticker.split('_'))


#년월일 데이터가 있을떄 문자열을 년도, 월, 일로 나누세용
date = "2020-05-01"
print(date.split('-'))

#오른쪽의 공백만 제거
date = "039490    "
print(date.rstrip())

#왼쪽의 공백만 제거
daste = "      039490"
print(date)
print(date.lstrip())


