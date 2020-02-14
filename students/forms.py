from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from students.models import *

class SignUpForm(forms.ModelForm):

    def save(self):
        data = self.data
        print("user created")
        user = User.objects.create(username=data['email'], email=data['email'], is_active=True,
                                   first_name=data['first_name'])
        return user

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')




class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields=['email',"password"]


class Hardware_iot_forms(forms.ModelForm):
  class Meta:
     model=Hardware_iot
     exclude=["student"]

  def save(self,student):
    data=self.cleaned_data

    hwd_iot=Hardware_iot(**data)
    hwd_iot.student=student
    hwd_iot.updated_at=timezone.now()
    hwd_iot.save()


class Ai_form(forms.ModelForm):

  class Meta:
     model=Ai
     exclude = ["student"]

  def save(self,student):
    data=self.cleaned_data
    ai=Ai(**data)
    ai.student=student
    ai.updated_at=timezone.now()
    ai.save()

class Software_form(forms.ModelForm):

  class Meta:
     model=Software
     exclude = ["student"]

  def save(self,student):
    data=self.cleaned_data
    softwate=Software(**data)
    softwate.student=student
    softwate.updated_at=timezone.now()
    softwate.save()


class Product_design_form(forms.ModelForm):
    class Meta:
        model = Product_design
        exclude = ["student"]

    def save(self, student):
        data = self.cleaned_data
        product_design = Product_design(**data)
        product_design.student = student
        product_design.updated_at = timezone.now()
        product_design.save()


class Software_platforms_form(forms.ModelForm):
    class Meta:
        model = Software_platforms
        exclude=["student"]

    def save(self, student):
        data = self.cleaned_data
        software_platform = Software_platforms(**data)
        software_platform.student = student
        software_platform.updated_at = timezone.now()
        software_platform.save()


class Programming_form(forms.ModelForm):
    class Meta:
        model = Programming
        exclude=["student"]

    def save(self, student):
        data = self.cleaned_data
        programing = Programming(**data)
        programing.student = student
        programing.updated_at = timezone.now()
        programing.save()

class Intellectual_Property_form(forms.ModelForm):
    class Meta:
        model = Intellectual_Property
        exclude=["student"]

    def save(self, student):
        data = self.cleaned_data
        ip = Intellectual_Property(**data)
        ip.student = student
        ip.updated_at = timezone.now()
        ip.save()


class Innovation_form(forms.ModelForm):
    class Meta:
        model = Innovation
        exclude=["student"]

    def save(self, student):
        data = self.cleaned_data
        innovation = Innovation(**data)
        innovation.student = student
        innovation.updated_at = timezone.now()
        innovation.save()




