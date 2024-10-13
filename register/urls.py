from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    # User and Authentication
    path("register/", UserCreate.as_view(), name="user_create"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # Area
    path("areas/", AreaListCreateView.as_view(), name="area-list"),
    path("areas/<int:pk>/", AreaDetailView.as_view(), name="area-detail"),
    # House
    path("house-names/", HouseNameListCreateView.as_view(), name="house-name-list"),
    path(
        "house-names/<int:pk>/", HouseNameDetailView.as_view(), name="house-name-detail"
    ),
    # Member URLS
    path("member/", MemberListCreateView.as_view(), name="member-list-create"),
    path(
        "member/<str:register_number>/",
        MemberUpdateView.as_view(),
        name="member-update",
    ),
    # Dpnd URLS
    path("dpnd/", DpndListCreateView.as_view(), name="dpnd-list-create"),
    path(
        "dpnd/<str:register_number>/",
        DpndUpdateView.as_view(),
        name="dpnd-update",
    ),
]
