word1 = str(input("첫번째 단어 :"))
word2 = str(input("두번째 단어 :"))
word3 = str(input("세번째 단어 :"))
print("="*25)

abbr = word1[0] + word2[0] + word3[0]
print("약자 :", format(abbr, 's'))