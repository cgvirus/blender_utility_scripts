import bpy

ob = bpy.context.active_object

vgroup_A = ob.vertex_groups.active
vgroup_B = bpy.context.active_object.vertex_groups[-1]

if vgroup_A.name and vgroup_B.name in ob.vertex_groups:
    
    vgroup = vgroup_B
    
    for id, vert in enumerate(ob.data.vertices):
        available_groups = [v_group_elem.group for v_group_elem in vert.groups]
        A = B = 0
        if ob.vertex_groups[vgroup_A.name].index in available_groups:
            A = ob.vertex_groups[vgroup_A.name].weight(id)
        if ob.vertex_groups[vgroup_B.name].index in available_groups:
            B = ob.vertex_groups[vgroup_B.name].weight(id)
        
        if len(vert.groups):
            for g in vert.groups:
                if ob.vertex_groups[g.group].name in [vgroup_A.name, vgroup_B.name]:
                    vgroup.add([id], A+B ,'ADD')
                    
# Select the last index
#ob.vertex_groups.active_index = vgroup_B.index
