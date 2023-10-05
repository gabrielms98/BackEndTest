from rest_framework.generics import ListAPIView

from .serializers import FinanceSerializer

from .models import Finance


class FinanceView(ListAPIView):
    model = Finance
    serializer_class = FinanceSerializer

    def get_queryset(self):
        symbol = self.request.query_params.get("symbol", None)
        year = self.request.query_params.get("year", None)

        queryset = Finance.objects.filter(repository__symbol=symbol, year=year)

        return queryset
