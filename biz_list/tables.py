import django_tables2 as tables
from django_tables2.utils import A
from .models import About


class CustomerTable(tables.Table):
    name = tables.LinkColumn('name', args=[A('pk')])
    city = tables.LinkColumn('city', args=[A('pk')])
    country = tables.LinkColumn('country', args=[A('pk')])
    email = tables.LinkColumn('email', args=[A('pk')])

    class Meta:
        model = About
        fields = ('name', 'city ',
                  'country', 'country', 'city',
                  'website', 'email')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no customers matching the search criteria..."
