from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from cv.models import Skill,Experience,Education,Type
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


def connect(request):
    template = loader.get_template('connect.html')
   
    context = {
       
       
    }
    return HttpResponse(template.render(context, request))


@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dashborad_education(request):

    template = loader.get_template('dashboard-education.html')
    educ = Education.objects.all().values()
    types = Type.objects.all().values()
   
    context = {
        
        "educ":educ,
        "types":types,
      
       
    }
    return HttpResponse(template.render(context, request))
@login_required
def add_educ(request):
 libelle = request.POST['label']
 dateb = request.POST['dateBegin']
 datee= request.POST['dateEnd']
 location= request.POST['location']
 type = request.POST['type']
 

 typ = Type.objects.get(id=type)
 educ = Education()
 educ.libelle=libelle
 educ.beginDate=dateb
 educ.endDate=datee
 educ.location=location
 
 if len(request.FILES) != 0:
    educ.certificate=request.FILES['Certificate']
 educ.type=typ
 educ.save()
 return HttpResponseRedirect(reverse('dashboard_education')) 


@login_required
def del_educ(request, id):
 educ = Education.objects.get(id=id)
 educ.delete()
 return HttpResponseRedirect(reverse('dashboard_education')) 

@login_required
def Update_education(request, id):
 educ = Education.objects.get(id=id)
 types = Type.objects.all().values()
 template = loader.get_template('update-education.html')
 context = {
  
 'educ': educ,
 'types':types, }
 return HttpResponse(template.render(context, request))

@login_required
def update_educ_action(request, id):
 libelle = request.POST['label']
 dateb = request.POST['dateBegin']
 datee= request.POST['dateEnd']
 location= request.POST['location']
 type = request.POST['type']


 typ = Type.objects.get(id=type)
 educ = Education.objects.get(id=id)
 if len(request.FILES) != 0:
    educ.certificate=request.FILES['Certificate']
 educ.libelle=libelle
 educ.beginDate=dateb
 educ.endDate=datee
 educ.location=location
 educ.type=typ
 educ.save()
 return HttpResponseRedirect(reverse('dashboard_education')) 




@login_required
def dashborad_edTypes(request):
    template = loader.get_template('dashboard-types.html')
    types = Type.objects.all().values()
    context = {
        
         'types':types
    }
    return HttpResponse(template.render(context, request))    


@login_required
def add_type(request):
 libelle = request.POST['type']
 type = Type(libelle=libelle)
 type.save()

 return HttpResponseRedirect(reverse('types')) 


@login_required
def Update_type(request,id):
    template = loader.get_template('update-type.html')
    type = Type.objects.get(id=id)
    context = {
        
        "type":type
       
    }
    return HttpResponse(template.render(context, request))   

@login_required
def update_type_action(request, id):
 libelle = request.POST['label']
 
 type = Type.objects.get(id=id)
 type.libelle=libelle
 type.save()
 return HttpResponseRedirect(reverse('types')) 


@login_required
def del_type(request, id):
 type = Type.objects.get(id=id)
 type.delete()
 return HttpResponseRedirect(reverse('types')) 



def signIn(request):
 username = request.POST['username']
 password = request.POST['password']
 user = authenticate(request, username=username,password=password)
 if user is not None:
  login(request, user)
  request.session['username'] = username
  return HttpResponseRedirect(reverse('dashboard_education'))

 else:
   
  print("Login et/ou mot de passe incorrect")
  return render(request,'connect.html', context={'error':True})
  #return HttpResponseRedirect(reverse('connect'))  

def signOut(request):
 logout(request)
 return HttpResponseRedirect(reverse('connect'))   