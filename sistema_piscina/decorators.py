from django.shortcuts import render
from .decorators import admin_required

@admin_required
def dashboard(request):
    return render(request, 'admin_dashboard.html')

