# ��Ű�� �ҷ�����
from googletrans import Translator

text = "LangChain is a framework for developing applications powered by language models"

#���� ������ü ����
google = Translator()
#��������
result = google.translate(text, dest="ko")
#��� Ȯ��
print(result.text)