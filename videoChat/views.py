from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, View
from .models import people

# Create your views here.
def index(request):
    return render(request, 'videoChat/index.html' )

class userReturn(View):
    def get(self, request):
        getPerson = people.objects.filter(used = False)[:1]

        for p in getPerson:
            name = p.name
            updateP = people.objects.filter(name = p.name).update(used = True)

        data = {
            'success': name
        }
        return JsonResponse(data)

def resetUsed(request):
    updatePips = people.objects.all().update(used = False)
    return render(request, 'videoChat/reset.html')