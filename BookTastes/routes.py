def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('recepts', '/recepts')
    config.add_route('collection', '/collection')
    config.add_route('recept_view', '/recepts/{id:\w+}')
