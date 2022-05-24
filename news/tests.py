from django.test import TestCase
#Importing the models we've created
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.reuben= Editor(first_name = 'Reuben', last_name ='Rotich', email ='reuben.kipkemboi@student.moringaschool.com')
        
    # Testing  instance to see if the object is instantiated correctly
    def test_instance(self):
        self.assertTrue(isinstance(self.reuben,Editor))
        
    # Testing Save Method
    def test_save_method(self):
        self.reuben.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
        
 #Article test classes       
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.reuben= Editor(first_name = 'Reuben', last_name ='kipkemboi', email ='reuben.kipkemboi@moringaschool.com')
        self.reuben.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.reuben)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
        
    #getting todays news
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
        
     #getting news according to a given date   
    def test_get_news_by_date(self):
        test_date = '2018-05-24'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
        
   

