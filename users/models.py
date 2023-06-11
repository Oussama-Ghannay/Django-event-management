from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.


def is_mail_esprit(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError(
            "Your email must be @esprit.tn"
        )
    
    
    
#username must begin with eng 


class Person(AbstractUser):

    cin = models.CharField(
        "CIN",
        primary_key=True,

        max_length=8,

        validators=[
       

            RegexValidator(
                regex='^[0-9]{8}$',
                message="digits only!!!"
            )
        ]
    )



    username = models.CharField("Username", max_length=255, unique=True)
    
    
    
    email = models.EmailField(
        unique=True,
        validators=[
            is_mail_esprit
        ]
    )

    #champ d'identification unique

    USERNAME_FIELD = 'username'



# Dans votre cas, la méthode __str__() 
# renvoie la valeur du champ username, 
# ce qui signifie que lorsqu'un objet Person
#  est converti en chaîne de caractères, le nom
#  d'utilisateur sera affiché.
    def __str__(self):
        return self.username



# pour afficher le nom de la table au pluriel dans l'interface d'administration.
    class Meta:
        verbose_name_plural = "users"
        models.PositiveIntegerField(("cin"))
