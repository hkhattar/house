


from django.conf.urls import url
from . import views
app_name='house'
urlpatterns=[
		url(r'^$',views.index,name='index'),
		url(r'^login_reg$',views.login_reg,name='login_reg'),
        url(r'^registration$',views.registration,name='register'),
        url(r'^login$',views.login,name='login'),
        url(r'^display$',views.display,name='display'),
        ]
