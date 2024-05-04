from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        origin = request.POST.get("origin")
        destination = request.POST.get("destination")
        api_url = f'http://127.0.0.1:8000/Flight/{origin}/{destination}/'  # Replace with your API endpoint URL
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            flight_data = response.json()
            return render(request, 'results.html', {'flight_data': flight_data})
        except requests.exceptions.RequestException as e:
            # Handle exceptions such as connection errors, timeouts, etc.
            return render(request, 'index.html', {'message': f'Failed to fetch flight results: {e}'})
        except ValueError as e:
            # Handle JSON decoding errors
            return render(request, 'index.html', {'message': f'Failed to decode JSON response: {e}'})
    
    return render(request, 'index.html')
