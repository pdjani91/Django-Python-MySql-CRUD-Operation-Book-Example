from django.shortcuts import render,redirect
from django.contrib.auth.models import User # Import User name which register in as a signup
from django.contrib.auth.forms import UserCreationForm # Here UserCreationForm is automatic functionality by django
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .forms import Book
from django.contrib import messages

def home(request): #7
	count = User.objects.count()
	return render(request,'home.html',{'count':count}) #8 and after create home.html file in templates folder

def signup(request):
	if request.method == 'POST': #<-----------------------------Logic handling the post request
		form = UserCreationForm(request.POST) #<------------That is data
		if form.is_valid():
			form.save()
			return redirect('home')
	else: #<-----------------------------------------------and the get request
		form = UserCreationForm
	return render(request,'registration/signup.html',{'form':form})

@login_required #Its decorators
def secret_page(request):
	return render(request,'secret_page.html')

class SecratePage(LoginRequiredMixin, TemplateView):
	template_name = 'secret_page.html'

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document'] #here FILES['document'] is connected from upload.html (name="document")
		# print(uploaded_file.name)
		# print(uploaded_file.size)

		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name,uploaded_file)
		context ['url'] = fs.url(name)
	return render(request,'upload.html',context)

def book_list(request):
	books = Book.objects.all()
	return render(request,'book_list.html',{
		'books': books
		})

def upload_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST,request.FILES) #request.POST = geting title/auth request.FILES = for book upload
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"You have uploaded successfully.")
			return redirect('book_list')
	else:
		form = BookForm()
	return render(request,'upload_book.html',{
		'form' : form
		})

class BookListView(ListView): #Generic Class Based Views
	model = Book
	template_name = 'class_book_list.html'
	context_object_name = 'books'

class UploadBookView(CreateView):
	model = Book
	form_class = BookForm
	# fields = ('title','author','pdf','cover')
	success_url = reverse_lazy('class_book_list')
	template_name = 'upload_book.html'

def delete_book(request,pk): # pk = primary key
	if request.method == 'POST':
		book = Book.objects.get(pk=pk)
		book.delete()
	return redirect('book_list')