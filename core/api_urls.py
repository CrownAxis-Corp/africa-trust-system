from django.urls import path, include

urlpatterns = [
    
    path('', include('jobs.urls')),
    path('', include('contracts.urls')),
    path('', include('payments.urls')),
    path('', include('trust.urls')),
    path('', include('disputes.urls')),
    path('', include('users.urls')),
    
]