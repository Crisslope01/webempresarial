from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class PageListView(ListView):
    model = Page
    
    

class PageDetailView(DetailView):
    model = Page
   