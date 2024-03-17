from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Criado em",auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega",null=False, blank=False)
    finished_at = models.DateField(verbose_name="Finalizado em",null=True, blank=True)

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.title
    