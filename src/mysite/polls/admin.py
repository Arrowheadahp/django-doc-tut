from django.contrib import admin

# Register your models here.
from .models import question, choice
# admin.site.register(question)
# admin.site.register(choice)


class choiceInLine(admin.TabularInline):
    model = choice
    extra = 3

class questionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'q_text']
    fieldsets = [
        (None,               {'fields': ['q_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [choiceInLine]
    list_display = ('q_text', 'pub_date', 'was_published_recently')

admin.site.register(question, questionAdmin)