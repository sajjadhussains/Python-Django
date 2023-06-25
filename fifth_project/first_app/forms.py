from django import forms 
from django.core import validators

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

def check_len(value):
    if len(value)<10:
        raise forms.ValidationError("Enter at least 10 charcters")
    
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,"Enter minimum 10 characters")])
    text = forms.CharField(widget=forms.TextInput,validators=[check_len])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message="maximum age can be 34"),validators.MinValueValidator(24,message="Minimum value can be 24")])
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Enter .com for valid email")
    #     else:
    #         return valemail
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
        
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your Email Must Contain .com")


class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        # Perform password validation here
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        # Perform confirm_password validation here
        return confirm_password

    def clean_name(self):
        name = self.cleaned_data['name']
        # Perform name validation here
        return name

    def clean(self):
        cleaned_data = super().clean()
        val_pass = cleaned_data.get('password')
        val_con_pass = cleaned_data.get('confirm_password')
        val_name = cleaned_data.get('name')

        if val_con_pass and val_pass and val_con_pass != val_pass:
            raise forms.ValidationError("Passwords didn't match")
        if val_name and len(val_name) < 15:
            raise forms.ValidationError("Name should be at least 15 characters")
