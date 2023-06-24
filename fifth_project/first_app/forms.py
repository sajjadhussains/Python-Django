from django import forms 

class contactForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField()
    appointment = forms.DateTimeField()
    CHOICES=[('S','small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES)
    MEAL=[('P','Pappermoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL)
