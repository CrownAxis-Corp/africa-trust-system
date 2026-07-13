from rest_framework import viewsets 
from .models import Contract
from .serializer import ContractSerializer
from rest_framework import permissions
from .permissions import IsClientOrContractor

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsClientOrContractor]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    