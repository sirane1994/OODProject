from django.db import models

# Create your models here.
CHOICES = (
    ('Books', 'Books'),
    ('Sports', 'Sports'),
    ('Learning', 'Learning'),
    ('Travel', 'Travel'),
    ('Technical', 'Technical'),
    ('Music', 'Music'),   
)

OPTIONS = (
    ('Recess Cafe', 'Recess Cafe'),
    ('Dunkin', 'Dunkin'),
    ('Alto Cinco', 'Alto Cinco'),
    ('Starbucks', 'Starbucks'),   
)


#Model for Profile Infromation Class
class ProfileInfo(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    inputEmail = models.CharField(max_length=250)
    userPassword = models.CharField(max_length=250)
    phoneNumber = models.BigIntegerField()
    dateOfBirth = models.DateTimeField(blank=True, null=True)
    locationCriteria = models.CharField(max_length=250, choices=OPTIONS)
    eventCategories = models.CharField(max_length=250, choices=CHOICES)

    # Constructor for the class to return the firstname when the class is invoked.
    def __str__(self):
            return self.firstName