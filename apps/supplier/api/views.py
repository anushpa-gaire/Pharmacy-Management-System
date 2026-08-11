from apps.supplier.api.serializer import SupplierSerializer
from apps.supplier.models import Supplier
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def supplier_list(request):
    data = Supplier.objects.all()
    serializer = SupplierSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def supplier_create(request):
    request_data = request.data
    serializer = SupplierSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Supplier created successfully"
        })
    else:
        return Response(serializer.errors)


@api_view(["PUT"])
def supplier_update(request, id):
    # supplier = Supplier.objects.get(id=id)
    supplier = get_object_or_404(Supplier, id=id)
    request_data = request.data
    serializer = SupplierSerializer(supplier, data=request_data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Supplier updated successfully"})
    else:
        return Response(serializer.errors)


@api_view(["DELETE"])
def supplier_delete(request, id):
    supplier = Supplier.objects.filter(id=id).delete()
    return Response({"message": "Supplier deleted successfully"})