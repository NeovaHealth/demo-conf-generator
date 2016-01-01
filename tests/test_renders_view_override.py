import unittest
from jinja2 import Environment, PackageLoader
import xml.etree.ElementTree as Et


class TestRendersViewOverride(unittest.TestCase):
    """
    Test that the Jinja template for view_override.xml is rendered correctly
    """

    def setUp(self):
        """
        We're always going to need the env & template loaded
        """
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))
        self.template = self.env.get_template('view_override.xml.j2')

    def test_01_renders_view_override_with_module_name(self):
        """
        Test that the module name is rendered correctly in the template
        """
        test_module = 'test_trust'
        data = self.template.render(module_name=test_module)
        svg = Et.fromstring(data)
        rendered_img = svg.findall('./t/t/div/img')[0]
        rendered_img_src = rendered_img.get('src')
        self.assertEqual(
            rendered_img_src,
            '/{0}/static/src/img/trust_logo.png'.format(
                test_module
            ),
            'Name incorrectly rendered'
        )
