from urllib.parse import urlencode

from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView

# from comments.models import Comments
# from topics.forms.publications_form import PublicationsForm
from topics.forms.search_form import SearchForm
from topics.models import Topics
from django.urls import reverse, reverse_lazy


# Create your views here.
class TopicsList(ListView):
    model = Topics
    template_name = 'topics/topics_list.html'
    context_object_name = 'topics'
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
        # if self.search_value:
        #     queryset = queryset.filter(author__icontains=self.search_value)
        return queryset
