from django.contrib import admin
from django import forms
from .models import CardSerial
from .models import Card

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    form = CardForm
    list_display = ('full_number', 'start_date', 'expired')


@admin.register(CardSerial)
class CardSerialAdmin(admin.ModelAdmin):
    pass

