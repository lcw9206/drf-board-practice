from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from board.views import PostingViewSet


router = routers.DefaultRouter()
router.register(r'postings', PostingViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'))
]
