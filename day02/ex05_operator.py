# ex05_operator.py 연산자 학습

a = 2
b = 10

print('덧셈 = ', a + b)
print('뺄셈 = ', a - b)
print('곱셈 = ', a * b)
print('나눗셈 = ', a / b) # 결과 항상 float
print('몫 = ', a // b)    # 정수
print('나머지 = ', a % b) # 정수
print('거듭제곱 = ', a ** b) # a의 b승


x = 10
print(x)

x+=5 # x = x + 5
print(x)

x-=2
print(x)

x *= 13
print(x)

# 비교연산
print(' a == b ', a == b)
print(' a > b ', a > b)
print(' a > b ', a > b)
print(' a >= b ', a >= b)
print(' a <= b ', a <= b)
print(' a != b ', a != b)

# 논리연산
age = 25
is_license = True

print('나이는 20세 이상이고 면허증소지? : ', age >= 20 and is_license == True)
print('나이는 20세 이상이고 면허증소지? : ', age>=20 and is_license) # 위와 동일

print('나이가 20세 이상이거나, 면허증 소지? : ', age>=20 or is_license == True)

# 멤버연산
friuts = ['사과', '바나나', '망고', '포도']
sentence = '파이썬은 쉬워요'

print('과일 중 바나나 존재 여부 : ' ,'바나나 'in friuts)
print('과일 중 수박 존재 여부 : ' ,'수박 'in friuts)
print('문장 내 `파이썬` 존재 여부 : ' ,'파이썬 'in sentence)
