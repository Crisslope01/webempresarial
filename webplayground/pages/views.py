from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
 
 # Si el usuario no es staff, no puede crear páginas asi funciona este mixin y el decorador
@method_decorator(staff_member_required, name='dispatch')
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class PageListView(ListView):
    model = Page
    
class PageDetailView(DetailView):
    model = Page
  
@method_decorator(staff_member_required, name='dispatch')   
class PagesCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages') # reverse_lazy es para que no se ejecute hasta que se ejecute la vista

@method_decorator(staff_member_required, name='dispatch')   
class PagesUpdate(UpdateView):
    model = Page
    template_name_suffix = '_update_form'
    fields = ['title', 'content', 'order']
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
 
@method_decorator(staff_member_required, name='dispatch')   
class PagesDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    
