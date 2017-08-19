from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from books.models import book
from .forms import UserForm
from .forms import LogForm

class IndexView(generic.ListView):
	template_name = 'librarian/index.html'

	def get_queryset(self):
		return

	

class UserFormView(View):
	form_class = UserForm
	template_name = 'librarian/registration_form.html'

	#dispaly blank form
	def get(self, request):
		form= self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self, request):
		form= self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalised) data
			username= form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct

			user = authenticate(username=username, password= password)
			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('/books/')

		return render(request, self.template_name, {'form': form})
		#success_url = reverse_lazy('index')

class LoginView(View):
	
	form_class = LogForm
	template_name = 'librarian/login_form.html'

	def get(self, request):
		form= self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form= self.form_class(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password= password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/books/')
			else:
				return redirect("Inactive user.")

		return render(request, self.template_name, {'form': form})

class LogoutView(View):
	template_name = 'librarian/logged_out.html'

	def get(self, request):
		logout(request)
		return render(request, self.template_name)
