from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.mail import EmailMessage
from io import BytesIO
from django.conf import settings
from django.core.mail import send_mail


def generate_registration_form_pdf(user_data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Customize the PDF content using the user_data dictionary
    c.drawString(100, 800, f"name: {user_data['name']}")
    c.drawString(100, 780, f"Email: {user_data['email']}")
    c.drawString(100, 760, f"contact: {user_data['contact_no']}")

    c.save()
    buffer.seek(0)
    return buffer
    
def send_registration_form_email(user_data):
    subject = 'Registration Form Submission'
    message = 'Thank you for registering. Please find the registration form attached.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user_data['email']]

    # Load the PDF content from the buffer and attach it to the email
    pdf_buffer = generate_registration_form_pdf(user_data)
    pdf_attachment = BytesIO(pdf_buffer.getvalue())

    email = EmailMessage(subject, message, from_email, to_email)
    email.attach('registration_form.pdf', pdf_attachment.getvalue(), 'application/pdf')
    email.send()

def send_email(user_data):
    subject = 'Registration Form Submission'
    message = 'Thank you for registering.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user_data['email']]

    send_mail(subject, message, from_email, to_email)


# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage

# def send_registration_form_email(user_data):
#     subject = 'Registration Form Submission'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     to_email = [user_data['email']]

#     # Render the HTML template with user_data
#     html_content = render_to_string('registration_form_template.html', user_data)

#     email = EmailMessage(subject, '', from_email, to_email)
#     email.content_subtype = 'html'  # Set the content type to HTML
#     email.body = html_content
#     email.send()

    # Optionally, you may save the filled form HTML to the user's account or elsewhere for future reference.
