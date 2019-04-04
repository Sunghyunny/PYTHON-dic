# =========================================================
# 필요한 모듈은 이곳에 importing 합니다.
import re

# 필요한 모듈은 이곳에 importing 합니다.
# =========================================================


# =========================================================
# 이곳에 함수를 작성합니다.

#1. 더하기 기능
def add(a, b):
    return a + b

#2. 빼기 기능
def miuns(a, b):
    return a - b

#3. 곱셈 기능
def multiple(a, b):
    return a * b

#4. 나눗셈 기능
def divide(a, b):
    return a / b

#5. 다항 덧셈 기능
def multisum(*a):
    result = 0
    for i in a:
        result = result + i
    return result

#6. 칸을 나누는 함수
def line():
   return "=" * 50

#7. 리스트의 인덱싱
def indexing(a, b):
    return a[b]

#8. 리스트의 슬라이싱
def sli():
    a = "가나다라마바사"
    print(a[1:3])

#9.리스트의 여러요소 삭제
def multislice():
    a = [1, 2, 3, 4, 5, 6]
    del a[1:3]
    print(a)

#10. 리스트 순차배열
def array():
    a = [4, 5, 1, 3, 5]
    a.sort()
    print(a)

#11. 성별감지
def human():
    a = input("주민등록번호를 입력해주세요")
    b = int(a[6])
    if b == 1:
        print("male")
    else:
        print("female")

#12. 예비군 계산기
def vet():
    a = input("군번을 입력해주세요")
    b = int(a[0:2])
    if b == 13:
        print("개구리, 마지막")
    elif b == 14:
        print("1년 남음")
    elif b == 15:
        print("2년 남음")
    else:
        print("뭘 세고있어요")

#13. 화석 판독기
def dino(a):
    print("안녕하세요 {0}학번 입니다.".format(a))

#14. 리스트 숫자 역순 추출
def reverse():
    a = [1, 2, 3, 4, 5]
    a.reverse()
    print(a)

#15. 리스트 숫자 수정
def fix():
    a = [1, 2, 3, 4, 5]
    a[3] = 'fix'
    del a[1]
    print(a)

#16. 동점자를 추출  그 수를 세는 함수
def samepoint():
    a = input("점수를 입력하세요")
    b = [90, 87, 87, 82, 90, 87, 85]
    b.count(int(a))

#17. 리스트에서 홀수만을 추출
def drain(*num):
    for i in num:
        if i % 2 == 1:
           return print(i)

#18.홀수 짝수 구분
def odd():
    a = int(input(""))
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

#19. 학점계산기
def grade():
    a = int(input("점수를 입력해주세요."))
    if a >= 80:
        print("A")
    elif a >= 60:
        print("B")
    elif a >= 40:
        print("C")
    else:
        print("F")

#20. jpg파일 걸러내기
def jpg():
    a = [".jpg", ".png", ".pdf", "hwp", ".ppt"]
    for i in a:
        if i == ".jpg":
            print(".jpg")
        else:
            print("Error")

#21. 우대권 발급
def old():
    ticket = 3000
    a = int(input("나이를 입력해주세요."))
    if a >= 65:
        print(ticket * 0.5)
    else:
        print(ticket)

#22. 3의배수의 합
def baesu():
    a = int(input("합이 필요한 숫자를 기입해주세요"))
    b = 0
    while b < a:
        b = b + 1
        if b % 3 == 0:
            i = 0
            for i in b:
                i = i + b
    print(b)
#23. 평균값 계산
def avr():
    a = [5, 1, 7, 5, 9]
    b = len(a)
    c = 0
    for i in a:
        c = c + i
    return i / int(b)

#24. 입력값의 개수를 모를 때 평균값 계산
def avrnone(*score):
    result = 0
    for i in score:
        result = result + i
    return result / len(score)



#25. 구구단
def kkd():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j)

#26. 피라미드
def pyramid():
    a = int(input("피라미드의 층수를 입력해주세요"))
    for i in range(1 , a+1):
        print(" "*(a-i), "*"*(2*i-1))

#27. 중복수 제거
def remove():
    a = input("숫자를 입력해주세요: ")
    b = set(a)
    c = list(b)
    print(c)

#28. 교집합 찾기
def inter():
    a = set([1, 4, 6, 7 ,0])
    b = set([1, 5, 6, 4, 7])
    print (a & b)

#29. 합집합 찾기
def plus():
    a = set([1, 3, 5, 2 ,7])
    b = set([2, 5, 6, 4 ,3])
    print(a | b)

#30. 인사
def bye():
    print("bye")

# 이곳에 함수를 작성합니다.
# =========================================================

# =========================================================
# 따로 설정할 필요 없습니다.
def main():
    print("함수 사전 목록을 불러옵니다.")


if __name__ == "__main__":
    main()
    func_list = []

    for i in dir():
        if re.search('[__]+', i) or i == "i" or i == "re" or i == "main":
            pass
        else:
            func_list.append(i)

    for num, func in enumerate(func_list, start=1):
        print("{0}: {1}".format(num, func))

# 따로 설정할 필요 없습니다.
# =========================================================
