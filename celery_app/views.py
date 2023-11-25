from django.shortcuts import render
from celery_app.tasks import *
from celery.result import AsyncResult


   ## Enqueue Task using delay()

# def index(request):
#     print("Results: ")
#     result1 = add.delay(10,20)
#     print('Result1 = ',result1)
#     result2 = sub.delay(100,20)
#     print('Result2 = ',result2)
#     return render(request, "celery_app/home.html")

   ## Enqueue Task using apply_async()

# def index(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[20,20])
#     print('Result1 = ',result1)
#     result2 = sub.apply_async(args=[80,30])
#     print('Result2 = ',result2)
#     return render(request, "celery_app/home.html")


def index(request):
    result = add.delay(20,30)
    return render(request, "celery_app/home.html",{'result':result})

def check_result(request,task_id):
    result = AsyncResult(task_id)
    print("Ready: ",result.ready())
    print("Successful: ",result.successful())
    print("Failed: ",result.failed())
    return render(request, "celery_app/result.html",{'result':result})



def about(request):
    return render(request, "celery_app/about.html")

def contact(request):
    return render(request, "celery_app/contact.html")



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.status import *
# from .models import Details
# class AddDetails(APIView):
#     def post(self,request):
#         name = request.data.get('name')
#         email = request.data.get('email')
#         phone_number = request.data.get('phone_number')
#         message = request.data.get('message')
#         road = request.data.get('road')
#         city = request.data.get('city')
#         state = request.data.get('state')
#         country = request.data.get('country')
#         qs = Details.objects.create(name =name,email=email,phone_number=phone_number,message=message,road=road,city=city,state=state,country=country)
#         qs.save()
#         return Response({'message':"Data Create Successfully"},status=HTTP_201_CREATED)

