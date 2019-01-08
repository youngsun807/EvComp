from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher


'''
http://ip:port/books
- 요청 받고 -> 화면 구성을 위한 list구성 -> 최종 template에게 출력 위힘
    : 요청박고 : http://ip:port/books
    : 화면 구성을 위한 list 구성
    context['model_list'] = ['Book', 'Author', 'Publisher']
    list에 선언된 순서대로 html에 보여짐
    향후에 순서 변경도 가능
    (화면 구성 + 응답지시)
    : 최종 template에게 출력 위힘
        화면 지정 : template_name = 'books/index.html
        실행 시점 : get_context_data() 함후가 return시 자동 실행

        - 결론 : http://ip:port/books -> BooksModelView -> index.html이 응답

1. class형 View
2. 별도의 처리 로직 없이 템플릿 파일만 출력(렌더링) 하고자 할 경우 구현 방법
    - TemplateView 상속
3. TemplateView를 상속한 경우
    1. template_name 
        - books 앱의 첫 화면 구성을 위한 템플릿 파일
    2. get_context_data()
        - 템플릿으로 전송해야 할 데이터가 있는 경우 재정의
        - super() 첫라인 필수
        - return 필수 
'''
class BooksModelView(TemplateView):
    # books/templates/books/index.html
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("**************************",context)
        # list 순서에 맞게 화면 구성, 순서 변경 가능
        context['model_list'] = ['Author', 'Publisher', 'Book']
        print("++++++++++++++++++++++++++", context)
        return context



# 각 table들의 모든 정보 제공하는 view + template
'''
1. ListView인 제네릭 view 상속
2. 객체가 들어 있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿에 전송만 하면 됨
    - table의 모든 데이터를 검색해서 전송하려 할 경우 모델명만 지정하면 됨
3. 자동 적용해주는 로직
    - templates 파일명 자동 반영
    - 모델명소문자_list.html
      : Book인 경우 book_list.html
      : books/book_list.html
'''
class BookList(ListView):
    model = Book 


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# 조건 검색인경우 사용하는 제네릭 View 
''' 
1. DetailView 제네릭 상속
2. 기능 
    - 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 전송
3. 처리 방식
    1. pk로 검색시 
        : table명 즉 모델명만 설정해주면 됨
        : URLconf에서 전송되는 데이터값을 기준으로 검색
    2. Template 명
        : 모델명소문자_detail.html로 자동 생성
''' 
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
