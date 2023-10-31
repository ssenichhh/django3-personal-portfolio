from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Project, ContactMessage
from .forms import HomeForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    template_name = 'portfolio/homenew.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        form = HomeForm()
        submitted = 'submitted' in request.GET
        context = {
            'projects': projects,
            'form': form,
            'submitted': submitted
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
        projects = Project.objects.all()
        context = {
            'projects': projects,
            'form': form,
        }
        return render(request, self.template_name, context)
