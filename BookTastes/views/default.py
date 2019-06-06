from BookTastes import models
from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError


@view_config(route_name='home', renderer='../templates/index.jinja2')
def my_view(request):
    # try:
    #     query = request.dbsession.query(models.User)
    #     one = query.filter(models.User.login == 'admin').first()
    #     print(one.name)
    # except DBAPIError:
    #     return Response(db_err_msg, content_type='text/plain', status=500)
    recepts = [{'name': 'Горячие пирожки', 'time': '40 минут', 'portions': '8 порций'}]
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
    return {'idRecept': id }


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