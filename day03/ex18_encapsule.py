## ex18_encapsule.py 캡슐화

class Account:
    def __init__(self, money):  # 초기화   
        # self.balance = money    # self.balance는 public 접근과 동일
        self.__balance = money  # __는 private와 동일

    def deposit(self, money):  # 입금
        self.balance += money

    def get_balance(self):  # 계좌조회
        return self.balance
    

if __name__ == '__main__':
    myacc = Account(100000)
    print(f'계좌금액은 {myacc.get_balance():,}원')  # 천단위 구분기호 하려면 `:,`
    # print(f'계좌금액 : {myacc.balance}달러') # __ 변수는 외부 접근 불가

    myacc.deposit(100_000)  # 정수 사용시 _로 천단위 구분 가능
    print(f'계좌금액은 {myacc.get_balance():,}원') 

    myacc.balance = -10000000 #멤버변수에 직접접근가능
    print(f'계좌금액은 {myacc.get_balance():,}원')
    