from django.contrib import admin
from .models import Conference , Submission
# Register your models here.

admin.site.header = "Conference Management Admin"
admin.site.index_title = "Admin Dashboard"


@admin.action
def mark_as_payed(modeladmin, request, queryset):
    queryset.update(payed=True) 

@admin.action
def mark_as_accepted(modeladmin, request, queryset):
    queryset.update(status='accepted')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'payed', 'submission_date')
    actions = [mark_as_payed, mark_as_accepted]
    list_filter = ('status', 'payed', 'submission_date')
    search_fields = ( 'user__username', 'keywords', 'titre')
    ordering = ('-submission_date',)
    fieldsets = (
        ("information generale",{
            "fields" : ( 'user', 'conference', 'titre', 'abstract', 'keywords', 'paper')
        }),
        ("logistic",{
            "fields" : ('status', 'payed')
        }))
    
class SubmissionInline(admin.StackedInline):
    model=Submission
    extra=1
    readonly_fields =("submission_id",)

@admin.register(Conference)
class AdminPerso(admin.ModelAdmin):
    list_display =("name","theme","location","start_date","end_date","duration")
    ordering= ("start_date",)
    list_filter =("theme","location","end_date")
    search_fields =("name",)
    fieldsets = (
            ("Information General",{
                "fields": ("conference_id","name", "theme","description")
            }),

            ("Logistics" , {
                "fields": ("location","start_date","end_date")
            }),
    )
    readonly_fields= ("conference_id",)
    date_hierarchy = "start_date"
    inlines = [SubmissionInline]
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "RAS"
    duration.short_description="Duration (days)"






