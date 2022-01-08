from rest_framework.routers import SimpleRouter
from .views import LoginViewSet, RegistrationViewSet, RefreshViewSet, UserViewSet


routes = SimpleRouter()

routes.register(r'login', LoginViewSet, basename='accounts-login')
routes.register(r'register', RegistrationViewSet, basename='accounts-register')
routes.register(r'refresh', RefreshViewSet, basename='accounts-refresh')

routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls
]