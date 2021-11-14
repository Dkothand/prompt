from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from app.serializers import ProviderSerializer
from app.models import Provider
from app.api import parse_bool_param

# Create your views here.
@api_view(['GET'])
def provider_list(request):
    if request.method == 'GET':
        providers = Provider.objects.all()

        name = request.GET.get('name')
        if name is not None:
            providers = providers.filter(name__icontains=name)
        
        fees = request.GET.get('fees')
        if fees is not None:
            providers = providers.filter(fees__lte=fees)

        min_balance = request.GET.get('minimum_balance')
        if min_balance is not None:
            providers = providers.filter(minimum_balance__lte=min_balance)
        
        automated = request.GET.get('automated')
        if automated is not None:
            providers = providers.filter(automated=parse_bool_param(automated))
        
        advisor = request.GET.get('advisor')
        if advisor is not None:
            providers = providers.filter(advisor=parse_bool_param(advisor))
        
        ease_of_use = request.GET.get('ease_of_use')
        if ease_of_use is not None:
            providers = providers.filter(ease_of_use=ease_of_use)

        priorities = request.GET.getlist('priority')
        if priorities:
            # ASC by default, need to convert ease_of_use to DESC
            try:
                index = priorities.index('ease_of_use')
                priorities[index] = '-' + priorities[index]
            except ValueError:
                pass
            providers = providers.order_by(*priorities)
        else:
            providers = providers.order_by('fees', 'minimum_balance', '-ease_of_use')
        
        limit = request.GET.get('limit')
        if limit is not None:
            providers = providers[:limit]
 
        serialize = ProviderSerializer(providers, many=True)
        return JsonResponse(serialize.data, safe=False)
