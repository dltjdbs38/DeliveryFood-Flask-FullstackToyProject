사용법

1. python3 -m pip install flask
2. 플라스크 실행 python3 app.py(=실행할 파일)

REST API란?

- HTTP URI를 통해 자원을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해
  해당 자원에 대한 CRUD Operation을 적용하는 것

- GET = 조회, POST = 생성/수정/삭제

GET

- 데이터를 URL뒤에 ?와 함꼐 사용
- GET 방식의 HTTP 요청은 브라우저에 의해 캐시되어(cached) 저장됩니다.
- GET 방식은 보통 쿼리 문자열(query string)에 포함되어 전송되므로, 길이의 제한이 있습니다.

POST

- 특정 양식에 데이터를 넣어 전송
- POST 방식은 폼 데이터를 별도로 첨부하여 서버로 전달하는 방식입니다.

- POST 방식의 HTTP 요청은 브라우저에 의해 캐시되지 않으므로, 브라우저 히스토리에도 남지 않습니다.

- POST 방식의 HTTP 요청에 의한 데이터는 쿼리 문자열과는 별도로 전송됩니다.

- 따라서 데이터의 길이에 대한 제한도 없으며, GET 방식보다 보안성이 높습니다.
