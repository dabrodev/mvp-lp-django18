from django.contrib import admin

from .models import EmailSignUp
from .forms import EmailSignUpForm

# Register your models here.

class EmailSignUpAdmin(admin.ModelAdmin):
	list_display = ["full_name", "email", "timestamp", "updated"]
	form = EmailSignUpForm
	#class Meta:
	#	model = EmailSignUp

admin.site.register(EmailSignUp, EmailSignUpAdmin)