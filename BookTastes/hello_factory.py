from pyramid.security import Allow


class HelloFactory(object):
    def __init__(self, request):
        self.__acl__ = [
            (Allow, 'vasya', 'view'),
            (Allow, 'group:editors', 'add'),
            (Allow, 'group:editors', 'edit'),
        ]


