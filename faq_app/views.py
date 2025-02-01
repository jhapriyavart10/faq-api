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
        lang = self.request.query_params.get('lang', 'en')  # Default to 'en' if not provided

        valid_lang_fields = ['hi', 'bn']

        # Validate the language code passed in the query parameters
        if lang not in valid_lang_fields and lang != 'en':
            raise ValidationError(f"Invalid language code '{lang}'. Supported languages are {valid_lang_fields + ['en']}.")

        # Choose the correct field based on the language code
        lang_field = f'question_{lang}' if lang != 'en' else 'question'

        # Filter the queryset based on the selected language
        queryset = queryset.filter(**{f'{lang_field}__isnull': False})

        return queryset
    
    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')  # Default to 'en' if not provided
        
        # Pass the lang to the serializer context when instantiating the serializer
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'lang': lang})
        
        try:
            # Return the serialized data as the response
            return Response(serializer.data)
        except ValidationError as e:
            # Handle any validation errors (e.g., invalid language code)
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
