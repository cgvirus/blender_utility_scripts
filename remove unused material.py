import bpy

for ob in bpy.context.selected_objects:
    ob= bpy.context.active_object
    bpy.ops.object.material_slot_remove_unused()
