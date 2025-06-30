from django.db import models
from core.models import BaseModel

class Person(BaseModel):
    doc_type = [
        ("p", "Անձնագիր"),
        ("id", "Նույնականացման քարտ"),
        ("fp", "Օտարերկրյա անձնագիր"),
        ("lc", "Կացության քարտ"),
        ("bp", "Կենսաչափական անձնագիր"),
        ("o", "Այլ"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    ssn = models.CharField(max_length=10, null=True, blank=True)
    document = models.CharField(choices=doc_type, null=True, blank=True, max_length=2)
    document_number = models.CharField(max_length=15, null=True, blank=True)
    document_date = models.DateField(null=True, blank=True)
    document_given_by = models.CharField(null=True, blank=True, max_length=10)


    def __str__(self):
        return self.first_name
    
    @property
    def document(self):
        return f"{self.document} N {self.document_number} given on\
              {self.document_date} by {self.document_given_by}"
