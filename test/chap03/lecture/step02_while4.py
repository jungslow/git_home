i = 0
while i < 16 :
    i += 1
    if i%3 == 0 :
        continue
    if i == 17 :
        break
    print(i, end=' ')

# (1) 문자열 열거형객체 이용
string = "홍길동"
print("\n문자 길이 = ",len(string))
for s in string :
    print(s)

# (2) list 열거형객체 이용
listset = [1, 2, 3, 4, 5]
for e in listset :
    print('원소 :', e)

