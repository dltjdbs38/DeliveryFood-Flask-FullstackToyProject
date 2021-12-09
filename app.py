from flask import Flask,jsonify,request,render_template,redirect
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

@app.route('/board', methods=['GET'])
def board_page():
    return render_template('board.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['POST']) # POST 메소드, 데이터를 html에서 입력받고 저장?
def register_service():
    id = request.form['username'] # <input name="username"> 태그로부터
    pw = request.form['password'] # <input name="password"> 태그로부터

    user = {'name':id, 'password':pw}
    user_list.append(user)
    return redirect('/') 

@app.route('/board', methods=['POST']) # 추가할 글의 제목, 내용을 board_list에 추가
def writer_service():
    name = request.form['username']
    content = request.form['content']
    data = {'name':name, 'content':content}
    board_list.append(data)
    return redirect('/board') # 아직 제대로 완성된 기능이 아님.

@app.route('/board/<id>') # 추가된 글의 내용 수정, id는 작성자의 아이디가 아닌 글의 아이디
def edit_board(id): 
    content = request.form['content']
    board_list[id+1]['content']=content # 해당 글의 내용에 접근 후 수정
    return redirect('/board')

@app.route('/login',methods=['POST']) # <form action="/login" method='post'></form>
# <form>의 action 속성: 서식 데이터(form data)를 서버로 보낼 때 해당 데이터가 도착할 URL
# <form>의 method 속성: 폼 데이터(form data)가 서버로 제출될 때 사용되는 HTTP 메소드를 명시
def login_service():
    id = request.form['username']
    pw = request.form['password']
    for user in user_list:
        if user['name'] ==id and user['password']==pw: # 입력한 id와 pw가 회원목록에 있으면
            return jsonify(f'로그인 성공! 안녕하세요 {id}님')
    return jsonify('로그인 실패! 회원정보를 다시 확인해주시거나 회원가입을 해주세요.')
if __name__=='__main__': # 파일 이름이 main일때만 app.run()이 실행되도록 한다.
    app.run()