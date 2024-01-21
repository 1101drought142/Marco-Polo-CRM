from django.db import models

class DocumentType(models.Model):
    name = models.CharField(max_length=63)
    def __str__(self):
        return self.name

class Manager(models.Model):
    pass

class Client(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    middle_name = models.CharField(max_length=63, blank=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='clients', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'
    
    def get_small_fio(self):
        if (self.middle_name):
            return f'{self.first_name[0]}.{self.middle_name[0]}. {self.last_name}'
        else:
            return f'{self.first_name[0]}. {self.last_name}'

class ClientDocumnt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    doc_series = models.CharField(max_length=63)
    doc_number = models.CharField(max_length=63)