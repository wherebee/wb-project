from django.contrib.auth import forms
from uni_form.helpers import FormHelper, Submit


class AuthenticationForm(forms.AuthenticationForm):

    helper = FormHelper()

    submit = Submit('login', 'Login')
    helper.add_input(submit)
