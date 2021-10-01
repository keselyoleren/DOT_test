from rest_framework import (
    generics,
    serializers,
    viewsets,
    status,
    response,
    permissions
)

from rest_framework.response import Response
from app.models import Comment
from django.contrib.auth.models import User
from app.serializers.comment import CommentSerialize
from helper.pagination import ResponsePagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache

class CommentViewset(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerialize
    queryset  = Comment.objects.all()
    pagination_class = ResponsePagination

    def _response(self, request, instance):
        page = self.paginate_queryset(instance)        
        serialize = self.get_paginated_response(
            self.serializer_class(page, many=True, context={"request":request}).data
        )
        response = serialize.data
        return Response(response)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(user=request.user)
        return self._response(request, instance)


    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        instance =self.queryset.filter(id=kwargs['pk']).order_by('-created_at')
        return self._response(request, instance)

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(raise_exception=True):
            comment = Comment()
            comment.message = request.data['message']
            comment.user = request.user
            comment.save()
            instance = Comment.objects.filter(id=comment.id).order_by('-created_at')
            cache.clear()
            return self._response(request, instance)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Comment, id=kwargs['pk'])
        serialize = self.serializer_class(instance, data=request.data, context={"request":request})
        serialize.is_valid(raise_exception=True)
        self.perform_update(serialize)
        cache.clear()
        return self._response(request, self.queryset.filter(id=instance.id).order_by('-created_at'))

    def destroy(self, request, *args, **kwargs):
        generics.get_object_or_404(Comment, id=kwargs['pk'])
        cache.clear()
        return Response({
            "message":"success"
        }, status=status.HTTP_200_OK)


