from rest_framework import routers
from app.views.comment import CommentViewset
from app.views.replies import RepliseViewSet

router = routers.DefaultRouter()
router.register('comment', CommentViewset, basename="comment")
router.register(r'(?P<comment_id>\d+)/replies', RepliseViewSet, basename="replies")

app_url = router.urls