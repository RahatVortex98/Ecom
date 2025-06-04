from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.conf import settings




from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core.mail import send_mail
from django.contrib import messages


from .models import *


class Store(ListView):
    template_name = 'store.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'
    


class OrderConfirmationView(TemplateView):
    template_name = 'order_confirmation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_id = self.request.session.get('order_id')

        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                context['order'] = order
                context['items'] = order.orderitem_set.all()
                context['message'] = "Thank you for your purchase!"
            except Order.DoesNotExist:
                context['order'] = None
                context['items'] = []
                context['message'] = "Order not found."
        else:
            context['order'] = None
            context['items'] = []
            context['message'] = "No order found."

        return context

    


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0} #Non logged in user!

        context['items'] = items
        context['order'] = order
        return context
    





class CheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {'items': items, 'order': order}
        return render(request, 'checkout.html', context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        # Save shipping info
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode
        )

        # Mark order as complete
        order.complete = True
        order.save()

        # Email to customer
        subject_customer = "Your order has been accepted!"
        message_customer = (
            f"Hi {customer.name},\n\n"
            "Thank you for your order. We have received your order with the following details:\n\n"
            f"Order ID: {order.id}\n"
            f"Shipping Address: {address}, {city}, {state} ({zipcode})\n"
            f"Total Amount: ৳ {order.get_cart_total:.2f}\n\n"
            "We will process your order and send updates via email.\n\n"
            "Thank you for shopping with us!"
        )
        send_mail(
            subject_customer,
            message_customer,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        # Email to owner/admin
        subject_admin = f"New Order #{order.id} from {customer.name}"
        message_admin = (
            f"New order received.\n\n"
            f"Customer: {customer.name}\n"
            f"Email: {email}\n"
            f"Shipping Address: {address}, {city}, {state} ({zipcode})\n"
            f"Order Total: ৳ {order.get_cart_total:.2f}\n"
            f"Order Items:\n"
        )
        for item in order.orderitem_set.all():
            message_admin += f"- {item.product.name} x {item.quantity}\n"

        send_mail(
            subject_admin,
            message_admin,
            settings.DEFAULT_FROM_EMAIL,
            ['r072islam@gmail.com'],  # Your email as the owner/admin
            fail_silently=False,
        )

        context = {
            'message': "Your order has been accepted! Thank you for shopping with us.",
            'order': order,
            'items': order.orderitem_set.all()
        }

        return render(request, 'order_confirmation.html', context)





      



class AddToCartView(View):
    def get(self, request, product_id):
        if not request.user.is_authenticated:
            return redirect('login')

        product = get_object_or_404(Product, id=product_id)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity += 1
        order_item.save()

        return redirect('cart')




@method_decorator(csrf_exempt, name='dispatch')
class UpdateCartView(View):
    def post(self, request):
        data = json.loads(request.body)
        product_id = data['productId']
        action = data['action']

        customer = request.user.customer
        product = Product.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            order_item.quantity += 1
        elif action == 'remove':
            order_item.quantity -= 1
        elif action == 'delete':
            order_item.delete()
            return JsonResponse('Item deleted', safe=False)

        if order_item.quantity <= 0 and action != 'delete':
            order_item.delete()
        else:
            order_item.save()

        return JsonResponse('Cart updated', safe=False)
