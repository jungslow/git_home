import random
# (1) range 객체 생성
num1 = range(10)
print('num1 : ', num1)
num2 = range(1,10)
print('num2 : ', num2)
num3 = range(1,10,2)
print('num3 : ', num3)

# (2) range 객체 이용
for n in num1 :
    print(n, end = ' ')
print()
for n in num2 :
    print(n, end = ' ')
print()
for n in num3 :
    print(n, end = ' ')
print()

# (3) list에 자료 저장하기
lst = []
for i in range(10) :
    r = random.randint(1,10)
    lst.append(r)

print('lst =', lst)

# (2) list에 자료 참조하기
for i in range(10) :
    print(lst[i] * 0.25)

