from django.shortcuts import render

from .models import Conference

def get_all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/conferences_list.html', {'conferences': conferences})

# Create your views here.
