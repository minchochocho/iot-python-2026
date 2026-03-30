## ex16_oop.py 객체지향 클래스

class Dog:
    # 생성자
    def __init__(self,name):
        self.name = name

    def bark(self): # 값을 넘길게 없어도 무조건 self를 줘야 한다
        print(f'{self.name}(이)가 짖습니다. 멍멍!')

poppy = Dog('뽀삐')
choco = Dog('초코')

poppy.bark()
choco.bark()