from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serialize import TransactionSerializer
from accounts.Permissions import IsAdmin , IsUser , CanUpdateTransaction , AuthorPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework import permissions
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def getTransaction(request):
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction , many=True)
    permission_classes = [IsAuthenticated , IsUser]


@api_view(['GET'])
def getTransactionById(request , pk):
    transaction = get_object_or_404(Transaction , pk)
    serializer = TransactionSerializer(transaction , many=False)
    return Response(serializer.data)


    
@permission_classes([ permissions.IsAuthenticated , IsUser])
@api_view(['POST'])
def create_transaction(request):
    sender_id = request.data.get('sender')
    receiver_id = request.data.get('receiver')
    amount = request.data.get('amount')
    currency_from_id = request.data.get('currency_from')
    currency_to_id = request.data.get('currency_to')
    exchange_rate = request.data.get('exchange_rate')
    
    try:
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        currency_from = Currency.objects.get(id=currency_from_id)
        currency_to = Currency.objects.get(id=currency_to_id)
    except User.DoesNotExist or Currency.DoesNotExist:
        return Response({"error": "Invalid user or currency ID"}, status=status.HTTP_400_BAD_REQUEST)

    # Vérification du solde de l'utilisateur
    if sender.balance < amount:
        return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)

    # Création de la transaction
    transaction = Transaction.objects.create(
        sender=sender,
        receiver=receiver,
        amount=amount,
        currency_from=currency_from,
        currency_to=currency_to,
        exchange_rate=exchange_rate,
        status='pending'
    )

    # Mise à jour des soldes
    sender.balance -= amount
    receiver.balance += amount * exchange_rate
    sender.save()
    receiver.save()

    # Passer la transaction à 'completed'
    transaction.status = 'completed'
    transaction.save()

    # Réponse
    return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)


@permission_classes([ permissions.IsAuthenticated , IsUser , AuthorPermission ,CanUpdateTransaction ])
@api_view(['PUT'])
def updateTransaction(request , pk):
    data = request.data
    transaction = get_object_or_404(Transaction , pk)
    serializer = TransactionSerializer(instance = transaction , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@permission_classes([ permissions.IsAuthenticated , IsUser , AuthorPermission])
@api_view(['DELETE'])
def deleteTransaction(request, pk):
    transaction = get_object_or_404(Transaction , pk)
    transaction.delete()
    return Response('Transaction supprime avec succes')







import csv
from django.http import HttpResponse

def export_transactions(request):
    transactions = Transaction.objects.filter(sender=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Sender', 'Receiver', 'Amount', 'Status'])
    for transaction in transactions:
        writer.writerow([transaction.transaction_date, transaction.sender.username, transaction.receiver.username, transaction.amount, transaction.status])
    return response
