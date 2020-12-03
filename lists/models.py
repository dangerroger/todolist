from django.db import models
class Item(models.Model):
    """docstring for Item."""
    text = models.TextField(default = '')


    #def __init__(self, arg):
        #super(Item, self).__init__()
        #self.arg = arg

# Create your models here.
