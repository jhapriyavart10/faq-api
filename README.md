# FAQ API with Multilingual Support

## Project Description
This is a Django-based application designed to manage Frequently Asked Questions (FAQs) with multilingual support. The project includes a RESTful API to fetch FAQs in various languages, caching mechanisms for improved performance, and the integration of a WYSIWYG editor (using django-ckeditor) to manage FAQ answers. The API supports querying FAQs based on the selected language (English, Hindi, Bengali, etc.), and translations are automatically managed using the Google Translate API.

## Features
1) **Multilingual FAQ Support**: The FAQs are available in multiple languages, including English, Hindi, and Bengali.
2) **WYSIWYG Editor**: The FAQ answers are formatted using django-ckeditor for a user-friendly rich text editor.
3) **Caching**: The API responses are cached using Redis for improved performance, reducing the need for repeated translation requests.
4) **Dynamic Translations**: Automatic translations of FAQ questions and answers are provided via the Google Translate API during object creation.
5) **REST API**: A REST API is available to retrieve FAQs in different languages via the `lang` query parameter.

## Installation

### Prerequisites
1) Python 3.8 or later

2) Redis (for caching) 
    * Install Redis on your machine (or use a cloud provider).
    * Start the Redis server using: `redis-server`.
    * Ensure the Redis host configuration in settings.py is correctly set.

3) A Google Cloud API key (for using Google Translate API)
    * Go to the Google Cloud Console: https://console.cloud.google.com/
    * Create a new project.
    * Enable the Google Translate API for your project.
    * Create API credentials and download the `credentials.json` file.
    * Set the `GOOGLE_TRANSLATE_API_KEY` environment variable in your settings.py file with the API key value.


### Steps to Set Up the Project

1) Clone the repository:
   ```bash
   git clone "https://github.com/jhapriyavart10/faq-api.git"
   cd faq-api

2) Create a virtual environment (optional but recommended): "python -m venv venv"

3) Activate the virtual environment: On Windows: ".\venv\Scripts\activate"   On macOS/Linux: "source venv/bin/activate"

4) Install the required dependencies: "pip install django djangorestframework django-ckeditor django-redis googletrans==4.0.0-rc1"

    We'll use:
    Django → Web framework
    Django REST Framework (DRF) → To build APIs
    Django CKEditor → To allow rich text editing
    Django Redis → For caching
    Googletrans → For automatic translations

5) Configure the settings: Set GOOGLE_TRANSLATE_API_KEY and REDIS_HOST in settings.py.

6) Run migrations to set up the database: "python manage.py migrate"

7) Run the development server: "python manage.py runserver"

***API Usage***
The application exposes a REST API to fetch the FAQs in different languages.

Fetch FAQs in English (default): curl http://localhost:8000/api/faqs/
Fetch FAQs in Hindi: curl http://localhost:8000/api/faqs/?lang=hi
Fetch FAQs in Bengali: curl http://localhost:8000/api/faqs/?lang=bn

***Testing***
Run the tests to ensure everything is working: "python manage.py test"
You should see output similar to:

Running tests...
........
----------------------------------------------------------------------
Ran 5 tests in 0.045s

OK