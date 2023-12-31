from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from comments.forms import CreateCommentForm
from topics.forms.search_form import SearchForm
from topics.forms.topics_form import TopicsForm
from topics.models import Topics
from django.urls import reverse, reverse_lazy


# Create your views here.
class TopicsList(ListView):
    model = Topics
    template_name = 'topics/topics_list.html'
    context_object_name = 'topics'
    paginate_by = 10
    page_kwarg = 'page'
    ordering = ("-create_date",)

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topics
    form_class = TopicsForm
    template_name = 'topics/topic_create.html'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.author = self.request.user
        topic.save()
        return redirect("topics:detail", pk=topic.pk)

    def get_success_url(self):
        return reverse("topics:detail", kwargs={"pk": self.object.pk})


class TopicUpdate(PermissionRequiredMixin, UpdateView):
    model = Topics
    form_class = TopicsForm
    template_name = "topics/topic_edit.html"
    permission_required = 'topics.change_topics'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("topics:detail", kwargs={"pk": self.object.pk})


class TopicDelete(PermissionRequiredMixin, DeleteView):
    model = Topics
    template_name = "topics/topic_delete.html"
    context_object_name = 'topic'
    success_url = reverse_lazy("topics:home")
    permission_required = 'topics.delete_topics'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class TopicDetail(DetailView):
    model = Topics
    template_name = 'topics/topic_detail.html'
    context_object_name = 'topic'
    paginate_related_by = 3

    def get_context_data(self, **kwargs):
        comments = self.object.comment_topic.order_by('create_date')
        paginator = Paginator(comments, self.paginate_related_by)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['comments'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        kwargs['form'] = CreateCommentForm
        return super().get_context_data(**kwargs)
