import open3d as o3d

if __name__ == "__main__":
    pcd1 = o3d.io.read_point_cloud("data-1.pcd")
    pcd2 = o3d.io.read_point_cloud("data-2.pcd").translate((0, 0, 150))
    pcd3 = o3d.io.read_point_cloud("data-3.pcd").translate((0, 0, 300))
    o3d.visualization.draw_geometries([pcd1, pcd2, pcd3])
