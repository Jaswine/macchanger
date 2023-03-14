from django.forms import ModelForm
from .models import CompanySocialMedia

class CompanySocialMediaForm(ModelForm):
   class Meta:
      model = CompanySocialMedia
      fields = '__all__'