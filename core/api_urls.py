from django.urls import path, include

urlpatterns = [
    
    path('', include('job.urls')),
    path('', include('contracts.urls')),
    path('', include('payments.urls'))
]