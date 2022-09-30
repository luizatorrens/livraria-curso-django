from django.http import HttpResponse
from django.views import View
from core.models import Categoria

import json

def teste(request):
    return HttpResponse("Hello Word!")

class CategoriaView(View):
    def get(self, request):
        data = list(Categoria.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type="application/json")