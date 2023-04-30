freight_weight = int(input("짐의 무게는 얼마입니까? "))
fee = 0

if freight_weight < 10 :
    print("수수료는 없습니다.")
else :
    fee = freight_weight//10*10000
    print("수수료는", format(fee, "3,d"), "원입니다.")

