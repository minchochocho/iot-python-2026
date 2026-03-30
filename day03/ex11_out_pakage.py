## ex11_out_pakage.py 외부 라이브러리 사용

import requests as r

response = r.get("https://www.google.com")

print(response.status_code) # 200 웹페이지 요청시 정상(OK)
print(response.content) # 웹 브라우저 대신 http프로토콜로 데이터 요청
