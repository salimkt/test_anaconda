from django.contrib.auth.models import User
from register.models import Member, Area, HouseName, Dependent
from rest_framework import serializers
from datetime import datetime


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class HouseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseName
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MemberSerializer(serializers.ModelSerializer):
    dob = serializers.DateField()  # Ensures it's treated as a date

    class Meta:
        model = Member
        fields = ["register_number", "name", "mobile", "dob", "father", "house", "area"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Customizing the output representation for foreign keys
        if instance.dob and isinstance(instance.dob, datetime):
            representation["dob"] = instance.dob.date()

        return representation


class DpndSerializer(serializers.ModelSerializer):
    dob = serializers.DateField()  # Ensures it's treated as a date

    class Meta:
        model = Dependent
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # If the `dob` is a datetime, convert it to a date
        if instance.dob and isinstance(instance.dob, datetime):
            representation["dob"] = instance.dob.date()
        return representation
