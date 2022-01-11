from django.core.exceptions import FieldError
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from api.models import Post, Thread

User = get_user_model()

class ThreadTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='martincc', email='martin.carrasco@utec.edu.pe', password='12345', display_name='martincc123')
        User.objects.create(username='juanbb', email='juan.bonero@utec.edu.pe', password='123451l', display_name='juannn')
        Thread.objects.create(creator = User.objects.get(username='martincc'), title='Test thread compromised of 1234 @as f')

    def test_main_post_diff_creator(self):
        """
        Test if a main post of a thread can be created by a different user
        """
        test_user = User.objects.get(username='juanbb')
        test_thread = Thread.objects.get(title='Test thread compromised of 1234 @as f')
        try:
            Post.objects.create(thread=test_thread, creator=test_user, content ='I have this problem', main=True)
            self.fail("Main post was created with a different user than the creator of the thread")
        except FieldError as e:
            pass



    
        