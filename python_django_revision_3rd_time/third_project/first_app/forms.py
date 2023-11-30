from django import forms

# class contactForm(forms.Form):
#     name = forms.CharField(label="User Name")
#     email = forms.EmailField(label="Email")
#     age = forms.IntegerField()
#     weight = forms.FloatField()
#     balance = forms.DecimalField()
#     check = forms.CheckboxInput()
#     birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'Date'}))
#     appointment = forms.DateTimeInput()
#     CHOICES =[('S','Small'),('M','Medium'),('L','Large')]
#     size = forms.ChoiceField(choices=CHOICES)
#     MEAL = [('P','Pappermoni'),('M','Mashroom'),('B','beef')]
#     pizza = forms.MultipleChoiceField(choices=CHOICES)

class StudentData(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
    def clean_name(self):
        valName = self.cleaned_data['name']
        if len(valName)<10:
            raise forms.ValidationError('Please Enter More than 10 charcter')
        return valName
    