from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100) # 음절 갯수(byte아님)

    # 책과 저자는 다대다 관계(N:M)
    authors = models.ManyToManyField('Author')

    # 책과 출판사는 N:1 관계(여러 권의 Book은 하나의 publisher간에 관계)
    # 출판사의 pk기준으로 참조하는 데이터는 해당 pk 삭제시 books tables에서도 삭제
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    publication_date = models.DateField()

    # book 객체값 출력시 자동 호출되는 함수
    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
