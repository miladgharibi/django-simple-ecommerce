from django.shortcuts import render
from django.views.generic import View
from product.models import ProductModel

class HomeView(View):
    def get(self, request):
        model = ProductModel.objects.all()[ProductModel.objects.count() - 4:ProductModel.objects.count()]
        context = {'products': model}
        return render(request, 'core/index.html', context)