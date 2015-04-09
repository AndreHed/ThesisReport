def CreateMesh(shape=[], minSize=10, maxSize=50):
    """
    Mesh the selected or specified object.

    This function creates a mesh for a given shape. The shape can either be
    selected in the Object Browser or given as a parameter.
    
    Attributes:
        shape -- name of the shape in a list, e.g. ["nameOfShape"]
    """
    if not isinstance(shape, list):
        raise InputError("Name of shape should be passes as a list, e.g. ['shape1','shape2']")
    shape = GetShape(shape)[0]
    if not shape:
        raise BrowserError("Select an object in Object Browser")

    groups = geompy.GetGroups(shape)
    # Create mesh
    mesh = smesh.Mesh(shape)
    smesh.SetName(mesh.GetMesh(), shape.GetName())
    # Create algorithm and hypothesis
    is3D = IsShape3D(shape)
    [NETGEN, parameters] = CreateAlgorithm(mesh, groups, is3D, minSize, maxSize)
    
    salome.sg.updateObjBrowser(1)
cm = CreateMesh