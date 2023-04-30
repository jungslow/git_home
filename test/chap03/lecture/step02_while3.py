# (1) random모듈 관련 함수
import random
help(random.randint)
help(random.choices)

# (2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동', '유관순', '이순신']
print(names)
print(names[1])

# (3) list에서 자료 유무 확인
if '장보고' in names:
    print('장보고 있음')
else :
    print('장보고 없음')

# (4) 난수 정수로 이름 선택하기
idx = random.randint(0,2)
print(idx, names[idx])


