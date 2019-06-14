from django.db import models
    
class Bank(models.Model):
    name = models.CharField(max_length = 250)
    logo_url = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Account(models.Model):
    owner = models.ForeignKey('auth.User', related_name='accounts', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    bank = models.ForeignKey(Bank, related_name='accounts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bank.name + ": " + self.name

    class Meta:
        ordering = ('created_at',)