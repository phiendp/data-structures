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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return False

    if user in group.users:
        return True

    for group in group.groups:
        return is_user_in_group(user, group)
    return False


def active_directory_specs():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    parent_user = "superuser"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_user(parent_user)

    assert is_user_in_group(parent_user, None) == False, "None group should return false"
    assert is_user_in_group(None, parent) == False, "None user should return false"
    assert is_user_in_group(sub_child_user, parent), "User not found in subgroup!"
    assert is_user_in_group(sub_child_user, sub_child), "User not found in same group!"
    assert is_user_in_group(parent_user, sub_child) == False, "User is only in super group!"

    print("Tests passed!")


if __name__ == "__main__":
    active_directory_specs()
