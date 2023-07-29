from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from accounts.forms import CustomRegisterForm
from accounts.models import User
from topics.models import Topics


# from topics.models import Topics


# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = CustomRegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('topics:home')
        return next_url


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = User
    context_object_name = 'profile_user'
    paginate_related_by = 10

    def get_context_data(self, **kwargs):
        topics = self.object.author.order_by('-create_date')
        paginator = Paginator(topics, self.paginate_related_by)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['topics'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)
