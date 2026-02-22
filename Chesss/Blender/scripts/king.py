import bpy

EXPORT_FBX_PATH = None  # e.g. "//Exports/king.fbx"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def shade_smooth(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.shade_smooth()


def join_objects(objs, name):
    for obj in objs:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    objs[0].name = name
    return objs[0]


def set_on_ground(obj):
    bpy.context.view_layer.update()
    min_z = min((obj.matrix_world @ v.co).z for v in obj.data.vertices)
    obj.location.z -= min_z


def build_king():
    objs = []

    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=0.3, location=(0, 0, 0.15))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cone_add(radius1=0.95, radius2=0.35, depth=1.7, location=(0, 0, 1.15))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_torus_add(major_radius=0.65, minor_radius=0.08, location=(0, 0, 1.95))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.22, location=(0, 0, 2.2))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cube_add(size=0.15, location=(0, 0, 2.45))
    v_bar = bpy.context.active_object
    v_bar.scale.x = 0.35
    v_bar.scale.y = 0.08
    v_bar.scale.z = 1.2
    objs.append(v_bar)

    bpy.ops.mesh.primitive_cube_add(size=0.15, location=(0, 0, 2.45))
    h_bar = bpy.context.active_object
    h_bar.scale.x = 1.2
    h_bar.scale.y = 0.08
    h_bar.scale.z = 0.35
    objs.append(h_bar)

    king = join_objects(objs, "King")
    shade_smooth(king)
    set_on_ground(king)
    return king


def export_if_requested(obj):
    if not EXPORT_FBX_PATH:
        return
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(filepath=EXPORT_FBX_PATH, use_selection=True, apply_unit_scale=True)


if __name__ == "__main__":
    clear_scene()
    king = build_king()
    export_if_requested(king)
