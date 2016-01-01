import unittest
from jinja2 import Environment, PackageLoader, Template


class TestTemplateLoading(unittest.TestCase):
    """
    Test that the Jinja templates are found
    """

    def setUp(self):
        """
        We're always going to need the env loaded
        """
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))

    def test_01_loads_logo_template(self):
        """
        Test that the logo template loads
        """
        template = self.env.get_template('logo.svg')
        self.assertTrue(isinstance(template, Template),
                        'Logo Template not loaded')
