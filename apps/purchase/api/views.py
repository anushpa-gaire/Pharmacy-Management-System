from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.purchase.api.serializer import (
    PurchaseItemSerializer,
    PurchaseSerializer,
)
from apps.purchase.models import Purchase, PurchaseItem
from rest_framework.decorators import api_view
from apps.medicine.api.service import create_medicine_batch
from datetime import datetime
class PurchaseView(GenericAPIView):
    queryset = Purchase
    serializer_class = PurchaseSerializer

    def get(self, request, *args, **kwargs):
        data = Purchase.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Purchase has been created successfully",
            })

        return Response(serializer.errors)


class UpdatePurchaseView(GenericAPIView):
    queryset = Purchase
    serializer_class = PurchaseSerializer

    def get(self, request, id):
        data = get_object_or_404(Purchase, id=id)
        serializer = self.get_serializer(data)

        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(Purchase, id=id)
        serializer = self.get_serializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Purchase updated successfully"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        data = get_object_or_404(Purchase, id=id)
        data.delete()

        return Response(
            {
                "message": "Purchase deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )



# {
#     "purchase":"1",
#     "items":[
#         {
#            " purchase item"
#         },
#         {

#         }
#     ]
# }

@api_view(['GET'])
def verify_purchase(request, id):
    purchase = get_object_or_404(Purchase, id=id)
    if purchase.is_purchase_verified:
        return Response({
            "message":"Purchase is already verified, please contact admin"
        },status.HTTP_400_BAD_REQUEST)
    else:
        purchase_item = PurchaseItem.objects.filter(purchase=purchase)
        for item in purchase_item:
            create_medicine_batch(
                medicine=item.medicine,
                batch_number = item.id ,
                manufacturing_date = item.manufacturing_date,
                quantity = item.quantity,
                supplier = purchase.supplier,
                expiry_date = item.expiry_date,
                purchase_price = item.unit_price,
                selling_price = (35/100)* float(item.unit_price) + float(item.unit_price),
                received_date = str(datetime.now().date())
            )
        purchase.is_purchase_verified = True
        purchase.save()

        return Response({
            "message":"Purchase is verified"
        })