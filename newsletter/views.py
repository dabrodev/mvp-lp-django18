from django.shortcuts import render

from .forms import EmailSignUpForm

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