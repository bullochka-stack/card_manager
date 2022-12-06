from django.utils import timezone
from .models import Card


def task_check(pk):
    queryset = Card.objects.filter(pk=pk, status='Active')
    for item in queryset:
        if item.date_end < timezone.now():
            item.status = 'Overdue'
            item.save()

