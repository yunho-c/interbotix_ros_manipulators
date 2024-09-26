import trimesh
import glob

stl_files = glob.glob("./*.stl")
for file in stl_files:
    # print(file)
    mesh = trimesh.load(str(file))
    obj_fn = file.replace(".stl", ".obj")
    try:
        mesh.export(str(obj_fn))
    except Exception as e: print(f"Error while processing {file}: {e}")
