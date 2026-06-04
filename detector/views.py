from django.shortcuts import render
from django.shortcuts import render

from .ml_model import predict_spam
from rest_framework.decorators import api_view
from rest_framework.response import Response

# WEBSITE VIEW
def home(request):

    result = ""

    if request.method == "POST":

        message = request.POST.get("message")

        prediction = predict_spam(message)

        if prediction == 1:
            result = "Spam Message"
        else:
            result = "Normal Message"

    return render(request, "index.html", {
        "result": result
    })
# API VIEW
@api_view(['POST'])
def api_predict(request):

    message = request.data['message']

    prediction = predict_spam(message)

    if prediction == 1:
        result = "Spam"
    else:
        result = "Not Spam"

    return Response({
        "prediction": result
    })


# Create your views here.
