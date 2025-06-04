

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

![store!](https://github.com/user-attachments/assets/f4879dfa-0064-4789-a16a-11f0be7059d9)

Customer Cart :

![customer cart](https://github.com/user-attachments/assets/8954612a-a1b5-404f-9485-002233336fc8)

Check-out page :

![checkout page](https://github.com/user-attachments/assets/5d669ebb-08a0-42fe-a911-668282fd7b36)

After confrimation :

![order Confrimation!](https://github.com/user-attachments/assets/ccfbd654-99b2-4353-89ec-57fdd00d8c60)


Customer Got Mail : 

![customer got the msG](https://github.com/user-attachments/assets/906cdddb-839d-41bd-8355-7edee3fcc8ed)

Owner GoT mail Too :

![owner got notify about order](https://github.com/user-attachments/assets/e25ad7ed-5bc0-42f9-bb98-36827e1d333e)



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




