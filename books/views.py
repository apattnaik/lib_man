from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import book

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name= 'all_books'
	
	def get_queryset(self):
		return book.objects.all()

class DetailView(generic.DetailView):
	model=  book
	template_name= 'books/detail.html'


class BookCreate(CreateView):
	model= book
	fields = ['name', 'author', 'category', 'publisher', 'published_date']
