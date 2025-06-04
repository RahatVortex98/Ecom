

# 🛒 Django eCommerce Web App

This is a modern eCommerce web application built with **Django**, featuring a dynamic shopping cart, product catalog, and class-based views for order management.

---

## 🚀 Features

- 🔒 User Authentication (Login/Logout)
- 🛍️ Product listing with prices and images
- ➕ Add-to-cart functionality via AJAX
- 🔄 Increase/Decrease quantity from cart page (AJAX)
- ❌ Remove item from cart (AJAX)
- 📦 Cart summary with total quantity and subtotal
- ✅ Checkout button (view only)

---

## 🧠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5, Bootstrap Icons
- **Database:** PostgreSQL (or SQLite for local dev)
- **AJAX:** Vanilla JavaScript + Fetch API
- **Admin Panel:** Django Admin

---

## 📁 Project Structure
ecommerce_project/
│
├── ecommerce/ # Main Django project
│ ├── settings.py
│ └── urls.py
│
├── store/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── cart.html
│ │ ├── store.html
│ │ └── main.html
│ └── static/ # Static files (CSS, JS, images)
│
└── manage.py


---

## 🧾 Models Overview

### Product

```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    @property
    def imageUrl(self):
        try:
            return self.image.url
        except:
            return ''

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        return sum(item.get_total for item in self.orderitem_set.all())

    @property
    def get_cart_items(self):
        return sum(item.quantity for item in self.orderitem_set.all())

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):
        return self.product.price * self.quantity

from django.urls import path
from .views import AddToCartView, CartView,CheckoutView, OrderConfirmationView,Store,ProductDetail, UpdateCartView

urlpatterns = [
    
    path('',Store.as_view(),name='store'),
    path('cart/',CartView.as_view(),name='cart'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('detail/<int:pk>/',ProductDetail.as_view(),name='detail'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('update-cart/', UpdateCartView.as_view(), name='update_cart'),
    path('order-confirmation/', OrderConfirmationView.as_view(), name='order_confirmation'),
]

<script>
document.querySelectorAll('.update-cart').forEach(button => {
    button.addEventListener('click', function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;

        fetch("{% url 'update_cart' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ productId: productId, action: action })
        })
        .then(response => response.json())
        .then(data => location.reload());
    });
});
</script>

How to Run Locally
git clone https://github.com/RahatVortex98/django-ecommerce.git
cd django-ecommerce

Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run migrations
python manage.py makemigrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Start development server
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.


📷 Screenshots

Main Page :Store


![store!](https://github.com/user-attachments/assets/9875b32c-aaa5-409c-93d7-2558ea6e1804)


Customer Cart :

![customer cart](https://github.com/user-attachments/assets/af55a4e3-9e6c-4a21-92eb-be14d7f0346b)


Check-out page :

![checkout page](https://github.com/user-attachments/assets/3fd33aa2-d601-4fc4-b8e1-ec2657e8e539)


After confrimation :

![order Confrimation!](https://github.com/user-attachments/assets/55ba01a6-97a9-4c73-afe2-c09eff2ea4ba)



Customer Got Mail :

![customer got the msG](https://github.com/user-attachments/assets/5aecdde7-260b-457c-98ed-302afabacbe5)



Owner GoT mail Too :

![owner got notify about order](https://github.com/user-attachments/assets/7d3a84f9-7488-4437-8e99-187a3cbe1b40)




🙌 Credits
Built with ❤️ using Django.
Author: RahatVortex98



📄 License

---

✅ You can now **copy and paste this directly into your `README.md`** file on GitHub. Let me know if you'd like me to:

- Add screenshots
- Include deployment steps (e.g., PythonAnywhere)
- Provide a `.env` configuration guide
- Include a Stripe or bKash integration section

I'm here to help make this project ready for production or portfolio showcase.




