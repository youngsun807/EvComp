from django.urls import path
from . import views

# app 구분용 별칭, url의 일부로 사용됨
# namespace / prefix 
app_name = 'books'
urlpatterns = [
    # /books/
    path('', views.BooksModelView.as_view(), name='index'),
        #as.view는 객체를 만들어서 진행한다는 의미임
    # /books/book/
    path('book/', views.BookList.as_view(), name='book_list'),

    # /books/author/
    path('author/', views.AuthorList.as_view(), name='author_list'),

    # /books/publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),

    # /books/book/99/
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),

    # /books/author/99/
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),

    # /books/publisher/99/
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]