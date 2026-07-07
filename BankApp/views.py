import random

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def pay(request):
    outcome = random.choice(["yes", "no", "timeout"])
    if outcome == "timeout":
        return Response({"status": "timeout"}, status=408)
    if outcome == "yes":
        return Response({"status": "accepted"}, status=201)
    return Response({"status": "rejected"}, status=402)
