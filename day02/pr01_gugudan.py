## pr01_gugudan.py 구구단 프로그램

# 2중 for 문

dan = int(input('출력 최대 단 수(2 ~ 9) > '))

for i in range(2,dan+1):
    print(f'{i}단 출력')
    print('-------------')
    for j in range(1,9+1):
        print(f'{i} X {j} = {i*j:<3}', end=' ')
