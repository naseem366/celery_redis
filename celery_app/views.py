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