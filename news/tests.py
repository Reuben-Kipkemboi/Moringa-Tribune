from django.test import TestCase
#Importing the models we've created
from .models import Editor,Article,tags

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

