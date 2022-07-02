from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]

class Article(models.Model):
    authorName = models.CharField(max_length=50, null=False, blank=False, verbose_name="имя автора")
    authorEmail = models.EmailField(max_length=50, null=False, blank=False, verbose_name="email автора")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=50, null=False, verbose_name="Статус", default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.id}. {self.authorName}: {self.authorEmail}"

    class Meta:
        db_table = "articles"
        verbose_name = "Записи"
        verbose_name_plural = "Гостевые книги"
