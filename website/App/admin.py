from django.contrib import admin
from App.models import Candidate,Questions,Result,Exam,Plans,Notes
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'name', 'test_attempted', 'test_score', 'email', 'phone']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']

admin.site.register(Candidate,CandidateAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['que_id', 'que', 'opt_1', 'opt_2', 'opt_3', 'opt_4']
    list_filter = ['que_id','exam']
    search_fields = ['que_id']

admin.site.register(Questions,QuestionsAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ['username', 'res_id', 'test_score','right_attempts','wrong_attempts','date_attempted','time']
    list_filter = ['username']
    search_fields = ['username']

admin.site.register(Result,ResultAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    
admin.site.register(Exam,ExamAdmin)

class PlansAdmin(admin.ModelAdmin):
    list_display = ['price','plan_type']

admin.site.register(Plans,PlansAdmin)


class NotesAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Notes,NotesAdmin)
