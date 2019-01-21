#'''
# CC-BY-NC 2018 EMANUEL DEMETRESCU
# emanuel.demetrescu@gmail.com

#Created by EMANUEL DEMETRESCU

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#'''

bl_info = {
    "name": "3D Survey Collection",
    "author": "Emanuel Demetrescu",
    "version": (1,4.0),
    "blender": (2, 80, 0),
    "location": "3D View > Toolbox",
    "description": "A collection of tools for 3D Survey activities",
#    "warning": "",
    "wiki_url": "",
#    "tracker_url": "",
    "category": "Tools",
    }


if "bpy" in locals():
    import importlib
    importlib.reload(import_3DSC)
#    importlib.reload(functions)
#    importlib.reload(mesh_helpers)
else:
    import math
    import bpy
    from bpy.props import (
            StringProperty,
            BoolProperty,
            FloatProperty,
            EnumProperty,
            IntProperty,
            PointerProperty,
            CollectionProperty,
            )
    from bpy.types import (
            AddonPreferences,
            PropertyGroup,
            )

    from . import (
            UI,
            import_3DSC,
            export_3DSC,
            functions,
            shift,
            QuickUtils,
            LODgenerator,
            ccTool,
            PhotogrTool,
            TexPatcher,
            )

# register
##################################

class InterfaceVars(PropertyGroup):
    cc_nodes: EnumProperty(
        items=[
            ('RGB', 'RGB', 'RGB Curve', '', 0),
            ('BC', 'BC', 'Bright/Contrast', '', 1),
            ('HS', 'HS', 'Hue/Saturation', '', 2),
        ],
        default='RGB'
    )

classes = (
    UI.VIEW3D_PT_Shift_ToolBar,
    UI.VIEW3D_PT_Import_ToolBar,
    UI.VIEW3D_PT_Export_ToolBar,
    UI.VIEW3D_PT_QuickUtils_ToolBar,
    UI.VIEW3D_PT_LODgenerator,
    UI.VIEW3D_PT_ccTool,
    UI.VIEW3D_PT_PhotogrTool,
    UI.VIEW3D_PT_TexPatcher,
    import_3DSC.ImportMultipleObjs,
    import_3DSC.OBJECT_OT_IMPORTPOINTS,
    import_3DSC.ImportCoorPoints,
    export_3DSC.ExportCoordinates,
    export_3DSC.OBJECT_OT_ExportButtonName,
    export_3DSC.OBJECT_OT_ExportObjButton,
    export_3DSC.OBJECT_OT_fbxexp,
    export_3DSC.OBJECT_OT_fbxexportbatch,
    export_3DSC.OBJECT_OT_objexportbatch,
    export_3DSC.OBJECT_OT_osgtexportbatch,
    functions.OBJECT_OT_createcyclesmat,
    functions.OBJECT_OT_savepaintcam,
    shift.OBJECT_OT_IMPORTPOINTS,
    QuickUtils.OBJECT_OT_activatematerial,
    QuickUtils.OBJECT_OT_CenterMass,
    QuickUtils.OBJECT_OT_CorrectMaterial,
    QuickUtils.OBJECT_OT_createpersonalgroups,
    QuickUtils.OBJECT_OT_cycles2bi,
    QuickUtils.OBJECT_OT_deactivatematerial,
    QuickUtils.OBJECT_OT_lightoff,
    QuickUtils.OBJECT_OT_LocalTexture,
    QuickUtils.OBJECT_OT_LOD0polyreducer,
    QuickUtils.OBJECT_OT_multimateriallayout,
    QuickUtils.OBJECT_OT_objectnamefromfilename,
    QuickUtils.OBJECT_OT_projectsegmentation,
    QuickUtils.OBJECT_OT_projectsegmentationinversed,
    QuickUtils.OBJECT_OT_removealluvexcept1,
    QuickUtils.OBJECT_OT_removefromallgroups,
    QuickUtils.OBJECT_OT_renameGEobject,
    QuickUtils.OBJECT_OT_tiff2pngrelink,
    LODgenerator.OBJECT_OT_CreateGroupsLOD,
    LODgenerator.OBJECT_OT_ExportGroupsLOD,
    LODgenerator.OBJECT_OT_LOD0,
    LODgenerator.OBJECT_OT_LOD1,
    LODgenerator.OBJECT_OT_LOD2,
    LODgenerator.OBJECT_OT_RemoveGroupsLOD,
    PhotogrTool.OBJECT_OT_applypaintcam,
    PhotogrTool.OBJECT_OT_BetterCameras,
    PhotogrTool.OBJECT_OT_Canon6D14,
    PhotogrTool.OBJECT_OT_Canon6D24,
    PhotogrTool.OBJECT_OT_Canon6D35,
    PhotogrTool.OBJECT_OT_Canon6Dscene,
    PhotogrTool.OBJECT_OT_IsometricScene,
    PhotogrTool.OBJECT_OT_nikond320018mm,
    PhotogrTool.OBJECT_OT_nikond3200scene,
    PhotogrTool.OBJECT_OT_NoBetterCameras,
    PhotogrTool.OBJECT_OT_paintcam,
    TexPatcher.OBJECT_OT_applyoritexset,
    TexPatcher.OBJECT_OT_applysptexset,
    TexPatcher.OBJECT_OT_exitsetup,
    TexPatcher.OBJECT_OT_paintsetup,
    TexPatcher.OBJECT_OT_removepaintsetup,
    TexPatcher.OBJECT_OT_textransfer,
    InterfaceVars
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.WindowManager.interface_vars = bpy.props.PointerProperty(type=InterfaceVars)

#def initSceneProperties(scn):
    bpy.types.Scene.LODnum = IntProperty(
        name = "LODs", 
        default = 0,
        min = 0,
        max = 3,
        description = "Enter desired number of LOD (Level of Detail)")
    
    bpy.types.Scene.BL_undistorted_path = StringProperty(
      name = "Undistorted Path",
      default = "",
      description = "Define the root path of the undistorted images",
      subtype = 'DIR_PATH'
      )
      
    bpy.types.Scene.BL_x_shift = FloatProperty(
      name = "X shift",
      default = 0.0,
      description = "Define the shift on the x axis",
      )

    bpy.types.Scene.BL_y_shift = FloatProperty(
      name = "Y shift",
      default = 0.0,
      description = "Define the shift on the y axis",
      )

    bpy.types.Scene.BL_z_shift = FloatProperty(
      name = "Z shift",
      default = 0.0,
      description = "Define the shift on the z axis",
      )

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)