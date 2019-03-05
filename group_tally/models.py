from django.db import models

# Create your models here.


class Record(models.Model):
    id = models.AutoField(u"ID", primary_key=True)
    name = models.CharField(u"名称", max_length=100)
    date = models.DateField(u"日期", auto_now=False, auto_now_add=True)
    members = models.ManyToManyField("Person", verbose_name=u"参与人员")
    cost = models. DecimalField(
        u"金额", default=0, max_digits=8, decimal_places=2)

    def all_members(self):
        member_list = []
        for member in self.members.values_list('name'):
            member_list.append(member[0])
        return ','.join(member_list)

    def members_count(self):
        return len(self.members.values_list())

    def average_cost(self):
        return round(float(self.cost) / float(self.members_count()), 2)

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.AutoField(u"ID", primary_key=True)
    name = models.CharField(u"名字", max_length=100)
    expense = models. DecimalField(
        u"支出", default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
