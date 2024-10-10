from rest_framework import serializers
from models import *

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('price', 'devise' , 'statut' , 'user')

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ('transaction_id', 'solde', 'devise' , 'statut_last_history_transaction' , 'statut_new_history_transaction')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('user', 'document_of_personnel_identification', 'adress_of_residence', 'region')


