import os
from mock import patch
import fake_filesystem_unittest
from jinja2 import Environment, PackageLoader
from configuration_generator.module_skeleton import ModuleSkeleton
from configuration_generator.module_files import ModuleFiles


class TestCreateOdooFiles(fake_filesystem_unittest.TestCase):
    """
    Test that the odoo module skeleton is created and files rendered
    - module
    - - __init__.py
    - - __openerp__.py
    - - data
    - - - master_data.xml
    - - static
    - - src
    - - - img
    - - - - trust_logo.ong
    - - - xml
    - - - - view_override.xml
    """

    def setUp(self):
        """
        We're using PyFakeFs to ensure we don't touch the filesystem so need
        to set it up
        """
        # As Jinja will use fake filesystem too need to save the templates
        env = Environment(loader=PackageLoader('configuration_generator',
                                               'templates'))
        self.conf_temp = env.get_template('__openerp__.py.j2')
        self.logo_temp = env.get_template('logo.svg.j2')
        self.data_temp = env.get_template('master_data.xml.j2')
        self.view_temp = env.get_template('view_override.xml.j2')

        def mock_get_template(*args, **kwargs):
            if args[1] == '__openerp__.py.j2':
                return self.conf_temp
            elif args[1] == 'logo.svg.j2':
                return self.logo_temp
            elif args[1] == 'master_data.xml.j2':
                return self.data_temp
            elif args[1] == 'view_override.xml.j2':
                return self.view_temp
            else:
                return None

        self.old_get_template = Environment.get_template
        Environment.get_template = mock_get_template

        # set up fake file system
        self.setUpPyfakefs()

    def tearDown(self):
        super(TestCreateOdooFiles, self).tearDown()
        Environment.get_template = self.old_get_template

    @patch('subprocess.check_output')
    def test_01_create_files(self, mock_check_output):
        """
        Test that the module name is correctly created
        """
        trust_dict = {
            'trust_name': 'Open-eObs',
            'trust_status': 'NHS Trust',
            'trust_email': 'test@gotmail.com',
            'trust_website': 'http://www.website.test'
        }
        ModuleSkeleton('test_module', '/')
        with open('/test_module/static/src/img/trust_logo.png', 'w') as f:
            f.write('')
        ModuleFiles('test_module', '/', trust_dict)
        self.assertTrue(os.path.exists('/test_module/__init__.py'))
        self.assertTrue(os.path.exists('/test_module/__openerp__.py'))
        self.assertTrue(os.path.exists('/test_module/data/master_data.xml'))
        self.assertTrue(
            os.path.exists('/test_module/static/src/xml/view_override.xml')
        )
        self.assertTrue(
            os.path.exists('/test_module/static/src/img/trust_logo.png')
            )