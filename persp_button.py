# Persp/Ortho Button by Mr. Spudnik
bl_info = {
    "name": "Persp/Ortho Button",
    "author": "Mr. Spudnik",
    "blender": (2, 79, 0),
	"version": (0, 0, 1),
	"location": "",
	"description": "",
	"warning": "",
    "doc_url": "spudnik3d.blogspot.com",
	"category": "3D View"
	}

import bpy
from bpy.types import Header

class Persp_Button(Header):
    bl_space_type = 'VIEW_3D'

    def draw(self, context):
        layout = self.layout
        layout.separator()
        layout.operator("view3d.view_persportho", text= "Persp/Ortho")
        
def register():
    bpy.utils.register_class(Persp_Button)
    
def unregister():
    bpy.utils.unregister_class(Persp_Button)

if __name__ == "__main__":
    register()  
