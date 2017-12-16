from django.contrib import admin

# Register your models here.
from tryquest.apps.question.models import Question, Option

class OptionAdmin(admin.StackedInline):
    model = Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    exclude = ['date_added', 'author']
    inlines = [OptionAdmin]
    date_hierarchy = 'date_added'

    list_filter = ('date_added', 'author')
    search_fields = ['author', 'text', 'tags']

    save_as = True
    save_on_top = True
    save_as_continue = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request,obj,form,change)

