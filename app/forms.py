from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            'Item_Identifier',
        'Item_Weight',
        'Item_Fat_Content',
        'Item_Visibility',
        'Item_Type',
        'Item_MRP',
        'Outlet_Identifier',
        'Outlet_Establishment_Year',
        'Outlet_Location_Type',
        'Outlet_Type',
        'Item_Outlet_Sales',
        'source',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
