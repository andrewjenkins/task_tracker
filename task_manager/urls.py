from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^group/add$', views.GroupAdd.as_view(), name='group_add'),
    url(r'^group/order', views.GroupOrder.as_view(), name="group_order"),
    url(r'^group/delete', views.GroupDelete.as_view(), name="group_delete"),
    url(r'^item/add$', views.ItemAdd.as_view(), name='item_add'),
    url(r'^item/move$', views.ItemMove.as_view(), name='item_move'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
]