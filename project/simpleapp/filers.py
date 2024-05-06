from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
        empty_label='Любой'
    )
    
    class Meta:
        model = Product
        fields = {
            # поиск по названию
            'name': ['icontains'],
            # кол-во товаров gt - должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равно указанной
                'gt',  # цена должна быть больше или равно указанной
            ],
        }
