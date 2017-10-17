from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):            # StackedInline
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                 ('Date information', {'fields': ['create_time'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]
    list_display = ('question', 'create_time')


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
