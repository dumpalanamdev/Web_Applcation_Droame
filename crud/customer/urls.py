from django.urls import path
from django.urls.conf import include
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cstmr', views.cstmr),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/int:id>', views.destroy),
    
]