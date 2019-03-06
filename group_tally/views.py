from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Record, Person
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    context = {}
    all_person = Person.objects.all()
    member_list = []
    for person in all_person:
        item = {
            "id": person.id,
            "name": person.name,
            "expense": str(person.expense())
        }
        member_list.append(item)

    context['member_list'] = member_list

    return render(request, 'index.html', context)


def get_records(request):
    all_records = Record.objects.all().order_by('-date')
    items = []
    for record in all_records:
        item = {
            "date": str(record.date),
            "name": record.name,
            "members": str(record.all_members()),
            "cost": str(record.cost),
            # "average": str(record.average_cost())
        }
        items.append(item)

    return JsonResponse({
        'total': len(items),
        'rows': items,
        'data': {
            "catalogues": {
                "date": "日期",
                "name": "名称",
                "members": "参与人员",
                "cost": "金额",
                "average": "人均"
            },
            "items": items
        }
    })


@csrf_exempt
def add_record(request):
    if request.method == "POST":
        name = request.POST['name']
        # getlist ref:https://blog.csdn.net/ndjk454164628/article/details/51757056
        members = request.POST.getlist('members[]')
        cost = request.POST['cost']
        date = request.POST['date']

        # validate members
        if len(members) < 1:
            return JsonResponse({
                "success": 0
            })

        record = Record.objects.create(
            name=name,
            cost=cost,
            date=date
        )

        for member_name in members:
            person = Person.objects.get(name=member_name)
            record.members.add(person)

        record.save()

        return JsonResponse({
            "success": 1,
            "name": name,
            "members": members,
            "cost": cost,
            "date": date
        })


def clear_records(request):
    Record.objects.all().delete()
    # for person in Person.objects.all():
    #     person.expense = 0.0
    #     person.save()

    return JsonResponse({
        "success": 1
    })


def get_expense(request):
    all_person = Person.objects.all()
    items = []
    for person in all_person:
        item = {
            "id": person.id,
            "name": person.name,
            "expense": str(person.expense())
        }
        items.append(item)
    return JsonResponse({
        "success": 1,
        "items": items
    })
