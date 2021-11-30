from flask import Flask,render_template
app = Flask(__name__)

@app.route('/') # 서버에 접속할 수 있는 url을 만들어 준다.
def greeting(): # app.route()의 url에서 실행할 함수
    # 1개의 app.route는 1개의 함수와 연결될 수 있다.
    return render_template('index.html')


if __name__=='__main__': # 파일 이름이 main일때만 app.run()이 실행되도록 한다.
    app.run()