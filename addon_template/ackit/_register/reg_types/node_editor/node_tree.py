import bpy
from bpy import types as bpy_types

from .._base import BTypeBase
from ...._globals import GLOBALS

from .node import Node


DEFAULT_NODETREE_IDENTIFIER = f'{GLOBALS.ADDON_MODULE.lower()}_NodeTree'


node_tree_classes = {}


class NodeTree(BTypeBase):
    ''' Base Class for NodeTree types. '''
    label: str
    icon: str = 'NONE'
    idname: str = DEFAULT_NODETREE_IDENTIFIER

    # NodeType: Node


    def update(self) -> None:
        # print("NodeTree::update()")
        if not hasattr(self, 'nodes'):
            print("WTF? NodeTree has no attribute 'nodes'")
            return
        if len(self.nodes) == 0:
            print("WTF? NodeTree has 0 nodes")
            return

    ###################################

    @classmethod
    def tag_register(deco_cls) -> 'NodeTree':
        node_tree_idname = f'{GLOBALS.ADDON_MODULE.upper()}_NodeCategory_{deco_cls.idname}'

        node_tree = super().tag_register(
            bpy_types.NodeTree, None,
            bl_idname=node_tree_idname,
            bl_label=deco_cls.label,
            bl_icon=deco_cls.icon,
            original_class=deco_cls,
        )

        from .node_cats import new_node_category
        new_node_category(node_tree_idname)

        node_tree_classes[node_tree_idname] = node_tree
        return node_tree
