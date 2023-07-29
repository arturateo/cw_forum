from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from comments.forms import CreateCommentForm
from comments.models import Comments
from topics.models import Topics


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CreateCommentForm

    def form_valid(self, form):
        comment_author = self.request.user
        topic = get_object_or_404(Topics, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.comment_author = comment_author
        comment.topic = topic
        comment.save()
        return redirect("topics:detail", pk=topic.pk)


class CommentUpdate(PermissionRequiredMixin, UpdateView):
    model = Comments
    form_class = CreateCommentForm
    template_name = "comments/comment_edit.html"
    permission_required = 'comments.change_comments'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().comment_author

    def get_success_url(self):
        return reverse("topics:detail", kwargs={"pk": self.object.topic.pk})


class CommentDelete(PermissionRequiredMixin, DeleteView):
    model = Comments
    template_name = "comments/comment_delete.html"
    context_object_name = 'comment'
    success_url = reverse_lazy("topics:home")
    permission_required = 'comments.delete_comments'

    def has_permission(self):
        print(self.get_object().comment_author)
        return super().has_permission() or self.request.user == self.get_object().comment_author

    def get_success_url(self):
        return reverse("topics:detail", kwargs={"pk": self.object.topic.pk})
