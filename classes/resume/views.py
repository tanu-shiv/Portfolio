from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact 


def projects_view(request):
    """
    Renders the projects page of the portfolio.
    """
    return render(request, 'projects.html')


def home_and_contact_view(request):
    """
    Renders the home page and handles the contact form submission.

    This single function handles both GET and POST requests for the homepage,
    eliminating the need for a separate 'home' view.
    """
    if request.method == "POST":
        # Handle the form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Create and save a new Contact object
        # You can add more validation here if needed
        try:
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                content=content
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        # Redirect the user to prevent form resubmission
        return redirect('home')

    # If the request is not a POST, just render the home page
    return render(request, 'home.html')
