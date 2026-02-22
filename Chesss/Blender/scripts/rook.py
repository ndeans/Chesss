import bpy
import math

EXPORT_FBX_PATH = None  # e.g. "//Exports/rook.fbx"


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


def build_rook():
    objs = []

    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=0.3, location=(0, 0, 0.15))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.8, depth=1.2, location=(0, 0, 0.9))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.6, depth=0.2, location=(0, 0, 1.5))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.95, depth=0.25, location=(0, 0, 1.75))
    objs.append(bpy.context.active_object)

    crenel_radius = 0.65
    crenel_size = 0.25
    for i in range(4):
        angle = math.radians(45 + i * 90)
        x = crenel_radius * math.cos(angle)
        y = crenel_radius * math.sin(angle)
        bpy.ops.mesh.primitive_cube_add(size=crenel_size, location=(x, y, 2.0))
        objs.append(bpy.context.active_object)

    rook = join_objects(objs, "Rook")
    shade_smooth(rook)
    set_on_ground(rook)
    return rook


def export_if_requested(obj):
    if not EXPORT_FBX_PATH:
        return
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(filepath=EXPORT_FBX_PATH, use_selection=True, apply_unit_scale=True)


if __name__ == "__main__":
    clear_scene()
    rook = build_rook()
    export_if_requested(rook)
