import bpy

def changeDataName():
    for objs in bpy.context.selected_objects:
        objs.data.name = objs.name
        
changeDataName()