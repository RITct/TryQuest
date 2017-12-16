from django.contrib import admin


# Register your models here.
from tryquest.apps.question.models import Question


@admin.register(Question)
class Question(admin.ModelAdmin):
    exclude = ['date_added']
