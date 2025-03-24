from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name="Título", max_length=60)
    price = models.DecimalField(verbose_name="Preço", max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.title (self.price)}"
    
    @property
    def get_price(self):
        price_as_string = str(self.price).replace(",", ".")
        return price_as_string
    
    class Meta:
        verbose_name = "Livro"    
        verbose_name_plural = "Livros"    
