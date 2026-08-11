from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.medicine.api.serializer import MedicineSerializer
from apps.medicine.models import Medicine
from django.shortcuts import get_object_or_404


class MedicineView(GenericAPIView):
    queryset = Medicine
    serializer_class = MedicineSerializer


    def get(self, request, *args, **kwargs):
        data = Medicine.objects.all()
        serializer = MedicineSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MedicineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Medicine Created Successfully"
            })
        else:
            return Response(serializer.errors)


    def put(self,request, *args, **kwargs):
        id = request.GET.get('id')
        if not id:
            return Response({
                "message":"Please provide id in request parameter"
            },status.HTTP_400_BAD_REQUEST)
        data = get_object_or_404(Medicine, id=id)
        serialzier = self.get_serializer(data, data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response({
                "message":"Put request trigger"
            })
        else:
            return Response(serialzier.errors, status.HTTP_400_BAD_REQUEST)