fat = int(input('지방의 그램을 입력하세요 :'))
carbohydrate = int(input('탄수화물의 그램을 입력하세요 :'))
protein = int(input('단백질의 그램을 입력하세요 :'))

tot_cal = fat*9 + protein*4 + carbohydrate*4
print('총칼로리 : ', format(tot_cal, ',d'), 'cal')