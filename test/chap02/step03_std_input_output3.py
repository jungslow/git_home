# (4) format() 함수 인수 : format(value, "format")
print("원주율=", format(3.14159, "8.3f"))
print("금액 =", format(10000, "10d"))
print("금액", format(125000, "3,d"))

# (5) 양식문자 인수 : print("%양식문자", %(값))
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, 가격 = %.2f" %(name, age, price))

# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, 가격 = {}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, 가격 = {2}".format(age, name, price))

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query)
