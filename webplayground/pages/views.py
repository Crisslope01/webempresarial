from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class PageListView(ListView):
    model = Page
    
class PageDetailView(DetailView):
    model = Page
   
class PagesCreateView(CreateView):
    model = Page
    fields = ["title", "content", "order"]
 