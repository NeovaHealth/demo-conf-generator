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
        template = self.env.get_template('logo.svg.j2')
        self.assertTrue(isinstance(template, Template),
                        'Logo Template not loaded')

    def test_02_loads_openerp_template(self):
        """
        Test that the __openerp__.py file template loads
        """
        template = self.env.get_template('__openerp__.py.j2')
        self.assertTrue(isinstance(template, Template),
                        '__openerp__.py Template not loaded')

    def test_03_loads_master_data_template(self):
        """
        Test that the master_data.xml file template loads
        """
        template = self.env.get_template('master_data.xml.j2')
        self.assertTrue(isinstance(template, Template),
                        'master_data.xml Template not loaded')

    def test_04_loads_view_override_data_template(self):
        """
        Test that the view_override.xml file template loads
        """
        template = self.env.get_template('view_override.xml.j2')
        self.assertTrue(isinstance(template, Template),
                        'view_override.xml Template not loaded')
