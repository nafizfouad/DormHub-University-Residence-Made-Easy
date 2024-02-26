"""
Django views Configuration Documentation

This module defines various controller files
"""
from django.shortcuts import render, redirect

from .models import *


def student(request):
    """
    View function to handle the student view.

    This function retrieves the student object based on the logged-in user's email.
    It gets the hall and room associated with the student and retrieves repair requests for the student's hall.
    The function processes form submissions for requesting room change and repair.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object rendering the student template.
    """
    student = Student.objects.get(email=request.user.email)
    hall = Hall.objects.get(hallId=student.hall.hallId)
    room = student.room.roomId
    requests = RepairRequest.objects.filter(student=student, hall=hall)

    if 'change' in request.POST:
        ifPresent = SwapRequest.objects.filter(hall=hall, student=student)
        if not ifPresent:
            createRequest = SwapRequest(
                hall=hall,
                student=student,
                reason=request.POST.get('reason'),
            )
            createRequest.save()
            createRequest.noOfRequests += 1
            createRequest.save()
        else:
            createRequest = SwapRequest.objects.get(hall=hall, student=student)
            createRequest.reason = request.POST.get('reason')
            createRequest.status = 0
            createRequest.noOfRequests += 1
            createRequest.save()
        return redirect('/student')

    if 'repair' in request.POST:
        requestId = len(RepairRequest.objects.filter()) + 1
        createRequest = RepairRequest(
            hall=hall,
            student=student,
            reason=request.POST.get('reason'),
            requestType=int(request.POST.get('type')),
            requestId=requestId
        )
        createRequest.save()
        return redirect('/student')

    context = {
        'room': room,
        'requests': requests
    }
    return render(request, 'student.html', context)