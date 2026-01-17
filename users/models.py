from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField("Nombre Completo", max_length=100)
    email = models.EmailField("Correo Electrónico", unique=True) # Evita correos duplicados
    phone = models.CharField("Teléfono", max_length=20)
    address = models.CharField("Dirección", max_length=255) # Cambié direction por address (más común)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Nombre del Producto", max_length=100)
    sku = models.CharField("Código/SKU", max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Claim(models.Model):
    # Definimos estados posibles para el campo status
    class Status(models.TextChoices):
        OPEN = 'OP', 'Abierta'
        IN_PROGRESS = 'PR', 'En Proceso'
        CLOSED = 'CL', 'Finalizada'

    # Relaciones
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="claims")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="claims")
    
    # Información de la reclamación
    title = models.CharField("Asunto", max_length=150)
    description = models.TextField("Descripción del problema")
    
    # Fechas automáticas
    date_claim = models.DateTimeField("Fecha de creación", default=timezone.now)
    date_finish = models.DateTimeField("Fecha de cierre", null=True, blank=True)
    
    # Estado más descriptivo que un simple Booleano
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN
    )

    def __str__(self):
        return f"{self.title} - {self.client.name}"

    class Meta:
        verbose_name = "Reclamación"
        verbose_name_plural = "Reclamaciones"
