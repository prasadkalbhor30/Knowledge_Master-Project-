from django.db import models
from PIL import Image
# Create your models here.

class main_test_Categories(models.Model):
    Heading=models.CharField(max_length=40)
    description=models.CharField(max_length=300)
    img=models.ImageField(upload_to="test_images/",default="")

    
    def __str__(self):
        return self.Heading
  
class Category(models.Model):
    topics=models.ForeignKey(main_test_Categories,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)


    def __str__(self):
        return self.title+"---"+self.topics.Heading

class sub_Category(models.Model):
    topics=models.ForeignKey(Category,on_delete=models.CASCADE)
    name_Of_Sub_Catagory=models.CharField(max_length=100)


    def __str__(self):
        return self.name_Of_Sub_Catagory


class c_language(models.Model):
    qno=models.IntegerField(auto_created=True,primary_key=True)
    que=models.CharField(max_length=500)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    ans=models.CharField(max_length=1)
    
class cpp_language(models.Model):
    qno=models.IntegerField(auto_created=True,primary_key=True)
    que=models.CharField(max_length=500)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    ans=models.CharField(max_length=1)
class python(models.Model):
    qno=models.IntegerField(auto_created=True,primary_key=True)
    que=models.CharField(max_length=500)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    ans=models.CharField(max_length=1)
class java(models.Model):
    qno=models.IntegerField(auto_created=True,primary_key=True)
    que=models.CharField(max_length=500)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    ans=models.CharField(max_length=1)
class javascript(models.Model):
    qno=models.IntegerField(auto_created=True,primary_key=True)
    que=models.CharField(max_length=500)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    ans=models.CharField(max_length=1)

class user(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=100,default="")
    pwd=models.CharField(max_length=16)
