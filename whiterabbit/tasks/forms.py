from django import forms
from . import models


class ProjectForm(forms.ModelForm):

    class Meta(object):

        model = models.Project
        fields = [
            'title', 'description', 'url', 'image',
        ]
