def MoveContactGroup(contact, groups):
    name = contact.GetName()
    # Check if objects's name has format: XX_YY###
    try:
        isContact = name[2]
    except IndexError:
        # Ignore names shorter than three characters
        isContact = ""
    if isContact == "_":
        # Get the type of contact
        groupType = geompy.GetType(contact)
        # 'contact' is a group, get the shapes of this group
        contactShapes = geompy.SubShapeAllSortedCentres(contact, groupType)
        for parent in groups[:]:
            try:
                parentName = parent.GetName()
            except:
                print "Couldn't get name of GEOM object."
                parentName = None
            if name[0:2] == parentName:
                # Add a sub-group to parent, containing the
                # shapes in contact
                newGroup = AddGroup(parent, contactShapes, groupType, name)
                groups.append(newGroup)
                # Remove old contact group
                groups.remove(contact)
            if name[3:5] == parentName:
                # New contact name
                contactName = name[3:5] + "_" + name[0:2] + name[5:8]
                # Add a sub-group to parent, containing the
                # shapes in contact
                newGroup = AddGroup(parent, contactShapes, groupType, contactName)
                groups.append(newGroup)