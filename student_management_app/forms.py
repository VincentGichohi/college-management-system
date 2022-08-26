
from django import forms
from django.forms.widgets import DateInput, TextInput

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'




