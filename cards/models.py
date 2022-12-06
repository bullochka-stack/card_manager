from django.db import models
from django.db.models.signals import post_save
from apscheduler.schedulers.background import BackgroundScheduler


class Card(models.Model):
    series = models.PositiveIntegerField()
    number = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    use_date = models.DateTimeField()
    summa = models.IntegerField()
    status = models.CharField(max_length=10, choices=(('Active', 'Active'),
                                                      ('Deactive', 'Deactive'),
                                                      ('Overdue', 'Overdue')))

    def __str__(self):
        return f'{self.series} {self.number}'

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class History(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    purchase = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    summa = models.IntegerField()

    def __str__(self):
        return self.purchase

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'


from .task import task_check


def schedule_checking(sender, instance, signal, *args, **kwargs):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        task_check,
        trigger='date',
        run_date=instance.date_end,
        args=[instance.pk],
        coalesce=True,
        max_instances=1,
        replace_existing=True,
    )

    scheduler.start()


post_save.connect(schedule_checking, sender=Card)
