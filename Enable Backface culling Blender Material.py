import bpy

def enable_backface:
    for obj in bpy.context.selected_objects:
        for m in obj.material_slots:
            bpy.data.materials[m.name].use_backface_culling = True

def disable_backface:
    for obj in bpy.context.selected_objects:
        for m in obj.material_slots:
            bpy.data.materials[m.name].use_backface_culling = False
            
enable_backface()
#disable_backface()
