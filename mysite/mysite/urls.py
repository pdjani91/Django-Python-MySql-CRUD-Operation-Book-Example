from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views #6 | go to app/views.py file for  step 7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'), #5 here views.home in 'home' is connect from views.py file def 'home'(req)
    path('signup/',views.signup,name='signup'), # name ='' is refernce for url in base.html file like <a href="{% url 'signup' %}"></a>
    path('secret/',views.secret_page,name='secret'),
    path('secret2/',views.SecratePage.as_view(),name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload/',views.upload,name='upload'), # Here views.upload means defupload connect from view.py
    path('books/',views.book_list,name='book_list'),
    path('books/upload/',views.upload_book,name='upload_book'),
    path('books/<int:pk>/',views.delete_book,name='delete_book'),
    path('class/books/',views.BookListView.as_view(),name ='class_book_list'),
    path('class/books/upload/',views.UploadBookView.as_view(),name ='class_upload_book'),
]

if settings.DEBUG: # Only during development pupose
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


