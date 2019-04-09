
from unittest import TestCase
from peco.template import Scope

class TestScope (TestCase):
  
  def test_access_value1 (self):
    value = "example value."
    scope = Scope()
    self.assertEqual(scope.get_value("a", defaultvalue=None), None) # test
    scope.set_value("a", value)
    self.assertEqual(scope.get_value("a"), value)
  
  def test_access_value2 (self):
    value1 = "example value."
    scope = Scope()
    scope.set_value("a", value1)
    with scope:
      value2 = "example value2."
      scope.set_value("a", value2)
      self.assertEqual(scope.get_value("a"), value2)
    self.assertEqual(scope.get_value("a"), value1)
  