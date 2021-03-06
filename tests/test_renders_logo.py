import unittest
from jinja2 import Environment, PackageLoader
import xml.etree.ElementTree as Et


class TestRendersLogo(unittest.TestCase):
    """
    Test that the Jinja template for logo.svg is rendered correctly
    """

    def setUp(self):
        """
        We're always going to need the env & template loaded
        """
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))
        self.template = self.env.get_template('logo.svg.j2')

    def test_01_renders_logo_with_trust_name_and_status(self):
        """
        Test that the logo SVG is rendered correctly
        """
        test_name = 'Open-eObs'
        test_status = 'NHS Trust'
        logo = self.template.render(trust_name=test_name,
                                    trust_status=test_status,
                                    svg_width=745,
                                    text_width=520,
                                    logo_offset=545)
        svg = Et.fromstring(logo)
        rendered_name = svg.findall('./g/text/[@id="trust_name"]')[0]
        rendered_status = svg.findall('./g/text/[@id="trust_status"]')[0]
        self.assertEqual(rendered_name.text.strip().replace('\n', ''),
                         test_name,
                         'Name incorrectly rendered')
        self.assertEqual(rendered_status.text.strip().replace('\n', ''),
                         test_status,
                         'Status incorrectly rendered')
