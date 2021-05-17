import bpy

sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
for obj in sel_objs:
    bpy.context.view_layer.objects.active = obj
    bpy.ops.mesh.customdata_custom_splitnormals_add()
