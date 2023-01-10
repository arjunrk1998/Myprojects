from . import views
from django.urls import path
urlpatterns=[
    path('',views.myfun,name='myfun'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('view/',views.myview.as_view(),name='view'),
    path('dv/<int:pk>/',views.taskdetailview.as_view(),name='dv'),
    path('dupdate/<int:pk>/',views.Taskupdateview.as_view(),name='dupdate'),
    path('delete/int:pk>/',views.deletes.as_view(),name='delete'),
]