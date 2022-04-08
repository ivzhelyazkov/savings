from django.utils import timezone


def get_monthly(data):
    return sum(entry.amount for entry in data
               .filter(date__gte=timezone.now()
                       .replace(day=1, hour=0, minute=0, second=0, microsecond=0)))