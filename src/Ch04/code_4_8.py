#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 4.8 if-else 문 안에 if-else 문 넣기, 108쪽
#
num = int(input("정수를 입력하시오: "))
if num >= 0:         # 반드시 들여쓰기를 하여 블럭을 생성
    if num == 0:     # 블럭 내에서 세부적인 조건을 한 번 더 검사
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")