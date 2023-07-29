from django import forms
from topics.models import Topics


class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['summary', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })