from database import DatabaseInterfaceImpl
from tree import Tree


database = DatabaseInterfaceImpl()

our_tree = Tree('Root', [
                        Tree('node0'),
                        Tree('node1', [
                                       Tree('node10'),
                                       Tree('node10'),
                                       Tree('node12', [
                                                      Tree('node120', [
                                                                      Tree('node1200'),
                                                                      Tree('node1201'),
                                                                      Tree('node1202'),
                                                                      Tree('node1203')
                                                                      ]),
                                                      Tree('node121'),
                                                      Tree('node122'),
                                                      Tree('node123')
                                                      ]),
                                       Tree('node13')
                                       ]),
                        Tree('node2')
                        ])

print('='*80)
our_tree.print()


test = 1
