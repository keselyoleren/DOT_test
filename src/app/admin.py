from django.contrib import admin
from app.models import Comment, Replies

# Register your models here.
@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'message', 'created_at']
    class Meta:
        model = Comment


@admin.register(Replies)
class RepliesAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'message', 'created_at']
    class Meta:
        model = Replies
    
