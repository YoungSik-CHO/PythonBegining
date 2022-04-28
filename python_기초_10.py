"""
아래의 표에서, 아이스크림 이름의 키값으로, (가격, 재고) 리스트를 딕셔너리의 값을 저장하라. 
딕셔너리의 이름은 inventory로 한다.

    이름    가격    재고
    메로나  300     20
    비비빅  400     3   
    죠스바  250     100

"""

inventory = { "메로나" : [300,20],
              "비비빅" : [400,3],
              "죠스바" : [250 , 100]}

print(inventory)

# inventory 변수에서 "메로나"의 "가격" 을 출력하라
print(inventory["메로나"][0])

# inventiry 변수에서 "메로나"의 "재고"를 출력하라
print(inventory["메로나"][1])

# inventory 딕셔너리에 아래 데이터를 추가하라
"""
    이름    가격    재고
    월드콘  500     7
"""
inventory["월드콘"] = [500,7]
print(inventory)

# 다음 딕셔너리로 부터 key 값만 구성된 리스트를 출력하라
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())  #dict_keys(['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나'])
print(list(icecream.keys()))  #['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']


# icecream 딕셔너리로 부터 value 값만 구성된 리스트를 출력하라
print(icecream.values())        #   dict_values([1200, 1200, 1800, 1500, 1000])
print(list(icecream.values()))  #   [1200, 1200, 1800, 1500, 1000]

# icecream 딕셔너리에 new_product 딕셔너리를 추가하라
new_product = {'팥빙수' : 2700, '아맛나' : 1000}
icecream.update(new_product)        # 딕셔너리 + 딕셔너리 한다.
print(icecream)


# 아래 두개의 튜플을 하나의 딕셔너리로 변환하라. keys는 키로, vals는 값으로 result 이름의 딕셔너리로 저장한다
keys = ("apple", "pear", "peach")
vals = 300, 250, 400
result = dict(zip(keys, vals))
print(result)

"""

 !중요 keys의 갯수와 vals의 갯수가 다를때
 zip 메소드는 key와 val을 1개씩 엮는 작업을 계속하며 
 둘 중 하나의 값이라도 다 엮게 되는 순간 남아있는 값은 신경쓰지 않은채 result변수가 만들어진다.
 ex) keys의 값이 4개, vals값이 6개라면
     result 변수는 key : val 이 4개의 쌍이 만들어진다.
"""


# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)




