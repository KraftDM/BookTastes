from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/index.jinja2')
def my_view(request):
    return {'project': 'index'}

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