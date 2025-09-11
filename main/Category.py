


class Category:


    def __init__(self, id_category, description):
        self.id_category = id_category
        self.description = description

    @property
    def category(self):
        return self.id_category

    @category.setter
    def category(self, category):
        self.category = category


    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description