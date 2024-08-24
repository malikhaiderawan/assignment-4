from django.db import models

# Create your models here.

#class for Author
class Author(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name

#class for posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
