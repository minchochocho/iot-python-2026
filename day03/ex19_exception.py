## ex19_exception.py


# 예외가 발생할 것으로 추측되는 위치를 try로 감싼다
try:
    num = int(input('나눌 분모 입력 > '))

    res = 100/num
    print(f'100 / {num} = {res}')
except ZeroDivisionError as e : # 0으로 나눌때
    print('0은 쓰지 마세요')
except ValueError as e :        # 숫자 대신 문자를 입력했을때
    print('숫자만 넣어주세요')
except Exception as e : # 예외클래스 인스턴스 e 생성
    print(e.args)
else:
    print('프로그램 정상 종료') # 정상적으로 종료되면 출력
finally: # 옵션
    print('예외 유무 관계없이 실행')
