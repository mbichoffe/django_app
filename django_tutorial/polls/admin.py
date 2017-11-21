from django.contrib import admin

# Register your models here.
from .models import Question, Choice



admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
"""
You’ll follow this pattern – create a model admin class, then pass it as the 
second argument to admin.site.register() – any time you need to change the 
admin options for a model.
"""