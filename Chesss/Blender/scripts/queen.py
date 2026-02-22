import bpy
import math

EXPORT_FBX_PATH = None  # e.g. "//Exports/queen.fbx"


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


def build_queen():
    objs = []

    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=0.3, location=(0, 0, 0.15))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_cone_add(radius1=0.9, radius2=0.3, depth=1.6, location=(0, 0, 1.1))
    objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_torus_add(major_radius=0.65, minor_radius=0.08, location=(0, 0, 1.85))
    objs.append(bpy.context.active_object)

    crown_radius = 0.65
    for i in range(6):
        angle = math.radians(i * 60)
        x = crown_radius * math.cos(angle)
        y = crown_radius * math.sin(angle)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(x, y, 2.05))
        objs.append(bpy.context.active_object)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(0, 0, 2.25))
    objs.append(bpy.context.active_object)

    queen = join_objects(objs, "Queen")
    shade_smooth(queen)
    set_on_ground(queen)
    return queen


def export_if_requested(obj):
    if not EXPORT_FBX_PATH:
        return
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(filepath=EXPORT_FBX_PATH, use_selection=True, apply_unit_scale=True)


if __name__ == "__main__":
    clear_scene()
    queen = build_queen()
    export_if_requested(queen)
