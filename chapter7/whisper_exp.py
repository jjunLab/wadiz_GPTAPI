import openai

#API Ű �Է�
openai.api_key ="API Key"
# �������� ����
audio_file = open("output.mp3", "rb")
# whisper �𵨿� �������� �ֱ�
transcript = openai.Audio.transcribe("whisper-1", audio_file)
#��� ����
print(transcript)