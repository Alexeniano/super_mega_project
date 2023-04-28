from django.db import models


class Quiz(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название квиза",
    )
    text = models.TextField(
        verbose_name="Текст",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации', 
    )
    image = models.ImageField(
        upload_to='static/quiz_images/',
        verbose_name='your photo',
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-date',)
