from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save(self):
        question = Question(**self.cleaned_data)
        aid = self._user.id
        if aid is None:
            aid = 1
        question.author_id = aid # TODO hardcoded for now
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label='Your answer', widget=forms.Textarea(attrs={'class': 'form-control'}))
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question = self.cleaned_data['question']
        try:
            if int(question) < 1:
                raise ValueError
            question = Question.objects.get(id=question)
        except (Question.DoesNotExist, ValueError):
            raise ValidationError(u'Incorrect question ID', code='qid_error')

        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        aid = self._user.id
        if aid is None:
            aid = 2
        answer.author_id = aid # TODO hardcoded for now
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(u'Invalid username or password', code='login_failed')
        return self.cleaned_data

    def login(self):
        user = authenticate(**self.cleaned_data)
        return user


