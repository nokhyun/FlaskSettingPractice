from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello 월드'

@app.route('/name')
def getName():
    return 'Nokhyun'

if __name__ == '__main__':
    app.run(debug=True)

# python 설치 후 Shift + command + p 눌러서 Python: 인터프린터 경로 설정
# source venv/bin/activate // 가상환경 활성화
# pip3 install flask // 설치 후 실행
# set FLASK_ENV=development // This is a development server. Do not use it in a production deployment.