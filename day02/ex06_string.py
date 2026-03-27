# ex06_string.py

language = 'Python' # List와 동일 

print(language[0]) # P
print(language[5]) # n
# print(language[6]) # IndexError, '\0'무시(없음)

print(language[-1]) # n, 역순 인덱스

print(language[0:2]) # Py, 인덱스로 문자열 슬라이싱
print(language[-3:-1]) # ho, 음수 인덱스로 문자열 슬라이싱

## 문자열 함수
print(language.upper()) # 문자를 모두 대문자로
print(language.lower()) # 문자를 모두 소문자로

language = 'hello'

print(language.capitalize()) # 첫 글자만 대문자로
print(language.replace('llo','y')) # 문자 교환
print(language.count('l')) # 찾는 문자(열) 개수 확인
print(language.index('l')) # 찾는 문자(열)의 위치값

language = 'Hello Python Wow'

print(language.split()) # 공백으로 문자열 자르기

## 포맷팅(formatting)
name = 'Ashely'
age = 36

# 기본
print('이름은 %s, 나이는 %d세 입니다'%(name, age)) # C방식. 지금은 거의 안씀
print('이름은 '+name + ", 나이는 "+str(age)+'세 입니다') # 기본적으로 \n이 포함
print('이름은', name ,", 나이는",str(age),'세 입니다')

print('이름은 {0}, 나이는 {1}세 입니다'.format(name, age)) # 예전방식
print(f'이름은 {name}, 나이는 {age}세 입니다')  # 기본 f-string

# f-string 포맷팅 중
pi = 3.141592
greeting = '안녕'

print(f'{greeting:}하세요')  # 기본
print(f'{greeting:<10}하세요')  # 둘 사이에 10자 띄우기
print(f'하세요{greeting:>10}')  # 둘 사이에 10자 띄우기
print(f'{greeting:*^10}하세요')  # 변수 앞뒤에 *로 채우기

print(f'{pi}') # 소수 자리수
print(f'{pi:.2f}') # 소수점 두자리까지만 출력

print(name[::-1])  # 문자열 뒤집기
