from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from board import views as board_views


router = routers.DefaultRouter()
router.register(r'postings', board_views.PostingViewSet)
router.register(r'comments', board_views.CommentViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/postings/(?P<pk>\d+)/$', board_views.posting_detail ),
]
