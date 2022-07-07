from django.db import models
from model_utils.models import TimeStampedModel

from users.models import User
# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField("Category name", max_length=50)

    class Meta: 
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

    objects = models.Manager()

    def __str__(self):
        return self.name

class Article(models.Model): 
    article_code = models.CharField("Article code", max_length=6, unique=True)
    category = models.ForeignKey(ArticleCategory, verbose_name="Article category", related_name="articles", blank=True, on_delete=models.PROTECT)
    name = models.CharField("Article name", max_length=50)
    cost = models.DecimalField("Manufacturing Cost", max_digits=5, decimal_places=2, blank=True)

    class Meta: 
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    def __str__(self):
        return f"{self.article_code} - {self.name}"
    

class Sale(TimeStampedModel):
    date = models.DateField("Date")
    author = models.ForeignKey(User, verbose_name="Author", related_name="sales", on_delete=models.PROTECT)
    article = models.ForeignKey(Article, verbose_name="Article", related_name="sales", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Quantity")
    unit_price = models.DecimalField("Unit selling price", max_digits=5, decimal_places=2, blank=True)

    class Meta: 
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return f"{self.date} - {self.article.name} x {self.quantity}"