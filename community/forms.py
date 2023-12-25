from django import forms
from django.forms import ModelForm
from .models import UserPost


from django import forms
from .models import UserPost

class UserPostForm(forms.ModelForm):
    programming_languages = [
        ('c', 'c'),
        ('clike', 'clike'),
        ('cpp', 'cpp'),
        ('csharp', 'csharp'),
        ('css', 'css'),
        ('dart', 'dart'),
        ('django', 'django'),
        ('erlang', 'erlang'),
        ('git', 'git'),
        ('go', 'go'),
        ('java', 'java'),
        ('javascript', 'javascript'),
        ('jsx', 'jsx'),
        ('kotlin', 'kotlin'),
        ('markup', 'markup'),
        ('markup-templating', 'markup-templating'),
        ('objectivec', 'objectivec'),
        ('parser', 'parser'),
        ('perl', 'perl'),
        ('php', 'php'),
        ('powershell', 'powershell'),
        ('python', 'python'),
        ('r', 'r'),
        ('regex', 'regex'),
        ('ruby', 'ruby'),
        ('sql', 'sql'),
        ('swift', 'swift'),
        ('tsx', 'tsx'),
        ('typescript', 'typescript'),
        ('yaml', 'yaml'),
    ]



    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-textarea', 'placeholder': 'Enter your title'})
    )

    code = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control custom-textarea', 'placeholder': 'Enter your code'})
    )

    language = forms.ChoiceField(
        choices=programming_languages,
        widget=forms.Select(attrs={'class': 'form-control custom-select'}),
    )

    class Meta:
        model = UserPost
        fields = ('title', 'code', 'language')

        