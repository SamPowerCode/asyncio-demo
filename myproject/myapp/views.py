import asyncio
from django.http import JsonResponse

async def async_view(request):
    # Simulate an asynchronous task
    await asyncio.sleep(2)
    return JsonResponse({'message': 'This is an async view!'})
