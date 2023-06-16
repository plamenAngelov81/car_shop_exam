from django import forms

from car_shop_exam.web.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password'
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []
