from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from books.models import book
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name= 'all_books'

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
					return redirect('librarian:index')

		return render(request, self.template_name, {'form': form})