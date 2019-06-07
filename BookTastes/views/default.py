from BookTastes import models
from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

def getString(count, endings):
  value = count % 100
  if (value > 10 and value < 20):
    return '{} {}'.format(count, endings[2])
  else:
    value = count % 10
    if value == 1:
      return '{} {}'.format(count, endings[0])
    elif (value > 1 and value < 5):
      return '{} {}'.format(count, endings[1])
    else:
      return '{} {}'.format(count, endings[2])

def formatPortions(count):
  endings = ['порция', 'порции', 'порций']
  return getString(count, endings)

def formatTimes(count):
  endingsMinutes = ['минута', 'минуты', 'минут']
  endingsHours = ['час', 'часа', 'часов']
  hours = count // 60
  minutes = count % 60
  result = ''
  if hours > 0:
    result = getString(hours, endingsHours) + ' '
  if minutes > 0:
    result += getString(minutes, endingsMinutes)
  return result


@view_config(route_name='home', renderer='../templates/index.jinja2')
def my_view(request):
    # try:
    #     query = request.dbsession.query(models.User)
    #     one = query.filter(models.User.login == 'admin').first()
    #     print(one.name)
    # except DBAPIError:
    #     return Response(db_err_msg, content_type='text/plain', status=500)
    receptsDb = [{'name': 'Горячие пирожки', 'time': 40, 'count_of_portion': 8, 'image': '../static/s1201.jpg'},
    {'name': 'Горячие пирожки', 'time': 40, 'count_of_portion': 8, 'image': '../static/no-photo.png'},
    {'name': 'Горячие пирожки', 'time': 40, 'count_of_portion': 8, 'image': '../static/s1201.jpg'}]
    recepts = []
    for recept in receptsDb:
      recepts.append({'name': recept['name'], 'time': formatTimes(recept['time']), 'portions': formatPortions(recept['count_of_portion']), 'image': recept['image']})
    return {'recepts': recepts, 'project': 'index'}


@view_config(route_name='recepts', renderer='../templates/recepts.jinja2')
def my_view2(request):
    return {'project': 'recepts'}


@view_config(route_name='collection', renderer='../templates/collection.jinja2')
def my_view3(request):
    return {'project': 'collection'}


@view_config(route_name='recept_view', renderer='../templates/recept_view.jinja2')
def my_view4(request):
    id = request.matchdict['id']
    receptDb = {
      'name': 'Горячие пирожки',
      'time': 40,
      'count_of_portion': 8,
      'image': '../static/s1201.jpg',
      'author': 'alex',
      'description': 'Какое-то небольшое описание. Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в формировании системы обучения кадров, соответствует насущным потребностям.',
      'total': 'Тут подводится какой-то итог! Бла-Бла-Бла. Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в формировании системы обучения кадров, соответствует насущным потребностям.'
    }
    recept = {
      'name': receptDb['name'],
      'time': formatTimes(receptDb['time']),
      'portions': formatPortions(receptDb['count_of_portion']),
      'image': receptDb['image'],
      'author': receptDb['author'],
      'description': receptDb['description'],
      'ingredients': [{'name': 'Лук', 'count': '2 кг'}, {'name': 'Тесто', 'count': '0.5 кг'}, {'name': 'Тесто', 'count': '0.5 кг'}],
      'stages': [{
        'index': 1,
        'description': 'Тут текст про первый этап! Какое-то небольшое описание. Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в формировании системы обучения кадров, соответствует насущным потребностям.',
        'image': '../static/no-photo.png'
      }, {
        'index': 2,
        'description': 'Тут текст про второй этап! Какое-то небольшое описание. Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в формировании системы обучения кадров, соответствует насущным потребностям.',
        'image': '../static/no-photo.png'
      }],
      'total': receptDb['total']
    }
    return {'recept': recept, 'idRecept': id }

@view_config(route_name='create_recept', renderer='../templates/create-recept.jinja2')
def my_view3(request):
    searchterm = request.params['recept_name']
    if (searchterm != None):
        print(searchterm)
    return {'project': 'create-recept'}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""