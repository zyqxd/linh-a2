# TODO: put all your tests in this file (you can delete this line)

# TODO(linh) For class Group
def test_get_members_shallow_copy(self, group) -> None:
  assert id(group.get_members()) != id(group._members)

# TODO(linh) For class Grouping
def test_get_groups_shallow_copy(self, groupings) -> None:
  assert id(groupings.get_groups()) != id(groupings._groups)