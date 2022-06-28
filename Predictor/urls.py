from django.urls import URLPattern, path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Prediction', views.ApprovalsView)
urlpatterns = [
    #path('/', views.Predictor, name='predictor'),
    path('form/', views.MyForm, name = 'myform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]