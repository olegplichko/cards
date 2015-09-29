import time
import uuid
from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime

EXPIRATION_PERIONDS = (
    ('OY', '1 year'),
    ('HY', '6 months'),
    ('OM', '1 month'),
)

INACTIVE_CARD_STATUS = 'IA'
ACTIVE_CARD_STATUS = 'AC'
EXPIRED_CARD_STATUS = 'EX'

CARD_STATUSES = (
    (INACTIVE_CARD_STATUS, 'Inactive'),
    (ACTIVE_CARD_STATUS, 'Active'),
    (EXPIRED_CARD_STATUS, 'Expired'),
)


class CardSerial(models.Model):
    number = models.CharField(max_length=2, primary_key=True)

    def __unicode__(self):
        return 'Serial #%s' % self.number


class Card(models.Model):
    """ Card with 14 digit number
    """
    serial = models.ForeignKey(CardSerial)
    number = models.UUIDField(max_length=14, default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField(auto_created=True, editable=False)
    expiration_date = models.DateTimeField(editable=False)
    last_used_date = models.DateTimeField(blank=True, editable=False)
    balance = models.IntegerField(blank=True, default=0)
    status = models.CharField(max_length=2, choices=CARD_STATUSES, default=INACTIVE_CARD_STATUS)

    def __unicode__(self):
        return 'Card #%d' % self.full_number()

    def full_number(self):
        return '%d%d' % (self.serial.number, self.number)

    def expired(self):
        return naturaltime(time.time()-self.expiration_date)


class Transaction(models.Model):
    card = models.ForeignKey(Card)
    date = models.DateTimeField(auto_created=True)
    amount = models.IntegerField()

