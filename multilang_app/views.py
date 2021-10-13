from django.shortcuts import render

# Create your views here.

from django.db import reset_queries
from django.shortcuts import render
from rest_framework.decorators import (
    api_view, renderer_classes,
)
from .models import MultiModel
from haystack.query import SearchQuerySet
 
from rest_framework.response import Response

import simplejson as json
from django.http import HttpResponse

 
 
def gindex(request):
    return render(request, 'search2.html')

def autocomplete2(request):
    print(f"Query: {request.GET.get('q', '')}")
    sqs = SearchQuerySet().using('german').models(MultiModel).autocomplete(
        content_de__fuzzy=request.GET.get('q', '')
        )[:10]
    suggestions = [f'{result.content_de}' for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    print(suggestions)
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')
