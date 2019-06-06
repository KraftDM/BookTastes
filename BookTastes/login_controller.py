from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import forget, remember
from pyramid.view import view_config

@view_config(route_name='hello', renderer='templates/index.jinja2')
def hello_world(request):
    #return Response('Hello %(name)s!' % request.matchdict)
    return {'project': 'Hello %(name)s!' % request.matchdict}


def login(request):
    headers = remember(request, 'vasya')
    return HTTPFound(location=request.route_url('hello', name='vasya'),
                     headers=headers)


def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('hello', name='log out!!!'),
                     headers=headers)
