import django_filters
from .models import About


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = About
        fields = ['name', 'country', 'city', 'category', ]
