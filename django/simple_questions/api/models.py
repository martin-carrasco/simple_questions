from django.core.exceptions import FieldError
from django.db import models
from django.db.models.fields.related import ForeignKey
from simple_questions import settings


class BaseComment(models.Model):
    """
    Basic information related basic information a comment should contain:
    - Content in string format
    - Creator
    - Dates for creation and update
    - Score of the comment
    """
    content = models.CharField(max_length=1024)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.content)

class Thread(models.Model):
    """
    Model for managing a Thread:
    - Title
    - Number of views
    - Creator
    - Update and creation timestmaps
    """
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=128)

class Post(BaseComment):
    """
    Model for managing a post
    Base comment information
    - If it's an accepted post as best answer
    - If it's the main post the thread creator started the thread with
    """
    thread = ForeignKey(Thread, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.thread.creator != self.creator and self.main:
            raise FieldError("Main post needs to be by thread creator")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated_at']

class Reply(BaseComment):
    """
    Model for managina a Reply:
    - Content (less than a base comment)
    """
    content = models.CharField(max_length=256)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'post'
