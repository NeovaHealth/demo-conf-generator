import unittest
from jinja2 import Environment, PackageLoader


class TestRendersOpenerp(unittest.TestCase):
    """
    Test that the Jinja template for __openerp__.py is rendered correctly
    """

    def setUp(self):
        """
        We're always going to need the env & template loaded
        """
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))
        self.template = self.env.get_template('__openerp__.py.j2')

    def test_01_renders_openerp_with_trust_name_and_status(self):
        """
        Test that the trust details are rendered correctly in the template
        """
        test_name = 'Open-eObs'
        test_status = 'NHS Trust'
        data = self.template.render(trust_name=test_name,
                                    trust_status=test_status)
        data_parts = data.split('\n')
        rejoined_data = ''.join(data_parts[1:])
        conf = eval(rejoined_data)
        desc = conf['description']
        name = conf['name']
        self.assertEqual(desc, 'Configuration for {0} {1}'.format(test_name,
                                                                  test_status),
                         'Incorrect description rendered')
        self.assertEqual(name, '{0} Open-eObs Configuration'.format(test_name),
                         'Incorrect name rendered')
