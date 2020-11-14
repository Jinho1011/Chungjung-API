from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from policy.views import PolicyViewSet, EducationViewSet, StateViewSet

router = routers.DefaultRouter()
router.register('policy', PolicyViewSet)
router.register('education', EducationViewSet)
router.register('state', StateViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
