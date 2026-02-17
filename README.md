# Custom Auth & RBAC System (Django DRF Junior Test Task)

## 🎯 Features
✅ Custom User model (email login)  
✅ Registration/Login/Logout/Profile/Update/Delete  
✅ Soft delete (is_active=False)  
✅ Session-based authentication (cookies)  
✅ **RBAC permissions system** (CustomRBACPermission)  
✅ Mock business resources (projects/tasks)  
✅ Admin CRUD for roles/permissions  

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
