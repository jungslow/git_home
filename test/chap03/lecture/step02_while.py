# 카운터와 누적변수
cnt = tot = 0
while cnt < 5 :
    cnt += 1
    tot += cnt
    print(cnt, tot)

# (2) [실습] 1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = tot = mnum = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt%3 == 0:
        mnum += 1
        tot += cnt
        dataset.append(cnt)

print('1 ~ 100 사이 3의 배수의 갯수 = %d' %mnum)
print('1 ~ 100 사이 3의 배수의 합 = %d' %tot)
print('dataset = ', dataset)

# 무한 루프(loop)
numData = []

while True :
    num = int(input('숫자 입력 : '))

    if num%10 == 0 :
        print('프로그램 종료')
        break
    else :
        print(num)
        numData.append(num)

print('numData = ', numData)


