from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from policy.views import PolicyViewSet, EducationViewSet

router = routers.DefaultRouter()
router.register('policy', PolicyViewSet)
router.register('education', EducationViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
