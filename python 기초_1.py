# Python 기본 출력함수 (Java : System.Out.PrintLn());
#                     (JavaScript : Console.log());
print('Hello World');
# 문자열은 따옴표 상관없이 사용 가능
print("Hello World");

#Print() 쓰면 안됨
# Python은 코드에 대소문자를 구분하는 언어다.
print("Mary's cosmetics");

# print 출력 구문에 따옴표가 있다면 그거랑 다른 따옴표를 사용해주면 출력이 가능하다.
print("신씨가 소리질렀다. '도둑이야'");
print("C:/Windows");


#\n 과 \t를 print 문자열 안에 넣으면 탭과 줄바꿈으로 자동 인식한다.
print("안녕하세요. \n만나서 \t \t 반갑습니다.");


# print 함수 내에 문자열을 여러개 넣어도 하나의 문장으로 인식한다.
print("오늘은", "일요일");

print("naver;kakao;sk;samsung");
print("naver/kakao/sk/samsung");

# end="" 를 두번째 매개변수로 넣으면 다음 print 구문도 줄바꿈 없이, 마치 한문장으로 인식하여 출력한다.
# => end 파라미터의 기본값은 \n 이다.
print("first", end="  ");print("second");

#print 함수는 연산도 가능하다. 연산된 결과값을 print 한다.
print(5/3)