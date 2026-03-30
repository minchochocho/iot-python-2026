# ex09_csv_read.py csv 파일 읽기

with open('./day02/부산시_해운대구_도서정보.CSV','r',encoding='utf-8') as f:
    # line = f.read()
    for line in f:
        print(line.strip()) # \n 줄바꿈 제거, 문자열로 출력
        # 문자열로 출력된 것을 한번더 가공하는 과정이 필요
        # 그래서 csv라는 라이브러리를 쓰는 것