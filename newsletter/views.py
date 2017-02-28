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
	return render(request, "home.html", context)

def contact(request):
	
	form = ContactForm(request.POST or None)

	if form.is_valid():
		for key, value in form.cleaned_data.items():
			print(key, value)
		# email = form.cleaned_data.get('email')
		# message = form.cleaned_data.get('message')
		# full_name = form.cleaned_data.get('full_name')
		# print(full_name, email, message)

	context = {
		'form': form

	}
	return render(request, "forms.html", context)