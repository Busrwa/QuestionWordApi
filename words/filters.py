import django_filters
from .models import Word
from django.db.models import Q

class WordFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    level = django_filters.CharFilter(field_name='level')

    class Meta:
        model = Word
        fields = ['level']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(turkish_word__icontains=value) |
            Q(english_word__icontains=value)
        )
