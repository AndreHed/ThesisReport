def CreateTreeStructure(groups):
    """
    Create a tree structure where contact groups are
    sub-groups of parents.
    """
    for group in groups[:]:
        MoveContactGroup(group, groups)
        oldGroups = MoveOtherGroups(group, groups)
        RemoveOtherGroups(oldGroups)
    return groups