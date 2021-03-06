# Resident registration number
# 901201 - 1111111

# Email adress
# bae3054@naver.com

# The car's number
# 123가 1234

# IP adress
# 192.168.0.1

import re
# abcd, book, desk
# ca?e
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")

# . : Meaning one literal
# ex) ("ca.e") = cafe(O), care(O), case(O), caffe(X)
# ^ : Meaning the first string (문자열의 시작)
# ex) ("^de") = desk(O), destination(O), fade(X),
# $ : Meaning the last string (문자열의 끝)
# ex) ("se$") = case(O), base(O), face(X)


def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열을 반환
        print("m.string:", m.string)  # 입력받은 문자열을 반환
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작과 끝 index
    else:
        print("Not matching")


# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는 지 확인
# print_match(m)

# m = p.search("good care")  # search : 주어진 문자열 중에 일치하는 게 있는 지 확인
# print_match(m)

# lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는 지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는 지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태
# . : Meaning one literal
# ex) ("ca.e") = cafe(O), care(O), case(O), caffe(X)
# ^ : Meaning the first string (문자열의 시작)
# ex) ("^de") = desk(O), destination(O), fade(X),
# $ : Meaning the last string (문자열의 끝)
# ex) ("se$") = case(O), base(O), face(X)
