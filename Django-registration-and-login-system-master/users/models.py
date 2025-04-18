from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
       
class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    Course = models.CharField(max_length=255)
    image = models.ImageField(default=None)
    chap1 = models.URLField()
    chap2 = models.URLField()
    chap3 = models.URLField()
    chap4 = models.URLField()
    chap5 = models.URLField()
    chap6 = models.URLField()
    chap7 = models.URLField()
    chap8 = models.URLField()
    chap9 = models.URLField()
    chap10 = models.URLField()

    def __str__(self):
        return self.Course
    
class Exam(models.Model):
    id = models.BigAutoField(primary_key=True)
    Course = models.ManyToManyField(Course)
    Question = models.TextField()
    opt1 = models.CharField(max_length=255)
    opt2 = models.CharField(max_length=255)
    opt3 = models.CharField(max_length=255)
    opt4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.Question
 
class contactus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    typeyourmessage = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
class Result(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    result = models.IntegerField(default=0)    

    def __str__(self):
        return self.name
    
