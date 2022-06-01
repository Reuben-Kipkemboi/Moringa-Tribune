from django.db import models
import datetime as dt

from django.contrib.auth.models import User
#Tinymce
from tinymce.models import HTMLField


# Create your models here.
#Editor model this will contain data of our editor
# class Editor(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)
    
#     def __str__(self):
#         return self.first_name
#     #save function
#     def save_editor(self):
#         self.save()
        
  #Tag model      
class tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length =60)
    # post = models.TextField()
    post= HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True)
    # pic_image=models.ImageField(upload_to = 'pictures/',default='pictures/user.png')
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
#subscribe model  
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

