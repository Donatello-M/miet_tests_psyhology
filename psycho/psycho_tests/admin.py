from django.contrib import admin
from .models import Answer, Question


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "result")
    search_fields = ("last_name", "first_name", "result", "pub_date")
    list_filter = ("result", "pub_date")
    empty_value_display = "-пусто-"


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("ask", "key_type")
    search_fields = ("ask",)
    list_filter = ("ask", "key_type")
    empty_value_display = "-пусто-"


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
