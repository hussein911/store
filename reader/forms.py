from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from reader.models import Account, Reader


class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Account
        fields = ('username', 'email','first_name','last_name','password1','password2','phone','u_type')


class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')

class ReaderForm(ModelForm):
    class Meta:
        model = Reader
        fields = ('preferred_categories','preferred_writers','Adress','u_id')