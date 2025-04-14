from django.urls import path
from .views.views import Start
from .views.viewsTask import *

urlpatterns = [
    path('', TareaList.as_view()),
    path('task/buscar/<int:id>/', TareaBuscar.as_view()),
    path('task/create/', TareaCreate.as_view()),
    path('task/update/<int:id>/', TareaUpdate.as_view()),
    path('task/delete/<int:id>/', TareaDelete.as_view()),
]
