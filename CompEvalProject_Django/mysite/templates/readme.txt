1. 추가 application(app)
    - books

2. 작업
    - books를 생성 -> mysite/settings.py에 등록

3. 추가 학습 내용
    1. css라는 파일을 적용하는 기술
        1. html 내부에 작성
            - <style></style>
        2. css라는 확장자 별도의 파일로 분리해서 작성
            - 다수의 html이 공동된 UI를 적용하고자 할 때 권장하는 형식
            - 재사용(django의 기본)
            - <link href="css파일의 경로 및 확장자">
            <link rel="stylesheet" type="text/css" href="books/style.css">
            rel="stylesheet", type="text/css" = css 파일 의미
            href = 위치 
            - django의 app/static/app이름/*.css

 -------------------------------------------------------------------------           
 예시
        <link rel="stylesheet" href="style.css">

        위의 link 태그는 stylesheet 와 관련이 있고~~~ 
        참조하는 파일은 style.css 이다~~
        라는 것!
        [출처] [HTML] rel 은 무엇을 하는 녀석인가?|작성자 assembly_j

 --------------------------------------------------------------------------   
    2. view의 처리 로직을 class view 형태로 개발하는 학습
        1. myapp에서는 views.py의 모든 로직은 함수 기반
        2. 정해진 스펙에 맞게 쉽게 개발할 경우 상속받는 부모 클래스는 정해져 있음
            - 코드 함축 이해 필요
        
    3. Template의 재사용 기술
        1. 화면 구성을 공통적으로 구성시에 상속 개념을 반영해서 화면도 상속 가능 
        2. template tag 활용
    
4. books의 도메인
    1. 책
    2. 저자
    3. 출판사

    - 관계 
        출판사는 여러권의 책을 출판할 수가 있음
        여러명의 공동 저자가 한권의 책을 집필
        다수의 책은 하나의 출판사에 소속될 수 있음
        한 저자가 한권의 책을 집필

5. table 설계
    1. books/models.py
    Book table
        # 책과 저자는 다대다 관계(N:M)
        authors = models.ManyToManyField('Author')
        a. 생성되는 table 
            Book / Author
            다대다 관계의 모델링 기술(정규화)로 인해 book_authors
            - 총 3개가 생성
    2. 0001_initial.py scan 필수

6. url 확인
    1. http://127.0.0.1:8000/books/
        - mysite/settings.py
            : books 등록
            : ROOT_URLCONF = 'mysite.urls' - mysite의 urls.py를 검증
        - mysite/urls.py
            : path('books/', include('books.urls')), 설정으로 인해
            : books/urls.py
                - app_name = 'books'
                - path('', views.BooksModelView.as_view(), name='index'),
                - *** API 
                    as_view() 
                        : BooksModelView 를 객체 생성
                        : 요청을 forward(dispatcher)
7. template tag
    1. 로직 처리
        {% %}
        - 반복, 조건, 상속 관계형성(공통 UI 설계 후 일전 부분만 수정 의미)
        - {% if }, {% for %}, {% url %}, {% block %}
        - {% with 표현식 as 변수 %} or{% with 변수 표현식 %}
            : template tag 자체적으로 변수에 값 대입하는 대입 tag
            : 로컬 변수
    2. 단순 변수값 출력
        {{ }}
