import bpy
import math

EXPORT_FBX_PATH = None  # e.g. "//Exports/knight.fbx"


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


def build_knight():
    objs = []

    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=0.3, location=(0, 0, 0.15))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.75, depth=1.0, location=(0, 0, 0.8))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cone_add(radius1=0.6, radius2=0.2, depth=1.0,
                                    location=(0, 0, 1.4), rotation=(math.radians(20), 0, 0))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.4, location=(0, 0.2, 1.85))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cube_add(size=0.4, location=(0, 0.5, 1.75))
    muzzle = bpy.context.active_object
    muzzle.scale.x = 0.7
    muzzle.scale.y = 1.2
    muzzle.scale.z = 0.5
    objs.append(muzzle)

    bpy.ops.mesh.primitive_cone_add(radius1=0.08, radius2=0.02, depth=0.3,
                                    location=(0.15, 0.1, 2.2), rotation=(math.radians(20), 0, math.radians(20)))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cone_add(radius1=0.08, radius2=0.02, depth=0.3,
                                    location=(-0.15, 0.1, 2.2), rotation=(math.radians(20), 0, math.radians(-20)))
    objs.append(bpy.context.active_object)

    knight = join_objects(objs, "Knight")
    shade_smooth(knight)
    set_on_ground(knight)
    return knight


def export_if_requested(obj):
    if not EXPORT_FBX_PATH:
        return
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(filepath=EXPORT_FBX_PATH, use_selection=True, apply_unit_scale=True)


if __name__ == "__main__":
    clear_scene()
    knight = build_knight()
    export_if_requested(knight)
