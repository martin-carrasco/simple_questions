from rest_framework.routers import SimpleRouter
from .views import ThreadViewSet, PostViewSet, ReplyViewSet 

routes = SimpleRouter()

routes.register(r'thread', ThreadViewSet, basename='api-thread')
routes.register(r'post', PostViewSet, basename='api-post')
routes.register(r'reply', ReplyViewSet, basename='api-reply')

urlpatterns = [
    *routes.urls
]