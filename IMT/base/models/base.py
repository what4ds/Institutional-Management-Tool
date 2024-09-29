from django.db import models
from django.core.exceptions import ValidationError


class Address(models.Model):
    street_address = models.CharField(max_length=125)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return "Address Saved !"
    

class RelationshipContact(models.Model):
    Mother = 'Mother'
    Father = 'Father'
    Sibling = 'Sibling'
    GrandParents = 'GrandParents'
    Other = "Other"

    rlChoice =     [   
    (Mother , 'Mother'),
    (Father , 'Father'),
    (Sibling , 'Sibling'),
    (GrandParents , 'GrandParents'),
    (Other,'Other')
    ]

    rlname = models.CharField(max_length = 50)
    rlCategory = models.CharField(max_length = 25, choices= rlChoice)
    rlContact = models.IntegerField(max_length= 10, blank= False, null= False)
    rladdress = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.rlCategory} information saved !"
    
    

class Person(models.Model):
    Teacher = 'Teacher'
    Counselor = 'Counselor'
    Admin = 'Admin'
    Janitor = 'Janitor'
    Principal = 'Principal'
    Librarian = 'Librarian'
    Student = 'Student'

    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

    Hindu = "Hindu"
    Muslim = "Muslim"
    Christian = "Christian"
    Sikh = "Sikh"
    Buddh = "Buddh"
    Jain = "Jain"
    other = "other"

    RoleChoices = [
        (Teacher,'Teacher'),
        (Admin , 'Admin'),
        (Janitor , 'Janitor'),
        (Principal , 'Principal'),
        (Librarian , 'Librarian'),
        (Student, 'Student')
    ]

    GenderChoices = [
        (Male , 'Male'),
        (Female , 'Female'),
        (Other , 'Other')    
    ]

    religionChoice = [
        (Hindu , "Hindu"),
        (Muslim , "Muslim"),
        (Christian , "Christian"),
        (Sikh , "Sikh"),
        (Buddh , "Buddh"),
        (Jain , "Jain"),
        (other , "other"),
    ]

    role = models.CharField(max_length = 25, choices= RoleChoices)
    fullname = models.CharField(max_length = 50)
    dateofbirth = models.DateField(auto_now= False, auto_now_add= False)
    gender = models.CharField(max_length = 25, choices= GenderChoices)
    contactnumber = models.IntegerField(max_length= 10, blank= True, null= True)
    emailaddress = models.EmailField(max_length= 50, blank= True, null= True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    rlcontactinfo = models.ForeignKey(RelationshipContact, on_delete=models.CASCADE)
    religion = models.CharField(max_length = 25, choices=religionChoice)
    caste = models.CharField(max_length = 30)
    

    class Meta:
        abstract = True

    def clean(self):
        if self.role != self.Student:

            if not self.contactnumber:
                raise ValidationError("Contact Number is required")
            if not self.emailaddress:
                raise ValidationError("Email Address is required")