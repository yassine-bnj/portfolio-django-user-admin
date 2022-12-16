from django.contrib import admin
from cv.models import Skill,Experience,Education,Type

class SkillAdmin(admin.ModelAdmin):
  list_display = ('libelle','skillType','levelPercent','skillIcon')
  list_filter = ('skillType','levelPercent')
#   date_hierarchy = 'dateParution'
  ordering = ('levelPercent','libelle')
  search_fields = ('libelle', 'skillType')    

class EducationAdmin(admin.ModelAdmin):
  list_display = ('libelle','beginDate','endDate','location','type')
  list_filter = ('location','type')
  ordering = ('beginDate','libelle')
  search_fields = ('libelle', 'location')  

class ExperiencenAdmin(admin.ModelAdmin):
  list_display = ('libelle','post','location','tasks','beginDate','endDate')
  list_filter = ('location','post')
  ordering = ('beginDate','libelle')
  search_fields = ('libelle', 'location')  



admin.site.register(Skill,SkillAdmin)
admin.site.register(Type)
admin.site.register(Education,EducationAdmin)
admin.site.register(Experience,ExperiencenAdmin)
