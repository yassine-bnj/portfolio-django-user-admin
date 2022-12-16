from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from cv.models import Skill,Experience,Education,Type
def about(request):
    template = loader.get_template('about.html')
    context = {
        'firstName': 'Yassine',
        'lastName': 'ben jeddou',
        'age': 21,
        'gender': "Male",
        'email':"yassinebenjeddou5@gmail.com",
        'adress': "nabeul",
        'country':"Tunisia",
        'phoneNumber':"55210306",
        'post':"Full Stack developper",
        'freelance':True,
        'description1':"I Am Yassine, Junior Web Developer, A Passionate Freelancer Bringing You Programming And Design From The Future. I Am Experienced In Developing Web.|",
        "description2":"I'm An Enthusiastic Person Who Lives By Learning New Skills And Experiences, Beside My Technical Interests Which Are Mainly Presented In Software Development, I'm Also Interested In Developing My Interpersonal Skills.",
        "image1":"yassine-1_1080x1080.png",
        "image2":"yassine-2_1080x1344.png",
        "resume":"cvYassine.pdf",
        "linkedIn":"https://www.linkedin.com/in/yassine-ben-jeddou-8a2a09213/"
       
    }
    return HttpResponse(template.render(context, request))
def skills(request):
    template = loader.get_template('skills.html')
    skills=Skill.objects.all().order_by('levelPercent').values()
    context = {
        'firstName': 'Yassine',
        'lastName': 'ben jeddou',
        'skills':skills,
    }
    return HttpResponse(template.render(context, request))

def experience(request):
    template = loader.get_template('experience.html')
    experience=Experience.objects.all().order_by('beginDate').values()
    context = {
        'firstName': 'Yassine',
        'lastName': 'ben jeddou',
        'experience':experience
       
    }
    return HttpResponse(template.render(context, request)) 


def education(request):
    template = loader.get_template('education.html')
    education=Education.objects.all().order_by('beginDate').values()
    types= Type.objects.all().values
    context = {
        'firstName': 'Yassine',
        'lastName': 'ben jeddou',
        'education':education,
        'types':types
    }
    return HttpResponse(template.render(context, request))