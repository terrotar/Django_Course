from django.contrib import admin


from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    # TabularInline istead of StackedInline is a huge difference
    # that it's simple to change and improve experience and results.
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Display of Choices in line
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # List of title displayed in the page
    list_filter = ['pub_date']
    # Put a filter of 'pub_date' automatically
    search_fields = ['question_text']
    # Put a filter of 'question_text' automatically


admin.site.register(Question, QuestionAdmin)
