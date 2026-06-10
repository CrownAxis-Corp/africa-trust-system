from django.urls import path, include

urlpatterns = [
    
    path('', include('jobs.urls')),
    path('', include('contracts.urls')),
    path('', include('payments.urls'))
]