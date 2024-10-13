from register.models import Member, Area, HouseName, Dependent
from rest_framework import generics
from .serializers import (
    MemberSerializer,
    UserSerializer,
    AreaSerializer,
    HouseNameSerializer,
    DpndSerializer,
)
from rest_framework.permissions import AllowAny


# Area Views
class AreaListCreateView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


# HouseName Views
class HouseNameListCreateView(generics.ListCreateAPIView):
    queryset = HouseName.objects.all()
    serializer_class = HouseNameSerializer


class HouseNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseName.objects.all()
    serializer_class = HouseNameSerializer


# Member view
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = "register_number"


# Dependent view
class DpndListCreateView(generics.ListCreateAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DpndSerializer


class DpndUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DpndSerializer


# User PAUSE for now
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
