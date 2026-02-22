import bpy

EXPORT_FBX_PATH = None  # e.g. "//Exports/pawn.fbx"


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


def build_pawn():
    objs = []

    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=0.25, location=(0, 0, 0.125))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_torus_add(major_radius=0.85, minor_radius=0.07, location=(0, 0, 0.25))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.6, depth=1.0, location=(0, 0, 0.85))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.45, depth=0.2, location=(0, 0, 1.35))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.45, location=(0, 0, 1.8))
    objs.append(bpy.context.active_object)

    pawn = join_objects(objs, "Pawn")
    shade_smooth(pawn)
    set_on_ground(pawn)
    return pawn


def export_if_requested(obj):
    if not EXPORT_FBX_PATH:
        return
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(filepath=EXPORT_FBX_PATH, use_selection=True, apply_unit_scale=True)


if __name__ == "__main__":
    clear_scene()
    pawn = build_pawn()
    export_if_requested(pawn)
