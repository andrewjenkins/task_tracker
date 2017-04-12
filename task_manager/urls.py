from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^group/add$', views.AddGroup.as_view(), name='add_group'),
    url(r'^group/order', views.OrderGroup.as_view(), name="order_group"),
    url(r'^item/add$', views.AddItem.as_view(), name='add_item'),
    url(r'^item/move$', views.MoveItem.as_view(), name='move_item'),
    url(r'^login$', views.Login.as_view(), name='login'),
]