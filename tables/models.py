# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from profiles.models import UserProfile

class Table(models.Model):
    
    #class Meta:
    #    permissions = (())
    name = models.CharField(max_length=100, default='Mein Tisch')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description =models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    #tags = models.ManyToManyField('tag.Tag', through='TableTagRel')
    people = models.ManyToManyField(UserProfile, through='Chair', related_name='tables')
    
    def get_user(self):
        query = Chair.objects.filter(table=self)
        return query
            
    def __str__(self):
        return "%s : %s" % (self.name, self.owner.username)


class Chair(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return "%s an Tisch %s" % (self.user.username, self.table.name)

class Rule(models.Model):
    text = models.CharField(max_length=100, default='be nice')

#class TableTagRel(models.Model):
    #table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    #tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE, null=True)
    