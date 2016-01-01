import unittest
from jinja2 import Environment, PackageLoader
import xml.etree.ElementTree as Et


class TestRendersMasterData(unittest.TestCase):
    """
    Test that the Jinja template for master_data.xml is rendered correctly
    """

    def setUp(self):
        """
        We're always going to need the env & template loaded
        """
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))
        self.template = self.env.get_template('master_data.xml.j2')

    def test_01_renders_master_data_with_trust_details(self):
        """
        Test that the master data is rendered with the correct details
        """
        test_name = 'Open-eObs'
        test_email = 'test@gotmail.com'
        test_website = 'http://www.website.test'
        test_encoded_image = 'DDDDDDDddddddropTheBass'
        data = self.template.render(trust_name=test_name,
                                    trust_email=test_email,
                                    trust_website=test_website,
                                    trust_logo_encoded=test_encoded_image)
        svg = Et.fromstring(data)
        xpath_temp = './data/record[@model="{0}"]/field[@name="{1}"]'
        rendered_comp_name = svg.findall(xpath_temp.format('res.company',
                                                           'name'))[0]
        rendered_partner_name = svg.findall(xpath_temp.format('res.partner',
                                                              'name'))[0]
        rendered_partner_email = svg.findall(xpath_temp.format('res.partner',
                                                               'email'))[0]
        rendered_partner_site = svg.findall(xpath_temp.format('res.partner',
                                                              'website'))[0]
        rendered_partner_logo = svg.findall(xpath_temp.format('res.partner',
                                                              'image'))[0]
        self.assertEqual(rendered_comp_name.text.strip().replace('\n', ''),
                         test_name,
                         'Company Name incorrectly rendered')
        self.assertEqual(rendered_partner_name.text.strip().replace('\n', ''),
                         test_name,
                         'Partner Name incorrectly rendered')
        self.assertEqual(rendered_partner_email.text.strip().replace('\n', ''),
                         test_email,
                         'Partner Email incorrectly rendered')
        self.assertEqual(rendered_partner_site.text.strip().replace('\n', ''),
                         test_website,
                         'Partner Website incorrectly rendered')
        self.assertEqual(rendered_partner_logo.text.strip().replace('\n', ''),
                         test_encoded_image,
                         'Partner Logo incorrectly rendered')
