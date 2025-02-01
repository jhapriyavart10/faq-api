from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, language_code='en'):
        """
        Dynamically retrieves translated question based on language code.
        Defaults to English if translation is unavailable.
        """
        return getattr(self, f'question_{language_code}', self.question)

    def __str__(self):
        return self.question
