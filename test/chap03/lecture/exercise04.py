# 중첩 반복문을 이용한 '단어 세기(word cunt)'
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

words = []
sents = []
wnum = 0

for sen in multiline.split(sep = "\n") :
    sents.append(sen)

    for word in sen.split() :
        words.append(word)
        wnum += 1
        print(word)
print('단어 개수 :', wnum)


