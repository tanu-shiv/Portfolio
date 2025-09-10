from django.contrib import admin
from django.urls import path, include
from resume import views

urlpatterns = [
    # The homepage URL now points to the new 'home_and_contact_view' function.
    path('', views.home_and_contact_view, name='home'),
    path('admin/', admin.site.urls),
    path('projects/', views.projects_view, name='projects'),
    # Note: Your original urls.py also had this line for contact
    path('contact/', views.home_and_contact_view, name='contact'),
]
