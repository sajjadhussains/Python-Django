from django import forms 

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label='User Name',initial='Rahim',help_text="total character must be at least 70 characters",required=False,widget=forms.Textarea)
    # file = forms.FileField()
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'Date'}))
    # appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # if DateField is not remembered then charField can use
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'Date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL=[('P','Pappermoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
