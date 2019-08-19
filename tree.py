class Tree:
    def __init__(self, value='root', children=None):
        self.value = value
        self.removed = False
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        self.children.append(node)

    def print(self, level=0):
        a = '*' if self.removed else ''
        print('\t' * level + a + self.value + a)
        level += 1
        for tree in self.children:
            tree.print(level)

    def from_database(self, database):
        pass


class DBTreeRepr:
    def __init__(self, raw_data):
        self.__raw_data = raw_data
        self.__root_id = self.get_root_id()
        self.root = self.__raw_data[self.__root_id]
        self.children = []
        self.add_children(self.__root_id, self.children)

    def add_children(self, node_id, children):
        queue = self.__raw_data[node_id].children_ids
        print(queue)
        children.append(self.__raw_data[node_id])
        print(children)
        for element in queue:
            print(self.__raw_data[element].children)
            self.add_children(element, self.__raw_data[element].children)

    def get_root_id(self):
        for element in self.__raw_data:
            if self.__raw_data[element].parent_id is None:
                # print(self.data[element].value)
                return element

    def parse(self, position):
        queue = self.__raw_data[position].children_ids
        print(self.__raw_data[position])
        self.root = self.__raw_data[position]
        for element in queue:
            self.parse(element)  # recursive call

    def fill(self):
        self.parse(self.__root_id)

    def show(self, position, level=0):
        queue = self.__raw_data[position].children_ids
        a = '*' if self.__raw_data[position].deleted else ''
        print('\t' * level + a + self.__raw_data[position].value + a)
        level += 1
        for element in queue:
            self.show(element, level)  # recursive call

    def draw(self):
        self.show(self.__root_id)
