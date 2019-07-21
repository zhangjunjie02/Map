
from django.conf.urls import url,include


urlpatterns = [
    url(r'^map_api/', include('Map_api.urls')),

]
