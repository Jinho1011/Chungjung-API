from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from policy.views import PolicyViewSet

router = routers.DefaultRouter()
router.register('policy', PolicyViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
