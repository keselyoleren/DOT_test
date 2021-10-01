from os import replace
from rest_framework import (
    generics,
    serializers,
    viewsets,
    status,
    response,
    permissions
)
from app.models import Replies
from django.contrib.auth.models import User
from app.serializers.replies import RepliesSerialize
from helper.pagination import ResponsePagination
from rest_framework.response import Response

from app.models import Comment

class RepliseViewSet(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RepliesSerialize
    queryset  = Replies.objects.all()
    pagination_class = ResponsePagination

    def _response(self, request, instance):
        page = self.paginate_queryset(instance)        
        serialize = self.get_paginated_response(
            self.serializer_class(page, many=True, context={"request":request}).data
        )
        response = serialize.data
        return Response(response)

    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(user=request.user)
        return self._response(request, instance)

    def retrieve(self, request, *args, **kwargs):
        instance =self.queryset.filter(id=kwargs['pk']).order_by('-created_at')
        return self._response(request, instance)

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(raise_exception=True):
            replies = Replies()
            replies.message = request.data['message']
            replies.user = request.user
            replies.comment = Comment.objects.get(id=request.data['comment_id'])
            replies.save()
            instance = Replies.objects.filter(id=replies.id).order_by('-created_at')
            return self._response(request, instance)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Replies, id=kwargs['pk'])
        serialize = self.serializer_class(instance, data=request.data, context={"request":request})
        serialize.is_valid(raise_exception=True)
        self.perform_update(serialize)
        return self._response(request, self.queryset.filter(id=instance.id).order_by('-created_at'))

    def destroy(self, request, *args, **kwargs):
        generics.get_object_or_404(Replies, id=kwargs['pk'])
        return Response({
            "message":"success"
        }, status=status.HTTP_200_OK)


        