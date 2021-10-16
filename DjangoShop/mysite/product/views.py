from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import ProductModel, Order, OrderProduct
from django.shortcuts import redirect

class ProductList(ListView):
    model = ProductModel
    template_name = 'product/product_list.html'


class ProductDetail(View):
    def get(self, request, product_id):
        model = get_object_or_404(ProductModel, pk=product_id)
        context = {
            'product': model
        }
        return render(request,'product/product_detail.html', context)


class Cart(View):
    def get(self, request):
        model = Order.objects.get(user=request.user, ordered=False)
        context = {
            'item_list': model.orders.all(),
            'total': model.get_total
        }
        return render(request, 'product/cart.html', context)


def addToCart(request, product_id):
    product              = get_object_or_404(ProductModel, pk=product_id)
    order_item, create   = OrderProduct.objects.get_or_create(user=request.user, product=product, ordered=False)
    order_qs             = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orders.filter(product__pk=product_id).exists():
            if request.method == "POST":
                quantity = int(request.POST['quantity'])
                order_item.quantity += quantity
                order_item.save()
            else:
                order_item.quantity += 1
                order_item.save()

        else:
            if request.method == "POST":
                quantity = int(request.POST['quantity'])
                order.orders.add(order_item)
                order_item.quantity = quantity
                order_item.save()

        return redirect('product:cart')

    else:
        if request.method == "POST":
            quantity = int(request.POST['quantity'])
            cart = Order.objects.create(user=request.user, ordered=False)
            cart.orders.add(order_item)
            order_item.quantity = quantity
            order_item.save()
        
    return HttpResponse("Added")

def removeFromCart(request, product_id):
    if request.method == "GET":
        product              = get_object_or_404(ProductModel, pk=product_id)
        order_item           = get_object_or_404(OrderProduct,user=request.user, product=product, ordered=False)
        order_qs             = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.orders.filter(product__pk=product_id).exists():
                if order.orders.filter(product__pk=product_id)[0].quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                
                else :
                    order_item.delete()

            return redirect('product:cart')


