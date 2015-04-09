def CreateSubMesh(sourceFace=[]):
    """
    Create a conformal contact mesh.

    Select a contact face from Geometry or specify the name
    as an input argument. The name of the contact face is
    XX_YY###, therefore the submesh is created under mesh XX
    with mesh YY as source mesh.
    """
    sourceFace = GetShape(sourceFace)[0]
    if not sourceFace:
        raise BrowserError("Select an object in Object Browser")

    contactName = sourceFace.GetName()
    # Get SMESH instances
    parentPath = "/Mesh/" + contactName[0:2]
    sourcePath = "/Mesh/" + contactName[3:5]
    parentMeshRef = salome.myStudy.FindObjectByPath(parentPath).GetObject()
    sourceMeshRef = salome.myStudy.FindObjectByPath(sourcePath).GetObject()
    # Get smeshBuilder object
    parentMesh = smesh.Mesh(parentMeshRef)
    sourceMesh = smesh.Mesh(sourceMeshRef)

    parentShape = GetObject(contactName[0:2], "GEOM")
    is3D = IsShape3D(parentShape)
    # Create Projection algorithm
    if is3D:
        projection = parentMesh.Projection1D2D(geom=sourceFace)
        sourceFaceHyp = projection.SourceFace(sourceFace, sourceMesh, None, None, None, None)
        smesh.SetName(sourceFaceHyp, 'Source Face')
    else:
        projection =parentMesh.Projection1D(geom=sourceFace)
        sourceEdgeHyp = projection.SourceEdge(sourceFace, sourceMesh, None, None)
        smesh.SetName(sourceEdgeHyp, 'Source Edge')
    contactMesh = projection.GetSubMesh()
    smesh.SetName(contactMesh, contactName)
    smesh.SetName(projection.GetAlgorithm(), 'Projection')

    # Add mesh groups for Code Aster
    if is3D:
        meshType = SMESH.FACE
    else:
        meshType = SMESH.EDGE
    # Add group to the mesh application
    try:
        meshGroup = parentMesh.GroupOnGeom(sourceFace, contactName, meshType)
        oppositeName = contactName[3:5] + "_" + contactName[0:2] + contactName[5:8]
        opposite = GetObject(oppositeName, "GEOM")
        meshGroup = sourceMesh.GroupOnGeom(opposite, opposite.GetName(), meshType)
    except:
        print "Add group to mesh failed!"

    salome.sg.updateObjBrowser(1)
csm = CreateSubMesh