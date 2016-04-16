from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^users/$', views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UsersDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

