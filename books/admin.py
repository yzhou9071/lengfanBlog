from django.contrib import admin
from models import BookDetail

class BookDetailAdmin(admin.ModelAdmin):
	list_display = ('bookName', 'bookTime',)
	search_fields = ('bookName', 'bookStar', 'bookState',)
	fieldsets = (
			(
				None,
				{
					'fields': ('bookName', 'bookAuthor', 'bookProduct', 'bookDes', 'bookStar', 'bookState', 'bookFlag', 'bookHref',)
				}
			),
	)

admin.site.register(BookDetail, BookDetailAdmin)
