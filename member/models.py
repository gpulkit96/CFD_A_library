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
	Dues=models.CharField(max_length=140)
	IssuedBy=models.CharField(max_length=140)
	Status=models.CharField(max_length=140, null=True)
	date=models.DateTimeField()
	books = models.ManyToManyField(Post, null=True)
	Fine = models.IntegerField(default=0)

	def __str__(self):
		allbooks = Post.objects.all()
		books_list = allbooks.filter(memberid__icontains =self.id)
		books = self.books.all()
		for book in books:
				if (datetime.now(pytz.timezone('Asia/Kolkata')) - book.date).days > 14:
					self.Fine += int((datetime.now(pytz.timezone('Asia/Kolkata')) - book.hidden_date).days)
					book.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
				book.memberid = self.id
				book.member_Name =self.Name
				book.date = datetime.now(pytz.timezone('Asia/Kolkata'))
				book.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
				book.save()
				# if self.EmailID=='sshanu@iitk.ac.in':
				# 	email = EmailMessage('Due', book.Title+'is due' ,'sshanu@iitk.ac.in', to=[self.EmailID])
				# 	email.send()


		for book_by_id in books_list:
			for  book in books:
				if (book_by_id.memberid==book.id):
					if book.id == book_by_id.id:
						break
					book_by_id.memberid = None
					book_by_id.member_Name = None
					book_by_id.save()
		self.save()
		return self.Name

	def save(self, *args, **kwargs):
		books = self.books.all()
		for book in books:
			if (book.memberid !=self.id):
				print(book.memberid)
				book.memberid = self.id
				book.member_Name =self.Name
				book.date = datetime.now(pytz.timezone('Asia/Kolkata'))
				book.hidden_date = datetime.now(pytz.timezone('Asia/Kolkata'))
				book.save()	
		super(Member, self).save(*args, **kwargs)
		super(Member, self).save(*args, **kwargs)
