from django.db import models


class GlobalSetting(models.Model):
    '''
    Global settings key/value store for the system. This model should not be
    used directly, but via the managers.GlobalSettings class.
    '''
    key = models.CharField(max_length=64, primary_key=True)
    val = models.TextField(null=True)


class UserSetting(models.Model):
    '''
    User settings key/value store for the system. This model should not be
    used directly, but via the managers.UserSettings class.
    '''
    key = models.CharField(max_length=64, primary_key=True)
    val = models.TextField(null=True)
