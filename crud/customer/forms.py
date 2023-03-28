from django.forms import fields
from customer.models import Customer

class CustomerForm(forms.modelForm):
    class meta:
        model=Customer
        fields="__all__"