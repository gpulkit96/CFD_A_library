from catalogue.models import Post
books = Post.objects.all()
for book in books:
	print(book)