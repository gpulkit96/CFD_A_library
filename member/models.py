from django.db import models
from catalogue.models import Post
from datetime import datetime, timedelta
import pytz
from django.core.mail import EmailMessage

class Member(models.Model):
	Name=models.CharField(max_length=140)
	RollNo=models.CharField(max_length=140)
	EmailID=models.CharField(max_length=140)
	Slots=models.CharField(max_length=140)
	IssuedBy=models.CharField(max_length=140)
	Fine = models.IntegerField(default=0)
	books = models.ManyToManyField(Post, null=True, blank=True)
	date = models.DateTimeField()
	hidden_date = models.DateTimeField(editable=False, null=True)

	def __str__(self):
		books_list = Post.objects.filter(memberid=self.id)
		books = self.books.all()
		if (datetime.now(pytz.timezone('Asia/Kolkata')) - self.hidden_date).days >1:
			
			for book in books:
					if (datetime.now(pytz.timezone('Asia/Kolkata')) - book.date).days >14:
						if (self.EmailID=='sshanu@iitk.ac.in')and(book.duestatus == 0):
							email = EmailMessage('Due', book.Title+'is due', to=[self.EmailID])
							# for iitk mail
							# email = EmailMessage('Due', book.Title+'is due' ,'sshanu@iitk.ac.in', to=[self.EmailID])  
							email.send()
							book.duestatus = 1
						self.Fine += int((datetime.now(pytz.timezone('Asia/Kolkata')) - book.hidden_date).days)
						book.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
					book.save()
			self.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
			self.save()

		for book_by_id in books_list:
			if(len(books)!=0):
				for  book in books:
					if book.id == book_by_id.id:
						break
					book_by_id.memberid = None
					book_by_id.member_Name = None
					book_by_id.duestatus = 0
					book_by_id.save()
			else:
				book_by_id.memberid = None
				book_by_id.member_Name = None
				book_by_id.duestatus = 0
				book_by_id.save()
		
		return self.Name

	def save(self, *args, **kwargs):
		if not self.pk:
			self.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
		else:
			books = self.books.all()
			for book in books:
				if (book.memberid !=self.id):
					book.memberid = self.id
					book.member_Name =self.Name
					book.date = datetime.now(pytz.timezone('Asia/Kolkata'))
					book.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
					book.save()	
		super(Member, self).save(*args, **kwargs)
		super(Member, self).save(*args, **kwargs)
		
