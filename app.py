from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

user_list = [
    {'name':'SY','password':'1999'},
    {'name':'SM','password':'1995'},
    {'name':'SA','password':'1996'},
    {'name':'BB','password':'2018'}
]

board_list = []

@app.route('/greeting') # 서버에 접속할 수 있는 url을 만들어 준다.
def greet(): # app.route()의 url에서 실행할 함수
    # 1개의 app.route는 1개의 함수와 연결될 수 있다.
    name = request.args.get('name') # http://127.0.0.1:5000/?name=seoyoon
    return jsonify(name) # 웹페이지에 "seoyoon"이라고 뜸.

@app.route('/') 
def home_page(): 
    return render_template('index.html')

@app.route('/register',methods=['GET'])    
def regist_page():
    return render_template('register.html')



if __name__=='__main__': # 파일 이름이 main일때만 app.run()이 실행되도록 한다.
    app.run()