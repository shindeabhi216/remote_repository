from django import forms

class InsertingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter product id:",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Product Id',
                'class':'form-control'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter product name:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product name',
                'class': 'form-control'
            }
        )
    )
    product_cost= forms.IntegerField(
        label="Enter product cost:",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter product Class:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Class',
                'class': 'form-control'
            }
        )
    )
    no_of_product = forms.IntegerField(
        label="Enter number of product:",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Number',
                'class': 'form-control'
            }
        )
    )
    y = range(2000,2020)
    manufacture_date= forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="Enter Manufacture Date "
    )
    z= range(2020,2040)
    expiry_date= forms.DateField(
        widget=forms.SelectDateWidget(years=z),
        label="Enter Expiry Date"
    )

    customer_name=forms.CharField(
        label="Enter Customer Name:",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Customer name',
                'class':'form-control'
            }

        )
    )

    mobile = forms.IntegerField(
        label="Enter Mobile No:",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile no.:',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Email Id:",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email Id',
                'class': 'form-control'
            }
        )
    )

class UpdatingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter product id:",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Id',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter product cost:",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )

class DelectingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter product id:",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Id',
                'class': 'form-control'
            }
        )
    )
