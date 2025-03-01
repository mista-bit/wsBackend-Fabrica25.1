from django import forms

class CurrencyExchangeForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    moeda_de_origem = forms.CharField(max_length=3, label='Moeda de Origem')
    moeda_destino = forms.CharField(max_length=3, label='Moeda Destino')
    valor_de_origem = forms.DecimalField(max_digits=10, decimal_places=2, label='Valor de Origem')
    valor_destino = forms.DecimalField(max_digits=10, decimal_places=2, label='Valor Destino')
    data = forms.DateField(label='Data', widget=forms.SelectDateWidget)
