# ex03_logic_control 분기문/반복문

# 분기문
age = int(input('나이는?'))

if age < 19:
    print('집에가세요')
elif age>30 and age <=60 :
    print('못 들어갑니다')
else:
    print('어, 들어오세요~')
    print('어서오세요!!')

# 반복문
num=int(input('반복횟수 > '))
for i in range(num):
    print(i)

print('-----')

for i in range(1,num+1):
    print(i)

print('-----')

for i in range(2,11,2):
    print(i)
    