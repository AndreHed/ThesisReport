def MoveOtherGroups(group, groups):
    oldGroups = []
    for parent in groups:
        name = group.GetName()
        # Check if objects's name has format: XX_YY###
        try:
            isContact = name[2]
        except IndexError:
            # Ignore names shorter than three characters
            isContact = ""
        # Move groups XXGROUP to XX, and ignore XX_YY and XX
        if name[0:2] == parent.GetName() and isContact != "_" and name != parent.GetName():
            # Get the type of group
            groupType = geompy.GetType(group)
            # Get the shapes of 'group'
            subShapes = geompy.SubShapeAllSortedCentres(group, groupType)
            # Add a sub-group to parent, containing the
            # shapes in group
            newGroup = AddGroup(parent, subShapes, groupType, name)
            groups.append(newGroup)
            # Remove old group group
            oldGroups.append(group)
            groups.remove(group)
    return oldGroups