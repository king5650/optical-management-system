# from .models import MedicalReport
from django.contrib import admin
from django import forms




# from django import forms
# from .models import MedicalReport, Lens

# class MedicalReportForm(forms.ModelForm):
#     class Meta:
#         model = MedicalReport
#         fields = [
#             'age', 'sexe', 'profession', 'sphere_od', 'cyl_od', 'axe_od', 'addition_od',
#             'sphere_og', 'cyl_og', 'axe_og', 'addition_og', 'ametropie', 'types_de_verre',
#             'teintes', 'foyers', 'port', 'indice'
#         ]


# admin.site.register(MedicalReport)

# from django import forms
# from .models import Lens

# class LensAdminForm(forms.ModelForm):
#     class Meta:
#         model = Lens
#         fields = '__all__'

#     def clean_lens_type(self):
#         lens_type = self.cleaned_data.get('lens_type')
#         if not lens_type:
#             raise forms.ValidationError("This field is required.")
#         return lens_type


from django import forms
from .models import Lens

# class LensForm(forms.ModelForm):
#     class Meta:
#         model = Lens
#         fields = '__all__'

#     def __str__(self):
#         return f"{self.cleaned_data['lens_type']} - {self.cleaned_data['stock_level']} items available"


from django import forms
from .models import Frame

class FrameForm(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ['frame_type', 'unit_price', 'stock_level']
        labels = {
            'frame_type': 'Frame Type',
            'unit_price': 'Unit Price (USD)',
            'stock_level': 'Number of Items',
        }
        widgets = {
            'frame_type': forms.Select(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Lens

class LensForm(forms.ModelForm):
    class Meta:
        model = Lens
        fields = ['lens_type', 'unit_price', 'stock_level']
        labels = {
            'lens_type': 'Lens Type',
            'unit_price': 'Unit Price (USD)',
            'stock_level': 'Number of Items',
        }
        widgets = {
            'lens_type': forms.Select(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import OpticalAccessory

class OpticalAccessoryForm(forms.ModelForm):
    class Meta:
        model = OpticalAccessory
        fields = ['name', 'unit_price', 'stock_level']

        
        
from django.contrib import admim
admin.site.register(Frame)
admin.site.register(Lens)
admin.site.register(OpticalAccessory)
