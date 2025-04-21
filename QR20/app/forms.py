from django import forms

class QRCodeForm(forms.Form):
    data = forms.CharField(label='Данные для QR-кода', max_length=200)
