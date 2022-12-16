from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
 path('about/', views.about, name='about'),
 
 path('skills/', views.skills, name='skills'),
 path('education/', views.education, name='education'),
 path('experience/', views.experience, name='experience'),

 ]