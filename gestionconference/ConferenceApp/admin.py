from django.contrib import admin
from .models import Conference , Submission
# Register your models here.
admin.site.register(Conference)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'user', 'conference', 'titre', 'status', 'payed', 'submission_date')
    list_filter = ('status', 'payed', 'submission_date')
    search_fields = ('submission_id', 'user__username', 'conference__name', 'titre')
    ordering = ('-submission_date',)
    fieldsets = (
        ("information generale",{
            "fields" : ('submission_id', 'user', 'conference', 'titre', 'abstract', 'keywords', 'paper')
        }),
        ("logistic",{
            "fields" : ('status', 'payed', 'submission_date')
        }))