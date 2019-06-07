from wsgiref.simple_server import make_server

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from .hello_factory import HelloFactory
from .login_controller import *

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('recepts', '/recepts')
    config.add_route('collection', '/collection')
    config.add_route('recept_view', '/recepts/{id:\w+}')
    config.add_route('create_recept', '/create-recept')

    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    # config = Configurator(root_factory=HelloFactory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    print('kek')
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world,
                    route_name='hello',
                    permission='view')

    # login form
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_view(login, route_name='login')
    config.add_view(logout, route_name='logout')

    # app = config.make_wsgi_app()
    # server = make_server('0.0.0.0', 8080, app)
    # server.serve_forever()
