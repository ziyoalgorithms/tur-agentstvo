from django import forms
from authapp.models import TravelUser
from authapp.forms import TravelUserEditForm
from mainapp.models import ListOfCountries, Accommodation



class TravelUserAdminEditForm(TravelUserEditForm):
    class Meta:
        model = TravelUser
        fields = '__all__'


class ListOfCountriesEditForm(forms.ModelForm):
    class Meta:
        model = ListOfCountries
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'from-cotrol'
            field.help_text = ''




class AccomodationEditForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'


        def __init__(self, *args, **kwargs):
            super(self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
