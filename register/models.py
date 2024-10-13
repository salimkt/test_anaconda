from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import re


def validate_ten_digit_number(value):
    # Ensure the number is exactly 10 digits long
    if not re.fullmatch(r"\d{10}", value):
        raise ValidationError("The phone number must be exactly 10 digits.")


class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class HouseName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    EXPIRE_REASON_CHOICES = [
        ("null", "Null"),
        ("death", "Death"),
        ("transfer", "Transfer"),
    ]

    register_number = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(
        max_length=10, null=True, validators=[validate_ten_digit_number]
    )
    name = models.CharField(max_length=255)
    dob = models.DateField()
    father = models.CharField(max_length=255)
    house = models.ForeignKey(HouseName, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, blank=True)
    active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now, verbose_name="Join Date")
    expire = models.DateField(null=True, blank=True, verbose_name="Expiration Date")
    expire_reason = models.CharField(
        max_length=20,
        choices=EXPIRE_REASON_CHOICES,
        default="null",
        verbose_name="Expiration Reason",
    )

    def __str__(self):
        return self.name


class Dependent(models.Model):
    RELATIONSHIP_CHOICES = [
        ("SPOUSE", "Spouse"),
        ("SON", "Son"),
        ("DAUGHTER", "Daughter"),
        ("DAUGHTER_IN_LAW", "Daughter-in-law"),
    ]
    mobile = models.CharField(
        max_length=10, null=True, validators=[validate_ten_digit_number]
    )
    name = models.CharField(max_length=255)
    dob = models.DateField()
    father = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=3, blank=True)
    active = models.BooleanField(default=True)
    relationship = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_CHOICES,
        default="child",
    )
    parent = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name="Parent Member",
    )

    def __str__(self):
        return self.name
