# -*- coding: utf-8 -*-
from __future__                 import unicode_literals

from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils               import timezone
from django.shortcuts           import render, redirect
from django.views.generic.edit  import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models                    import Table
from.forms                      import TableForm
from django.urls                import reverse_lazy
# Create your views here.
class createTable(LoginRequiredMixin, CreateView):
    model = Table
    fields = ['name', 'description', 'city']
    template_name = 'table_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = timezone.now()
        form.instance.last_modified = timezone.now()
        return super(createTable, self).form_valid(form)
    
class editTable(LoginRequiredMixin, UpdateView):
    model = Table
    field = ['name', 'description', 'city']
    template_name = 'table_form.html'

class deleteTable(LoginRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('table_list')

#@login_required
def tables(request):
    table_list = Table.objects.all()
    args ={'table_list':table_list}
    return render(request,'table_list.html', args)

def table(request, table_name):
    table = Table.objects.get(unique_name=table_name)
    args ={'table':table}
    return render(request,'table.html', args)

def error(request):
    return render(request, 'error.html')
