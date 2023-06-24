from rest_framework import viewsets

from api.serializers import LoanSerializer
from core.models import Loan


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
