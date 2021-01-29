from django.contrib import admin
from .models import Poll, Question, QuestionChoice


class QuestionChoiceInLine(admin.TabularInline):
    extra = 0
    min_num = 2
    model = QuestionChoice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionChoiceInLine,
    ]


class PollAdmin(admin.ModelAdmin):
    model = Poll

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        return ['start_date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
