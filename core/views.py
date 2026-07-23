import random
from datetime import datetime, timezone

from django.http import HttpResponse


def index(request):
    now = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
    number_of_the_minute = random.randint(1, 100)
    return HttpResponse(f"Hello, World!<br>{now}<br>Here's your random number: {number_of_the_minute}")
