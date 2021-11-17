#
# Active Directory
#

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    '''steps:
    check if user in current group users list.
    if not check if user is in any of the sub groups users list
    '''
    if user is None or group is None:
        return False
        
    if user in group.get_users():
        return True

    in_subgroup = False
    for sub_group in group.get_groups():
        in_subgroup = is_user_in_group(user, sub_group)
        if in_subgroup:
            break

    return in_subgroup

#
# MAIN
#

if __name__ == "__main__":
    child_user2 = "child user 2"

    print(f"Test0: is_user_in_group(sub_child_user, child)")
    # True
    print(is_user_in_group(sub_child_user, child))

    print(f"Test1: is_user_in_group(sub_child_user, parent)")
    # True
    print(is_user_in_group(sub_child_user, parent))

    print(f"Test2: is_user_in_group(sub_child_user2, parent)")
    # False
    print(is_user_in_group(child_user2, parent))

    print(f"Test3: is_user_in_group(None, parent)")
    # False
    print(is_user_in_group(None, parent))

    print(f"Test4: is_user_in_group(child, None)")
    # False
    print(is_user_in_group(child, None))