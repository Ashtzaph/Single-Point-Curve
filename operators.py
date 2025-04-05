import bpy

class ADD_SINGLE_POINT_CURVE(bpy.types.Operator):
    """Add a single control point with zero-length handles"""
    bl_idname = "curve.single_point_add"
    bl_label = "Single Point"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Create new curve data
        curve_data = bpy.data.curves.new(name="SinglePoint", type='CURVE')
        curve_data.dimensions = '3D'
        
        # Add new spline with single point
        spline = curve_data.splines.new('BEZIER')
        
        # Get reference to the single point
        point = spline.bezier_points[0]
        
        # Configure the single point
        point.co = (0, 0, 0)
        point.handle_left = point.co
        point.handle_right = point.co
        point.handle_left_type = 'VECTOR'
        point.handle_right_type = 'VECTOR'
        
        # Create object and link to scene
        curve_obj = bpy.data.objects.new("SinglePoint", curve_data)
        curve_obj.location = context.scene.cursor.location
        
        # Link to collection and make active
        context.collection.objects.link(curve_obj)
        context.view_layer.objects.active = curve_obj
        curve_obj.select_set(True)
        
        return {'FINISHED'}
