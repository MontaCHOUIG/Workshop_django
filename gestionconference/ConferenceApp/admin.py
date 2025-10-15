from django.contrib import admin
from .models import Conference , Submission
# Register your models here.

admin.site.header = "Conference Management Admin"
admin.site.index_title = "Admin Dashboard"


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
    

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('conference_id', 'name', 'location', 'theme', 'start_date', 'end_date')
    list_filter = ('theme', 'start_date', 'end_date')
    search_fields = ('name', 'location', 'theme')
    ordering = ('-start_date',)
    fieldsets = (
        ("Information générale", {
            "fields": ('conference_id', 'name', 'description', 'location', 'theme', 'start_date', 'end_date')
        }),
        ("Dates", {
            "fields": ('created_at', 'updated_at')
        })
    )