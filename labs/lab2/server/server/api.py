from django.http import (HttpResponse,
                         JsonResponse,
                         HttpResponseBadRequest,
                         HttpResponseNotAllowed,
                         HttpResponseServerError)
import json
from datetime import date, datetime
from . import db
from .models.Airport import Airport
from .models.Flight import Flight


def save(request, table):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            try:
                dict_list = json.loads(file.read().decode('utf8'))
                db.truncate(table)
                db.create_list(table, dict_list)
            except Exception as error:
                return HttpResponseServerError(error_in_json(str(error)))
            return HttpResponse(success_in_json('Data saved'))
        return HttpResponseBadRequest(error_in_json('File does not exist'))
    else:
        return HttpResponseNotAllowed(['POST'])


def default(o):
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    raise TypeError("Type %s not serializable" % type(o))


def get_data(data):
    return json.loads(data.decode('utf-8'))


def flight(request, id):
    if request.method == 'GET':
        phrase = request.GET.get('search')
        excluded = request.GET.get('excluded')
        if id:
            data = Flight.get(id)[0]
        elif phrase or excluded:
            data = db.fulltext(phrase, excluded)
        else:
            data = db.get_join_flights()
        return HttpResponse(json.dumps(data, default=default))
    elif request.method == 'POST':
        try:
            data = get_data(request.body)
            new_id = Flight.create(
                id_from_airport=str(data['from']),
                id_to_airport=str(data['to']),
                id_plane=str(data['plane']),
                date="'%s'" % data['date'][:10],
                status=str(data['status'])
            )
            flight = Flight.get(new_id)[0]
            return JsonResponse(flight)
        except Exception as error:
            return HttpResponseBadRequest(error_in_json(str(error)))
        return HttpResponse(success_in_json('Data added'))
    elif request.method == 'PUT':
        try:
            data = get_data(request.body)
            Flight.update(
                id,
                id_from_airport=str(data['from']),
                id_to_airport=str(data['to']),
                id_plane=str(data['plane']),
                date="'%s'" % data['date'][:10],
                status=str(data['status'])
            )
        except Exception as error:
            return HttpResponseBadRequest(error_in_json(str(error)))
        return HttpResponse(success_in_json('Data updated'))
    elif request.method == 'DELETE':
        try:
            Flight.delete(id)
        except Exception as error:
            return HttpResponseBadRequest(error_in_json(str(error)))
        return HttpResponse(success_in_json('Data deleted'))
    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])


def airport(request):
    if request.method == 'GET':
        data = Airport.all()
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponseNotAllowed(['GET'])


def plane(request):
    if request.method == 'GET':
        min = request.GET.get('min')
        max = request.GET.get('max')
        cargo = request.GET.get('cargo')

        params = []
        if min:
            params.append('seats > %s' % min)
        if max:
            params.append('seats < %s' % max)
        if cargo:
            params.append('cargo = %s' % cargo)

        if params:
            where = ' AND '.join(params)
            query = 'SELECT * FROM plane WHERE %s' % where
        else:
            query = 'SELECT * FROM plane'

        data = db.do(query)
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponseNotAllowed(['GET'])


def success_in_json(message):
    return json.dumps({'message': message})


def error_in_json(error):
    return json.dumps({'error': error})
