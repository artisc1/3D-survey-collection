import bpy

from bpy.types import Panel
from bpy.types import Operator
from bpy.types import PropertyGroup


import os
from bpy_extras.io_utils import ImportHelper

from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       CollectionProperty
                       )

class ToolsPanelImport:
    bl_label = "Importers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        self.layout.operator("import_scene.multiple_objs", icon="WORLD_DATA", text='Import multiple objs')
        row = layout.row()
        self.layout.operator("import_points.txt", icon="WORLD_DATA", text='Import txt points')


class VIEW3D_PT_Import_ToolBar(Panel, ToolsPanelImport):
    bl_category = "3DSC"
    bl_idname = "VIEW3D_PT_Import_ToolBar"
    bl_context = "objectmode"
