from django.urls import path
from . import views
urlpatterns = [
 path('connect', views.connect, name='connect'),
 path('education', views.dashborad_education, name='dashboard_education'),
 path('addEduc/', views.add_educ, name='addEduc'),
 path('types/', views.dashborad_edTypes, name='types'),
 path('types/addType/', views.add_type, name='addType'),
 
 
 path('update_educ/<int:id>', views.Update_education, name='update_educ'),
 path('update_educ/update_educ_action/<int:id>',views.update_educ_action, name='update_educ_action'),



 path('types/update_type/<int:id>', views.Update_type, name='updateType'),
 path('types/update_type/update_type_action/<int:id>', views.update_type_action, name='updateType_action'),
 path('del_educ/<int:id>', views.del_educ, name='del_educ'),
 path('types/del_type/<int:id>', views.del_type, name='del_type'),



 path('login/', views.signIn, name='signIn'),
 path('login/login/', views.signIn, name='signIn'),
 path('disconnect/', views.signOut, name='disconnect'),

 ]