from django import forms

from comments.models import Comments


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['summary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })