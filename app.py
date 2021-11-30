from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/',methods=['GET']) # 서버에 접속할 수 있는 url을 만들어 준다.
def greeting(): # app.route()의 url에서 실행할 함수
    # 1개의 app.route는 1개의 함수와 연결될 수 있다.
    name = request.args.get('name') # http://127.0.0.1:5000/?name=seoyoon
    return jsonify(name) # 웹페이지에 "seoyoon"이라고 뜸.


if __name__=='__main__': # 파일 이름이 main일때만 app.run()이 실행되도록 한다.
    app.run()