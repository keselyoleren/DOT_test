from django.db.models.fields import CharField
from rest_framework import serializers
from app.models import Replies
from app.serializers.user import UserSerialize
from app.serializers.comment import CommentSerialize

class RepliesSerialize(serializers.ModelSerializer):
    comment = CommentSerialize(many=False, read_only=True)
    user = UserSerialize(many=False, read_only=True)
    message = serializers.CharField(required=False)
    
    
    class Meta:
        model = Replies
        fields = "__all__"
