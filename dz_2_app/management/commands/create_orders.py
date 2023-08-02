from datetime import date, datetime
from django.core.management.base import BaseCommand
from dz_2_app.models import Order, User, Goods
from random import randint

ORDERS = 9


class Command(BaseCommand):
    help = 'Fill table fake data'

    def handle(self, *args, **options):
        pk_user = 5
        pk_goods = 9

        user = User(pk=pk_user)
        goods = Goods(pk=pk_goods)
        order = Order(
            user_ID=user,
            goods_ID=goods,
            quantity=randint(1, 10),
            amount=0,
            creation_date=datetime.now()
        )
        order.save()
