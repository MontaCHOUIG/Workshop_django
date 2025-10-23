from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Conference
from .forms import ConferenceModel
from django.views.generic import ListView , DetailView , CreateView, UpdateView ,DeleteView

def get_all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/conferences_list.html', {'conferences': conferences})

# Create your views here.
class ConferenceList(ListView):
    model = Conference
    context_object_name = 'conferences'
    ordering = ['start_date']
    template_name = 'conference/conferences_list.html'

class ConferenceDetails(DetailView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'conference/conference-details.html'
    pk_url_kwarg = 'conference_id'
    
class ConferenceCreate(CreateView):
    model=Conference
    template_name='conference/conference_form.html'
    #fields='__all__'
    form_class=ConferenceModel
    success_url=reverse_lazy('conference-list')


class ConferenceUpdate(UpdateView):
    model = Conference
    template_name = 'conference/conference_form.html'
    form_class = ConferenceModel
    success_url = reverse_lazy('conference-list')

class ConferenceDelete(DeleteView):
    model = Conference
    template_name = 'conference/conference_confirm_delete.html'
    success_url = reverse_lazy('conference-list')
