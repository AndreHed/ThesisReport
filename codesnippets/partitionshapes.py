def PartitionShapes(shapes=[]):
    """
    Partition shapes, identify contact groups and create group tree.

    Attributes:
        shapes -- list of shapes that should be partitioned
    """
    if not isinstance(shapes, list):
        raise InputError("Name of shape should be passes as a list, e.g. ['shape1','shape2']")
    shapes = GetShape(shapes)
    if not shapes:
        raise BrowserError("Select an object in Object Browser")

    # Make a partition of the imported object
    if IsShape3D(shapes[0]):
        partition = geompy.MakePartition(shapes, [], [], [], geompy.ShapeType["SOLID"], 0, [], 0, "partition")
    else:
        partition = geompy.MakePartition(shapes, [], [], [], geompy.ShapeType["FACE"], 0, [], 0, "partition")
    # Add all groups of shapes to partition
    for shape in shapes:
        groups = geompy.GetGroups(shape)
        groups.append(shape)
        allGroups = geompy.RestoreGivenSubShapes(partition, groups, GEOM.FSM_GetInPlace, True, False)
        # Delete groups that where copied to partition
        groups.pop()
        for group in groups:
            salome.geom.geomtools.GeomStudyTools().deleteShape(salome.ObjectToID(group))
    groups = geompy.GetGroups(partition)

    CreateTreeStructure(groups)
    RemoveContactGroups(partition)

    salome.sg.updateObjBrowser(1)
ps = PartitionShapes