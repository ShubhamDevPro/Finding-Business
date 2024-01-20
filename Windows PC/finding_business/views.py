# business_app/views.py

from django.shortcuts import render
from .main_windows import get_business_list  # Import your script or functions here


def index(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        type1 = request.POST.get('type1')

        # Call your script or functions here and capture the output
        import sys
        from io import StringIO

        # Capture the standard output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        get_business_list(location, type1)

        # Get the output and reset the standard output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Render the template with the captured output
        return render(request, 'index.html', {'table': output})

    # Render the template without results if it's a GET request
    return render(request, 'index.html', {'table': None})
