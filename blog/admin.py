from django.contrib import admin
from blog.models import Post,Category, Comment
# Register your models here.
# superuser username : Jennifer
#email - jennifer@example.com
#password: july3007

class PostAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)

