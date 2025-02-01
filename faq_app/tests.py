from django.test import TestCase
from django.urls import reverse
from .models import FAQ

# Model Test
class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="डजांगो क्या है?",
            question_bn="ডজাঙ্গো কী?"
        )

    def test_faq_creation(self):
        faq = FAQ.objects.get(id=self.faq.id)
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a high-level Python web framework.")
        self.assertEqual(faq.question_hi, "डजांगो क्या है?")
        self.assertEqual(faq.question_bn, "ডজাঙ্গো কী?")

    def test_translation_method(self):
        faq = FAQ.objects.get(id=self.faq.id)
        self.assertEqual(faq.get_translated_question('hi'), "डजांगो क्या है?")
        self.assertEqual(faq.get_translated_question('bn'), "ডজাঙ্গো কী?")

# API Test
class FAQApiTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="डजांगो क्या है?",
            question_bn="ডজাঙ্গো কী?"
        )

    def test_get_faqs(self):
        url = reverse('faq-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('question', response.json()[0])  # Check if 'question' is present in the response

    def test_get_faqs_with_language(self):
        url = reverse('faq-list') + "?lang=hi"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('डजांगो क्या है?', response.content.decode())

    def test_get_faqs_with_invalid_language(self):
        url = reverse('faq-list') + "?lang=xyz"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)  # Adjust if you're handling invalid language codes differently
        self.assertIn('Invalid language code', response.content.decode())
