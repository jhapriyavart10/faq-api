from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Get the 'lang' from the context passed in the view
        lang = self.context.get('lang', 'en')  # Default to 'en' if not provided
        
        # Initialize the base representation
        representation = super().to_representation(instance)
        
        # Select the appropriate question field based on the language
        if lang == 'hi':
            representation['question'] = instance.question_hi
        elif lang == 'bn':
            representation['question'] = instance.question_bn
        else:
            representation['question'] = instance.question  # Default to English
        
        # Remove the other language-specific fields
        del representation['question_hi']
        del representation['question_bn']
        
        return representation

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn']
