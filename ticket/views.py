from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import AddTicketForm
from .models import Ticket
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from account.models import MyUser
from .serializers import TicketSerializer
from rest_framework.permissions import IsAdminUser


def add_ticket(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = AddTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.user = user
                ticket.save()
                return redirect('ticket:list')
        else:
            form = AddTicketForm()
    else:
        return redirect('account:login')
    return render(request, 'ticket/add.html', context={'form': form, 'user': user})


def list_ticket(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user)
    return render(request, 'ticket/list.html', context={'tickets': tickets})


@api_view(['GET'])
@permission_classes([IsAdminUser]) #  is_authenticated=True  ---->  is_staff=True ---->  ...
def list_ticket_api(request):
    user_get = request.GET.get('user')
    if not  user_get:
        return Response({'detail': 'user parameter is required'}, status=400)

    try:
        user = MyUser.objects.get(id=user_get)
    except MyUser.DoesNotExist:
        return Response({'detail': 'user is not found'}, status=404)

    ticket = Ticket.objects.filter(user_id=user.id)
    ser = TicketSerializer(ticket, many=True)
    return Response(ser.data)


class AddTicket(APIView):
    def post(self, request):
        ser = TicketSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(request.data)
        else:
            return Response(ser.errors)


class UpdateTicket(APIView):
    def put(self, request, pk):
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instance=ticket, validated_data=serializer.validated_data)
            return Response({'response': 'successful'})
        return Response(serializer.errors)