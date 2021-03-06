from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^board/order$', views.BoardOrder.as_view(), name='board_order'),
    url(r'^group/add$', views.GroupAdd.as_view(), name='group_add'),
    url(r'^group/order$', views.GroupOrder.as_view(), name="group_order"),
    url(r'^group/delete$', views.GroupDelete.as_view(), name="group_delete"),
    url(r'^item/add$', views.ItemAdd.as_view(), name='item_add'),
    url(r'^item/move$', views.ItemMove.as_view(), name='item_move'),
    url(r'^item/delete$', views.ItemDelete.as_view(), name='item_delete'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^register', views.Register.as_view(), name='register'),
]