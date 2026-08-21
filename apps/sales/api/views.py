from rest_framework.generics import GenericAPIView
from apps.sales.models import Sales, SalesItem
from apps.sales.api.seraizlier import SalesSerializer, SalesItemSerializer
from rest_framework.response import Response

class SalesView(GenericAPIView):
    queryset = Sales
    serializer_class = SalesSerializer


    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Sales created Successfully"
            })
        else:
            return Response(serializer.errors)

# {
#   "invoice_number": "123",
#   "customer": 1,
#   "sub_total": "50000",
#   "discount": "2000",
#   "tax": "48500",
#   "total": "500",
#   "payment_method": "cash",
#   "sales_item": [
#     {
#       "quantity":2,
#       "unit_price": "25000",
#       "discount": "1000.",
#       "tax": "500",
#       "total": "48500",
#       "medicine": 1,
#       "batch": 12
#     },
 #  {
#       "quantity":2,
#       "unit_price": "25000",
#       "discount": "1000.",
#       "tax": "500",
#       "total": "48500",
#       "medicine": 1,
#       "batch": 12
#     }
#   ]
# }