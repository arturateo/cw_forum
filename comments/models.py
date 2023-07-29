from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Comments(models.Model):
    comment_author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='comment_author',
                                       verbose_name='Автор')
    topic = models.ForeignKey('topics.Topics', on_delete=models.CASCADE, related_name='comment_topic',
                              verbose_name='Топик')
    summary = models.CharField(null=False, blank=False, max_length=300, verbose_name='Текст комментария')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.summary}'
