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
from .models import Devise

@api_view(['GET'])
def getTransaction(request):
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction , many=True)
    permission_classes = [IsAuthenticated , AuthorTransactionPermission]


@api_view(['GET'])
def getTransactionById(request , pk):
    permission_classes = [IsAuthenticated , AuthorTransactionPermission]
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


@permission_classes([ permissions.IsAuthenticated , IsUser , AuthorTransactionPermission ,CanUpdateTransaction ])
@api_view(['PUT'])
def updateTransaction(request , pk):
    data = request.data
    transaction = get_object_or_404(Transaction , pk)
    serializer = TransactionSerializer(instance = transaction , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@permission_classes([ permissions.IsAuthenticated ,   AuthorTransactionPermission])
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




# cette vue permet de recuperer les taux de change actuels entre le RUB et le XAF

class ExchangeRateView(APIView):
    def get(self , request , *args , ****kwargs):
        exchange_rate = Devise.objects.first()
        if not exchange_rate:
            fetch_exchange_rate()
            fetch_exchange_rate = Devise.objects.first()
        if  exchange_rate:
            return Response({
                'base_currency': exchange_rate.base_currency,
                'target_currency':exchange_rate.target_currency,
                'rate': exchange_rate.rate
            })

        return Response({'error': 'Taux de change non disponble'} , status=status.HTTP_400_BAD_REQUEST)



# cette vue permet soumetre un montan et d'obtenir la converion en RUB

class CurrentConvertView(APIView):
    def get(self , request , *args , ****kwargs):
        amount = request.query_params.get('amount')
        if not amount:
            return Response({'error' : 'Le montant est requis'} , status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = float(amount)
        except ValueError:
            return response({'error': 'Le montant doit etre un nombre'} , status=status.HTTP_400_BAD_REQUEST)


            # recuperer le taux d'echange
            exchange_rate = Devise.objects.first()
            if not exchange_rate:
                fetch_exchange_rate  #si aucun taux n'est retrouve on le recupere de l'api
                exchange_rate = Devise.objects.first()

            
            if exchange_rate:
                converted_amount = amount * exchange_rate.rate
                return Response ({
                    'amount':amount,
                    'convert_amount':convert_amount,
                    'base_currency': exchange_rate.base_currency,
                    'target_currency': exchange_rate.target_currency,
                })

            return Response({'error': 'Taux de change non disponible'} , status=status.HTTP_400_BAD_REQUEST )

