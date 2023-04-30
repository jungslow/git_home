# (1) 특정 글자 수 변환
oneline = "this is one line string"
print('i 글자 수 : ', oneline.count('i'))

# (2) 접두어 문자 비교 판단
print(oneline.startswith('this'))
print(oneline.startswith('that'))

# (3) 문자열 교체
print(oneline.replace("this", 'that'))

# (4) 문자열 분리(split) : 문단 ==> 문장
multiline = """this is 
multi line
string"""
sent = multiline.split('\n')
print('문장 : ', sent)

# (5) 문자열 분리(split) : 문장 ==> 단어
words = oneline.split(' ')
print('단어 : ', words)

# (6) 문자열 결합(join) : 단어 ==> 문장
sent2 = ', '.join(words)
print(sent2)