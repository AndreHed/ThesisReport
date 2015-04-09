def CreateGroups(shape=[], edge=True, vertex=False):
    """
    Create groups that were defined in NX.

    Groups defined in NX are included in the STEP file.
    This function identifies these groups and adds them
    to the Object Browser.
    
    Attributes:
        shape -- name of the shape in a list, e.g. ["nameOfShape"]
        vertex -- True if vertex groups should be created
    """
    if not isinstance(shape, list):
        raise InputError("Name of shape should be passes as a list, e.g. ['nameOfShape']")
    shape = GetShape(shape)
    if not shape:
        raise BrowserError("Select an object in Object Browser")

    # Create groups of different types
    try:
        GetNXGroups(shape[0], "SOLID")
        GetNXGroups(shape[0], "FACE")
        if edge:
            GetNXGroups(shape[0], "EDGE")
        if vertex:
            GetNXGroups(shape[0], "VERTEX")
    except IndexError:
        print "Select or specify a shape."
        return
cg = CreateGroups