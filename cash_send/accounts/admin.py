from django.contrib import admin

class AdminAccount(admin.ModelAdmin):

    list_display = ('user','solde', 'devise')



class AdminCountry(admin.ModelAdmin):

    list_display = ('name_of_country','code_of_country', 'drapeau')
    

class AdminUserRegistrationModel(admin.ModelAdmin):

    list_display = ('numero_telephone','pays')
    

class AdminProfile(admin.ModelAdmin):

    list_display = ('user','document_of_personnel_identification', 'adress_of_residence' , 'region')
    
