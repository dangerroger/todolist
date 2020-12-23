from django.db import models

class List(models.Model):
    """docstring for List"""
    pass

class Item(models.Model):
    """docstring for Item."""
    text = models.TextField(default = '')
    list = models.ForeignKey(List, default = None)


    #def __init__(self, arg):
        #super(Item, self).__init__()
        #self.arg = arg





# Create your models here.
