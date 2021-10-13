from django.db import reset_queries
from django.shortcuts import render
from rest_framework.decorators import (
    api_view, renderer_classes,
)
from .models import Customer
from haystack.query import SearchQuerySet
 
from rest_framework.response import Response

import simplejson as json
from django.http import HttpResponse

 
 
@api_view(['POST'])
def search_customer(request):
    name = request.data['name']
    print(f'----> name: {name}')
    customer = SearchQuerySet().models(Customer).autocomplete(
        first_name__fuzzy=name
    )
    searched_data = []
    for i in customer:
        all_results = {"first_name": i.first_name,
                       "last_name": i.last_name,
                       "balance": i.balance,
                       "status": i.customer_status,
                       }
        searched_data.append(all_results)
 
    return Response(searched_data)


def autocomplete(request):
    print(f"Query: {request.GET.get('q', '')}")
    sqs = SearchQuerySet().models(Customer).autocomplete(
        content_auto__fuzzy=request.GET.get('q', '')
        )[:10]
    suggestions = [f'{result.first_name}: {result.last_name}' for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    print(suggestions)
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')

def index(request):
    return render(request, 'search.html')