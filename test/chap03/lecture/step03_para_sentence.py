string = """git 기능을 테스트중입니다. 
나는 홍길동입니다.
주소는 서울시 송파구입니다.
나이는 35세입니다."""

sents = []
words = []

# (1) 문단 ==> 문장
for sen in string.split("\n") :
    sents.append(sen)
    # (2) 문장 --> 단어
    for word in sen.split() :
        words.append(word)

print('문장 :', sents)
print('문장 수 :', len(sents))
print('단어 :', words)
print('단어 수 :', len(words))

