from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.http import HttpResponse


class ProductListView(ListView):
    model =
    # model = Product
    # template_name = 'products/product_list.html'

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context
    #
    # # def get_context_data(self, **kwargs):
    # #     context = super(ProductListView, self).get_context_data(**kwargs)
    # #     print(context)
    # #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, 'products/product_list.html', context)