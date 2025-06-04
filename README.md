

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

🏬 Main Store Page

![image alt](https://github.com/RahatVortex98/Ecom/blob/d8d5a93810a1074c8fa59cccc4b93bed62133f89/store!.PNG)




🛒 Customer Cart

![customer cart](https://github.com/user-attachments/assets/af55a4e3-9e6c-4a21-92eb-be14d7f0346b)


✅ Checkout Page

![checkout page](https://github.com/user-attachments/assets/3fd33aa2-d601-4fc4-b8e1-ec2657e8e539)


📧 After Order Confirmation

![order Confrimation!](https://github.com/user-attachments/assets/55ba01a6-97a9-4c73-afe2-c09eff2ea4ba)



📩 Customer Got Email

![customer got the msG](https://github.com/user-attachments/assets/5aecdde7-260b-457c-98ed-302afabacbe5)



🧾 Owner Got Notification

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




