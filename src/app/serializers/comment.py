from rest_framework import serializers
from app.models import Comment
from app.serializers.user import UserSerialize
from app.models import Replies


class ListReplise(serializers.ModelSerializer):
    user = UserSerialize(many=False, read_only=True)
    class Meta:
        model = Replies
        fields = ("id", 'user',"message")


class CommentSerialize(serializers.ModelSerializer):
    comment = serializers.CharField(required=False)
    user = UserSerialize(many=False, read_only=True)
    replies = ListReplise(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
    