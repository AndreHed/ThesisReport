def GetNXGroups(shape, groupType):
    """
    Return groups that are defined in NX.

    Attributes:
        shape -- object to get groups from (not a list of objects)
        groupType -- SOLID, FACE, EDGE or VERTEX
    """
    # Extract all groups from shape
    try:
        objects = geompy.ExtractShapes(shape, geompy.ShapeType[groupType], True)
    except:
        print "Shape could not be extracted.", shape
        raise

    for obj in objects[:]:
        # Add objects to study to get NX names
        geompy.addToStudyInFather(shape, obj, "")
        # Delete objects with lower case letters
        if obj.GetName() != obj.GetName().upper():
            salome.geom.geomtools.GeomStudyTools().deleteShape(salome.ObjectToID(obj))
            salome.sg.updateObjBrowser(1)
            objects.remove(obj)

    # Sort the remaining objects based on name
    objects.sort(key=lambda obj: obj.GetName())

    # For objects with equal names create a group
    group = []
    for obj in objects:  
        # Add object to 'group' if list is empty or the name
        # of the object is the same as the previous object
        if not group or obj.GetName()==group[-1].GetName():
            group.append(obj)
        else:
            AddGroup(shape, group, groupType, group[-1].GetName())
            group = [obj]
    if group:
        AddGroup(shape, group, groupType, group[-1].GetName())

    # Delete the objects from the object browser
    for obj in objects:
        salome.geom.geomtools.GeomStudyTools().deleteShape(salome.ObjectToID(obj))
    salome.sg.updateObjBrowser(1)