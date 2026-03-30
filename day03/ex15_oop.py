## ex15_oop.py

# 기본 사용법
class Dog:
    pass    # 당장 지금 넣을게 없다~, 오류를 잡고싶을때 사용

if __name__ == '__main__':
    poppy = Dog() # 클래스 인스턴스 객체 생성, new X
    poppy.name = '뽀삐'
    poppy.age = 3

    print(f'강아지 이름 : {poppy.name}({poppy.age}살)')

