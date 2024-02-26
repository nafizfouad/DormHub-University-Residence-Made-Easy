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
   
        # Fetch the student object based on the email associated with the current user
student = Student.objects.get(email=request.user.email)

# Fetch the hall object associated with the student
hall = Hall.objects.get(hallId=student.hall.hallId)

# Extract the room ID of the student
room = student.room.roomId

# Fetch repair requests related to the student and hall
requests = RepairRequest.objects.filter(student=student, hall=hall)

# Check if the 'change' action is triggered via POST request
if 'change' in request.POST:
    # Check if there's already a swap request for the same hall and student
    ifPresent = SwapRequest.objects.filter(hall=hall, student=student)
    if not ifPresent:
        # If no swap request exists, create a new one
        createRequest = SwapRequest(
            hall=hall,
            student=student,
            reason=request.POST.get('reason'),
        )
        createRequest.save()
        createRequest.noOfRequests += 1
        createRequest.save()
    else:
        # If a swap request exists, update the existing request
        createRequest = SwapRequest.objects.get(hall=hall, student=student)
        createRequest.reason = request.POST.get('reason')
        createRequest.status = 0
        createRequest.noOfRequests += 1
        createRequest.save()
    # Redirect to the student page after handling the request
    return redirect('/student')

# Check if the 'repair' action is triggered via POST request
if 'repair' in request.POST:
    # Calculate the ID for the new repair request
    requestId = len(RepairRequest.objects.filter()) + 1
    # Create a new repair request object
    createRequest = RepairRequest(
        hall=hall,
        student=student,
        reason=request.POST.get('reason'),
        requestType=int(request.POST.get('type')),
        requestId=requestId
    )
    createRequest.save()
    # Redirect to the student page after handling the request
    return redirect('/student')

# Prepare context data to be passed to the template
context = {
    'room': room,
    'requests': requests
}

# Render the student.html template with the context data
return render(request, 'student.html', context)
