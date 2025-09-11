from domain.Category import Category


class Object:


    def __init__(self, id_object, description, state, category):
        self._id_object = id_object
        self._description = description
        self._state = state
        self._category = category


    @property
    def id_object(self):
        return self._id_object

    @id_object.setter
    def id_object(self, id_object):
        self._id_object = id_object

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def state(self):
        return self._state


    @state.setter
    def state(self, state):
        self._state = state

    @property
    def category(self):
        return self._category


    @category.setter
    def category(self, category):
        self._category = category