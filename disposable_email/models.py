from django.db import models

# Create your models here.



class DisposableEmailDomain(models.Model):
    domain = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain
    
    class Meta:
        db_table = 'disposable_email_domain'