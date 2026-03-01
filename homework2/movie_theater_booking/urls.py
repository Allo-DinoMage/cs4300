from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    """
    Admin panel URL.
    """
    path('admin/', admin.site.urls),
    
    """
    Include all the bookings app URLs under the /api/ prefix.
    Example: /api/movies/, /api/seats/, /api/bookings/
    """
    path('api/', include('bookings.urls')),
]
```

Save with `Ctrl+X`, `Y`, `Enter`.

Then run the server to test everything works:
```
python manage.py runserver 0.0.0.0:3000
