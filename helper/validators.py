from django.core.validators import RegexValidator

mobile_regex = RegexValidator( regex = r'^[6-9]\d{9}$', message ="upto 10 digits")
email_regex = RegexValidator( regex = r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$', message ="Enter a valid email address.")