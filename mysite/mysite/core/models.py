from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='books/pdf')
	cover = models.ImageField(upload_to='books/covers/',null=True,blank=True)

	def __str__(self):
		return self.title

	def delete(self,*args,**kwargs):
		self.pdf.delete()
		self.cover.delete()
		super().delete(*args,**kwargs)