from django.contrib import admin
from App.models import Candidate,Questions,Questions,Result
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'name', 'test_attempted', 'test_score', 'email', 'phone']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']

admin.site.register(Candidate,CandidateAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['que_id', 'que', 'opt_1', 'opt_2', 'opt_3', 'opt_4']
    list_filter = ['que_id']
    search_fields = ['que_id']

admin.site.register(Questions,QuestionsAdmin)

