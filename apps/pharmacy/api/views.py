from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.pharmacy.api.serializer import PharmacySerializer

from django.shortcuts import get_object_or_404

from apps.pharmacy.models import Pharmacy
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.pharmacy.api.service import AccessCha


class PharmacyView(GenericAPIView):
    queryset = Pharmacy
    serializer_class = PharmacySerializer
    permission_classes = [AccessCha]


    def get(self, request, *args, **kwargs):
        data = Pharmacy.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Pharmacy Created Successfully"
            })
        else:
            return Response(serializer.errors)




class UpdatePharmacyView(GenericAPIView):
    queryset = Pharmacy
    serializer_class = PharmacySerializer

    def get(self, request, id):
        data = get_object_or_404(Pharmacy, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self,request,id):
        data = get_object_or_404(Pharmacy, id=id)
        serialzier = self.get_serializer(data, data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response({
                "message":"Pharmacy Update Successfully"
            })
        else:
            return Response(serialzier.errors, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        data = get_object_or_404(Pharmacy, id=id)
        data.delete()
        return Response({
            "message":"Pharmacy deleted successfully"
        },status.HTTP_204_NO_CONTENT)