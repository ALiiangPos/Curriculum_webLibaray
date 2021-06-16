from django.db import models ;

'''
    书的信息   
'''
class Book( models.Model):
    book_id = models.CharField(max_length = 20 , primary_key=True)
    isbn = models.CharField( max_length = 20 ) 
    name = models.CharField( max_length = 50 )
    author = models.CharField( max_length = 30 )
    price = models.FloatField( )
    quantity = models.IntegerField() 
    book_type = models.CharField(max_length = 30)
    the_number_of_page = models.IntegerField() 
    press = models.CharField( max_length=40 )
    entry_date = models.DateField() 

'''
    用户信息 
'''
class  User( models.Model ) :
    Sex_choice = (
        ('F'   , 'female' ) ,
        ('M'   , 'male'  ) ,
    )
    flag_choice = (
        (1 , 'admintor' ),
        (2 , 'Ordinary users' ) ,
    )
    status_choice = (
        ( '1' , 'undergraduate' ) ,
        ( '2' , 'master' ) ,
        ( '3' , 'Doctor' ) ,
        ( '4' , 'Teacher' ) ,
        ( '5' , 'Outsiders') ,
        ( '6' , 'worker' ) ,
    ) 
    id = models.CharField( max_length = 30 ,primary_key = True)
    loan_id = models.CharField( max_length = 30  ,unique=True)
    name = models.CharField( max_length = 50 )
    email = models.CharField( max_length = 20 )
    tele_nummebr = models.CharField()
    pwd = models.CharField( max_length = 15 )
    sex = models.CharField(  choices=Sex_choice , max_length = 1  )
    age = models.IntegerField() 
    flag = models.IntegerField(choices = flag_choice  ) 
    status = models.CharField( max_length =1  , choices = status_choice )

'''
    借阅表
'''  
class Loan( models.Modle ) :
    loan_id = models.CharField (max_length = 30  ,primary_key = True )
    user_id = models.ForeginKey(User ,related_name ='loan_id' ,on_delete=models.CASCADE)
    book_id = models.ForeginKey(Book ,related_name ='book_id' ,on_delete=models.CASCADE)
    loan_date = models.DateField() 

'''
    借阅历史表
'''
class LoanHistory( models.Modle ):
    loan_id = models.CharField (max_length = 30  ,primary_key = True )
    user_id = models.ForeginKey(User ,related_name ='loan_id' ,on_delete=models.CASCADE)
    book_id = models.ForeginKey(Book ,related_name ='book_id' ,on_delete=models.CASCADE)
    loba_date = models.DateField() 
    uesr_loan = models.OneToManyField()
    return_date = models.DateField() 

'''
    预约表
'''
class revesation( models.module ) :
    loan_id = models.CharField (max_length = 30  ,primary_key = True )
    user_id = models.ForeginKey(User ,related_name ='loan_id' ,on_delete=models.CASCADE)
    book_id = models.ForeginKey(Book ,related_name ='book_id' ,on_delete=models.CASCADE)
    user_reversation = models.OneToManyField(User)

