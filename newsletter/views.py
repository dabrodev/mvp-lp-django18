from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import EmailSignUpForm, ContactForm

# Create your views here.
def home(request):
	

	form = EmailSignUpForm(request.POST or None)

	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)
		#do some validation
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Sumoling"

		instance.save()

		print(instance.full_name)
		print(instance.email)
		print(instance.timestamp)

	context = {
		"form": form,
	}
	return render(request, "base.html", context)

def contact(request):
	
	form = ContactForm(request.POST or None)

	if form.is_valid():
	#	for key, value in form.cleaned_data.items():
	#		print(key, value)
	
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get('full_name')

		subject = "Site contact form"
		from_email = settings.EMAIL_MAIN
		to_email = [form_email]
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email,
			)
		form_html_message = """
			<h1>Hello</h1>
		"""
		#http://stackoverflow.com/questions/2809547/creating-email-templates-with-django

		send_mail(
		    subject,
		    contact_message,
		    from_email,
		    to_email,
		    html_message=form_html_message,
		    fail_silently=False,
		)	

	context = {
		'form': form

	}
	return render(request, "forms.html", context)