def CreateAlgorithm(mesh, groups, is3D, minSize, maxSize):
    if is3D:
        NETGEN = mesh.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
    else:
        NETGEN = mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)

    parameters = NETGEN.Parameters()
    parameters.SetMaxSize(maxSize)
    parameters.SetMinSize(minSize)
    parameters.SetSecondOrder(1) # Second order elements
    parameters.SetOptimize(1)    # Optimize activated
    parameters.SetFineness(5)    # Set finess to Custom
    parameters.SetFuseEdges(1)   # Fuse activated
    parameters.SetQuadAllowed(0) # Quadrangles deacativated
    parameters.SetGrowthRate(0.3)
    parameters.SetUseSurfaceCurvature(0)
    parameters.SetNbSegPerEdge(0.2)
    parameters.SetNbSegPerRadius(0.2)
    # Add local sizes
    AddLocalSize(parameters, groups)
    # Set name of algorithm and hypothesis
    smesh.SetName(parameters, "NETGEN")
    smesh.SetName(NETGEN.GetAlgorithm(), "NETGEN")
    return [NETGEN, parameters]