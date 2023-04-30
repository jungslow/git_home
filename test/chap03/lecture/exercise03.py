# for 반복문을 이용한 '수열 출력하기'
series = []
sum = 0

print('수열 =', end = ' ')
for i in range(1, 101) :
    if i%3 == 0 and i%2 != 0 :
        print(i, end = ' ')
        series.append(i)
        sum += i

print('\n누적합 = %d' %sum)