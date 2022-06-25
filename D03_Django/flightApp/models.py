from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_lenght=10)
    operationAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20,blank=True,null=True)
    arrivalCity=models.CharField(max_lenght=20)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()

class Passenger(models.Model):
    firstName = models.CharField(max_lenght=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone =models.CharField(max_length=10)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)