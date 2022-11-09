from rest_framework.views import APIView
from rest_framework import status, response
from .services.expense_stats_generator import ExpenseStatsGenerator
from .services.income_stats_generator import IncomeStatsGenerator


class ExpenseSummaryStats(APIView):

    def get(self, request):

        service = ExpenseStatsGenerator(user=request.user)
        final = service.execute()
        return response.Response({'expense_category_data': final}, status=status.HTTP_200_OK)


class IncomeSourcesSummaryStats(APIView):

    def get(self, request):
        service = IncomeStatsGenerator(user=request.user)
        final = service.execute()
        return response.Response({'income_source_data': final}, status=status.HTTP_200_OK)
