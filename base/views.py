from .forms import ContactForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


class UserLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class ListOfTask(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user_name=self.request.user)

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(
                task_title__contains=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'taskname'
    template_name = 'base/task.html'


class CreateATask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_title', 'task_desc', 'task_status']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super(CreateATask, self).form_valid(form)


class UpdateTheTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteATask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'taskname'
    success_url = reverse_lazy('tasks')


def contact_view(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'base/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'base/contactus.html', context)


def checklist_view(request):
    return render(request, 'base/checklist.html')


def site_view(request):
    return render(request, 'base/site.html')


def about_view(request):
    return render(request, 'base/aboutus.html')


def home_view(request):
    return render(request, 'base/home.html')
