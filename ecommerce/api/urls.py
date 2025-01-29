from rest_framework.routers import DefaultRouter
from .views import ProductViewset,OrderViewset,SignupView,LoginView
from django.urls import path,include
router=DefaultRouter()
router.register(r'products',ProductViewset)
router.register(r'orders',OrderViewset)

urlpatterns=[
    path("",include(router.urls)),
    path('signup/',SignupView.as_view()),
    path('login/',LoginView.as_view())
]