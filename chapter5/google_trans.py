# 패키지 불러오기
from googletrans import Translator

text = "LangChain is a framework for developing applications powered by language models"

#구글 번역객체 생성
google = Translator()
#번역실행
result = google.translate(text, dest="ko")
#결과 확인
print(result.text)