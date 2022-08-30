from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        required=True, 
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Ingrese su nombre complto'}
        ), 
        min_length=1, 
        max_length=100
    )
    phone = forms.CharField(
        label='Teléfono',
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Ingrese su no. de teléfono'}
        ),
    )
    email = forms.EmailField(
        label='Email', 
        required=True, 
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Ingrese su correo electrónico'}
        ), 
        min_length=5, 
        max_length=100
    )
    message = forms.CharField(
        label='Mensaje', 
        required=True, 
        widget=forms.Textarea(
            attrs={'class':'form-control', 'rows':3, 'placeholder':'Ingrese el mensaje que desea mandar a easybroker'}
        ), 
        min_length=5, 
        max_length=1000
    )
        