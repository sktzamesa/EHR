from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'register-name',
            'placeholder': 'Enter your full name',
            'autocomplete': 'name',
            'class': 'form-group'
        })
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'register-username',
            'placeholder': 'Enter your username',
            'autocomplete': 'username',
            'class': 'form-group'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'register-email',
            'placeholder': 'Enter your email',
            'autocomplete': 'username',
            'class': 'form-group'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'register-password',
            'placeholder': 'Create a password',
            'autocomplete': 'new-password',
            'class': 'form-group'
        })
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'register-confirm-password',
            'placeholder': 'Confirm your password',
            'autocomplete': 'new-password',
            'class': 'form-group'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')