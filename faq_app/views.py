from django.shortcuts import render
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'faq_app/index.html')

def home(request):
    return HttpResponse("Welcome to the FAQ API!")

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()  
    serializer_class = FAQSerializer

    def get_queryset(self):
        queryset = FAQ.objects.all()
        lang = self.request.query_params.get('lang', 'en')

        valid_lang_fields = ['hi', 'bn']

        if lang not in valid_lang_fields and lang != 'en':
            raise ValidationError(f"Invalid language code '{lang}'. Supported languages are {valid_lang_fields + ['en']}.")

        lang_field = f'question_{lang}' if lang != 'en' else 'question'
        queryset = queryset.filter(**{f'{lang_field}__isnull': False})

        return queryset
    
    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            response['Content-Type'] = 'application/json; charset=utf-8'  
            return response
        except ValidationError as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
