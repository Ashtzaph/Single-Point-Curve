bl_info = {
    "name": "Single Point Curve",
    "author": "Amir Diab (or Ashtzaph)",
    "version": (1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Add > Curve",
    "description": "Adds a single control point with collapsed handles",
    "category": "Add Curve",
    "doc_url": "https://github.com/Ashtzaph/Single-Point-Curve/new/main",
    "tracker_url": "https://github.com/Ashtzaph/Single-Point-Curve/issues",
}

import bpy
from .operators import ADD_SINGLE_POINT_CURVE

def menu_func(self, context):
    self.layout.operator(ADD_SINGLE_POINT_CURVE.bl_idname, text="Single Point")

def register():
    bpy.utils.register_class(ADD_SINGLE_POINT_CURVE)
    bpy.types.VIEW3D_MT_curve_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ADD_SINGLE_POINT_CURVE)
    bpy.types.VIEW3D_MT_curve_add.remove(menu_func)

if __name__ == "__main__":
    register()
