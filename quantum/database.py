import uuid


class DBNode:
    def __init__(self, value, parent_node=None):
        self.value = value
        self.deleted = False
        self.__id = str(uuid.uuid1())
        self.__parent_id = None
        self.__children_ids = []

        if parent_node:
            self.__parent_id = parent_node.id

            if self.__id not in parent_node.children_ids:
                parent_node.children_ids.append(self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def parent_id(self):
        return self.__parent_id

    @parent_id.setter
    def parent_id(self, value):
        if value is not None:
            self.__parent_id = value

    @property
    def children_ids(self):
        return self.__children_ids

    @children_ids.setter
    def children_ids(self, value):
        # return self.__children_ids
        self.__children_ids.append(value)


class DatabaseInterface:
    def get_all(self):
        pass

    def get_by_id(self, node_id):
        pass


class DatabaseInterfaceImpl(DatabaseInterface):
    def __init__(self):
        self.data = {}

    def get_all(self):
        self.fake_values()
        return self.data

    def get_by_id(self, node_id):
        for element in self.data:
            if element.id == node_id:
                return element

    def add_node(self, node):
        self.data[node.id] = node

    def fake_values(self):

        root = DBNode('Root')

        node0 = DBNode('Node0', root)
        node1 = DBNode('Node1', root)
        node2 = DBNode('Node2', root)

        node10 = DBNode('node10', node1)
        node11 = DBNode('node10', node1)
        node12 = DBNode('node12', node1)
        node13 = DBNode('node13', node1)

        node120 = DBNode('node120', node12)
        node121 = DBNode('node121', node12)
        node122 = DBNode('node122', node12)
        node123 = DBNode('node123', node12)

        node1200 = DBNode('node1201', node120)
        node1201 = DBNode('node1201', node120)
        node1202 = DBNode('node1202', node120)
        node1203 = DBNode('node1203', node120)

        self.add_node(root)

        self.add_node(node0)
        self.add_node(node1)
        self.add_node(node2)

        self.add_node(node10)
        self.add_node(node11)
        self.add_node(node12)
        self.add_node(node13)

        self.add_node(node120)
        self.add_node(node121)
        self.add_node(node122)
        self.add_node(node123)

        self.add_node(node1200)
        self.add_node(node1201)
        self.add_node(node1202)
        self.add_node(node1203)
