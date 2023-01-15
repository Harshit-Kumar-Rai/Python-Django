from django.urls import path
from .views import index, insert_data,  fetch_data, edit_data, update_data, delete_data
urlpatterns = [
    path("", index, name="index"),
    path("insert/",insert_data, name="insert"),
    path('show/', fetch_data, name='fetch_data'),
    path('edit/<int:pk>', edit_data, name='edit'),
    path('update/<int:pk>', update_data, name='update'),
    path('delete/<int:pk>', delete_data, name='delete')
]
