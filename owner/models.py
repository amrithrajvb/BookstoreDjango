from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    copies=models.IntegerField()
    category=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.book_name
        # return self.author

class Order(models.Model):
    product=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    options=(("ordered","ordered"),("delivered","delivered"),
             ("in_transit","in_transit"),("cancelled","cancelled"))
    status=models.CharField(max_length=100,choices=options,default="ordered")
    phone=models.CharField(max_length=20)
    expected_deliverydate=models.DateField(null=True)

# book=Book(book_name="randamoozham",author="mt",price=200,copies=500)
# book.save()

#to fetch all objects:

# books=Book.objects.all()

#to fetching specific record

#reference=modelname.objects.get(fieldname=value)

#updating specific record

# book=Book.objects.get(id=1)

#book.price=280
#book.save()

#book=Book.objects.filter(price__lt=300)
# book=Book.objects.filter(price__lte=300)
# book=Book.objects.filter(book_name__iexact="AMMA")
# book=Book.objects.filter(book_name__contains="da")
