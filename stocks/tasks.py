# stock/tasks.py

from celery import shared_task
from .utils import update_stock_prices


@shared_task
def scheduled_price_update():
    update_stock_prices()
