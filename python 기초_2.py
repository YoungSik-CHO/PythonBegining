# 변수에 값 담고 연산하여 출력하기
삼성전자 = 50000;
주식 = 10;
print(삼성전자 * 주식);

'''
    항목        값
    시가총액    298조
    현재가      50,000원
    PER         15.79
'''
# 변수에 값 담기
시가총액 = 2980000000000;
현재가 = 50000;
PER = 15.79
print(시가총액);print(현재가);print(PER);

#변수를 이용한 문자열 출력 (결과값 = hello! python)
s = "hello"
t = "python"
print(s + '!' , t );


# 2 + 2 * 3 출력하기
print(2+2*3)


# type 출력하기
a = 128
print(type(a))
# => a에는 정수가 바인딩 되어 있어 <class 'int'>  형태로 출력함.
a = "132"
print(type(a))
# => a에 따옴표가 들어간 값을 바인딩히어 <class 'str'> 형태로 출력함.



# 문자열을 정수로 변환 => 문자값 720을 정수로 변환하여 +1 시키고 그 타입을 출력하기
num_str = "720"
num_int = int(num_str);

print(num_int + 1 , type(num_int))

# 정수를 문자열로 변환
num = 100
print(str(num), type(str(num)))



# 문자열을 실수로 변환
flo = "15.79"
print(float(flo), type(float(flo)))

# 문자열을 정수로 변환 한 후 산식
year = '2020'
print(int(year))
print(int(year) - 1)
print(int(year) - 2)


# 에어컨이 월 48584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있음.
# 총 금액을 계산한 후 이를 화면에 출력하자
airconditioner = 48584
month = 36
print(airconditioner * month)

