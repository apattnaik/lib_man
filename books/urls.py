from django.conf.urls import url

from . import views

urlpatterns = [
	
	#/books/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/books/2/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name= 'detail'),

    url(r'register/add/$', views.BookCreate.as_view(), name='books-add'),
    

]