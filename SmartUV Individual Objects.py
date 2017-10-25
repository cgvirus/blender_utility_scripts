#________________________________________________________________________________________#

#A simple Blender script for Smart UV mapping in object mode
#Modified for smart UV in 0-1 uv space for individual object
#You can select all your objects in Object mode and then run the script
#EACH objects will be mapped within 0-1 uv Space 
#Author: Fahad Hasan Pathik (CGVIRUS)

#Recommended addon for running script easily: "Script Runner"
#https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Script_Runner
#Or Blender Text Editor

#________________________________________________________________________________________#


import bpy
lenth = len(bpy.context.selected_objects)
i= 0
for i in range(0,lenth):
    selobj = bpy.context.selected_objects[i]
    bpy.context.scene.objects.active = selobj
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action = 'SELECT')
    bpy.ops.uv.smart_project(stretch_to_bounds=False)
    bpy.ops.uv.pack_islands(margin=0.001)
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.object.mode_set(mode = 'EDIT')
