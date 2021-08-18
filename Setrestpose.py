import bpy

def apply_Rest_Pose_Chnage_Object():
    rig = bpy.context.active_object

    for obj in bpy.data.objects:
        if (obj.type == 'MESH' and
            rig in [m.object for m in obj.modifiers if m.type == 'ARMATURE']
            ):
                
                objectToSelect = bpy.data.objects[obj.name]
                objectToSelect.select_set(True)    
                bpy.context.view_layer.objects.active = objectToSelect
                for mod in bpy.context.object.modifiers:
                    if mod.type == 'ARMATURE':
                        bpy.ops.object.modifier_copy(modifier=mod.name)
                        bpy.ops.object.modifier_apply(modifier=mod.name)
                        bpy.context.object.modifiers.active.name = mod.name
                        bpy.ops.object.select_all(action='DESELECT')
                        
    bpy.context.view_layer.objects.active = rig
    bpy.ops.pose.armature_apply(selected=False)
    
  
    
    
    
#apply_Rest_Pose_Chnage_Object()
