from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Skill(models.Model):
    x=[
        ('linguistic','linguistic'),
        ('technical','technical')
    ]
    libelle = models.CharField(max_length=20)
    skillType=models.CharField(max_length=20,choices=x)
    levelPercent=models.IntegerField()
    skillIcon=models.ImageField( upload_to="cv/static/skillsIcons/", default="cv/static/skillsIcons/icon.png")
   

    def __str__(self) -> str:
        return self.libelle


class Education(models.Model):
    x=[
        ('education','education'),
        ('training','training')
    ]
    libelle = models.CharField(max_length=100)
    beginDate=models.IntegerField()
    endDate=models.IntegerField()
    location=models.CharField(max_length=50)
    certificate=models.ImageField( upload_to="cv/static/certificates/", default="cv/static/certificates/certificate.png")
    type = models.ForeignKey('Type', on_delete=models.CASCADE,)
   

    def __str__(self) -> str:
        return self.libelle

class Type(models.Model):
    libelle= models.CharField(max_length=50)
    
  
    
    def __str__(self) -> str:
     return self.libelle     

class Experience(models.Model):
    libelle = models.CharField(max_length=100)
    post=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    tasks=models.TextField()
    beginDate=models.IntegerField()
    endDate=models.IntegerField()
    
   

    def __str__(self) -> str:
        return self.libelle