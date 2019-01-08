from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


    def __str__(self):
        return self.name 

class Profitability(models.Model):

    title = models.CharField(max_length=100) # 음절 갯수(byte아님)
    publication_date1 = models.FloatField(max_length=100)
    publication_date2 = models.FloatField(max_length=100)
    publication_date3 = models.FloatField(max_length=100)
    publication_date4 = models.FloatField(max_length=100)
    publication_date5 = models.FloatField(max_length=100)


    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Activity(models.Model):

    title = models.CharField(max_length=100) # 음절 갯수(byte아님)
    publication_date1 = models.FloatField(max_length=100)
    publication_date2 = models.FloatField(max_length=100)
    publication_date3 = models.FloatField(max_length=100)
    publication_date4 = models.FloatField(max_length=100)
    publication_date5 = models.FloatField(max_length=100)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Stability(models.Model):

    title = models.CharField(max_length=100) # 음절 갯수(byte아님)
    publication_date1 = models.FloatField(max_length=100)
    publication_date2 = models.FloatField(max_length=100)
    publication_date3 = models.FloatField(max_length=100)
    publication_date4 = models.FloatField(max_length=100)
    publication_date5 = models.FloatField(max_length=100)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Growth(models.Model):

    title = models.CharField(max_length=100) # 음절 갯수(byte아님)
    publication_date1 = models.FloatField(max_length=100)
    publication_date2 = models.FloatField(max_length=100)
    publication_date3 = models.FloatField(max_length=100)
    publication_date4 = models.FloatField(max_length=100)
    publication_date5 = models.FloatField(max_length=100)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Operation(models.Model):
    owner = models.CharField(max_length=100) # 음절 갯수(byte아님)
    publication_date1 = models.DateField()   
    etc = models.CharField(max_length=100)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Finance(models.Model):
    title = models.CharField(max_length=50)
    publication_date1 = models.URLField(max_length=100)
    publication_date2 = models.URLField(max_length=100)
    publication_date3 = models.URLField(max_length=100)
    publication_date4 = models.URLField(max_length=100)
    publication_date5 = models.URLField(max_length=100)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Analysis(models.Model):
    title = models.CharField(max_length=100)
    rm = models.FloatField(default=0)
    rf = models.FloatField(default=0)
    re = models.FloatField(default=0)
    beta = models.FloatField(default=1)
    ev = models.FloatField(default=0)
    evps = models.FloatField(default=0)

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date1 = models.DateField()

    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
