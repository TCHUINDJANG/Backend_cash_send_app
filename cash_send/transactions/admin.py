from django.contrib import admin


class AdminTransaction(admin.ModelAdmin):

    list_display = ('sender_account_id','receiver_account_id', 'price' , 'devise' , 'statut')



class AdminTransactionHistory(admin.ModelAdmin):

    list_display = ('transaction_id','code_of_country', 'drapeau')
    

class AdminUserRegistrationModel(admin.ModelAdmin):

    list_display = ('numero_telephone','pays')
    

class AdminAccount(admin.ModelAdmin):

    list_display = ('user','document_of_personnel_identification', 'adress_of_residence' , 'region')
    

