# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from profiles.models import UserProfile
from django.urls import reverse
class Table(models.Model):
    #class Meta:
    #    permissions = (())
    unique_name = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100, default='Mein Tisch', primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description =models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    #tags = models.ManyToManyField('tag.Tag', through='TableTagRel')
    people = models.ManyToManyField(User, related_name='tables')
    
    
            
    def __str__(self):
        return "%s : %s" % (self.name, self.owner.username)

    def save(self):
        self.unique_name = self.name.replace(' ', '').lower()
        super(Table, self).save()

    def get_absolute_url(self):
        return ('/tables/%s' % self.unique_name)

     



class Rule(models.Model):
    text = models.CharField(max_length=100, default='be nice')

#class TableTagRel(models.Model):
    #table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    #tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE, null=True)
    