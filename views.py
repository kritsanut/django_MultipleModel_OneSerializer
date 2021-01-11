from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # AllowAny
from rest_framework.serializers import ModelSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK

from .serializers import ModelMainSerializer
from .serializers import FiltersSerializers
from .models import ModelMain

from get_app_name.models import Incident

from get_app_name.models import MyComponent


@api_view(['GET'])
def get_all(request):
    filters = {}
    filters['model_main'] = ModelMain.objects.all()
    filters['model_1'] = Model1.objects.all()
    filters['model_2'] = Model2.objects.all()
    serializer = FiltersSerializers(filters, context={"request": request})

    return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)

