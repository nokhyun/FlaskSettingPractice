from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

# python 설치 후 Shift + command + p 눌러서 Python: 인터프린터 경로 설정
# source venv/bin/activate // 가상환경 활성화
# pip3 install flask // 설치 후 실행
