"""
Django views Configuration Documentation

This module defines various controller files
"""
from Hall_Admin.models import *
from Varsity_Admin.models import *
from django.shortcuts import render, redirect


def hallAdmin(request):
    """
    View function to handle the hall admin view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object rendering the hall admin template.
    """
    # Retrieve the hall admin and associated hall using the provided HTTP request object.
    admin = HallAdmin.objects.get(email=request.user.email)
    hall = Hall.objects.get(hallAdmin=admin)

    # Check if the hall has rooms
    changeStructure = 0
    rooms = Room.objects.filter(hall=hall)
    if rooms:
        changeStructure = 1

    # Define colors for rooms
    colors = {
        1: 'crimson',
        2: 'indigo',
        3: 'orange',
        4: 'cornflowerblue',
        5: 'coral',
        6: 'seagreen',
        7: 'yellow',
    }

    # Handle POST request to change hall structure
    if 'change' in request.POST:
        numberOfFloors = int(request.POST.get('floor')) + 1
        for x in range(1, numberOfFloors):
            ca = x * 100
            da = ca + 30 + 1
            for i in range(ca, da):
                newRoom = Room(
                    hall=hall,
                    roomId=i,
                    capacity=int(request.POST.get('capacity')),
                    color=colors[int(i / 100)]
                )
                newRoom.save()
        return redirect('/hallAdmin')

    # Query rooms and organize them by floor
    queryDict = {}
    for o in range(1, 8):
        queryDict[o] = []
    rooms = Room.objects.filter(hall=hall)
    for room in rooms:
        queryDict[int(room.roomId / 100)].append(room)

    # Render the hall admin template with context
    context = {
        'hall': hall,
        'changeStructure': changeStructure,
        'queryDict': queryDict
    }
    return render(request, 'hallAdmin.html', context)
