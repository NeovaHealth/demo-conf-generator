import os
import fake_filesystem_unittest
from configuration_generator.module_skeleton import ModuleSkeleton


class TestCreateOdooModuleSkeleton(fake_filesystem_unittest.TestCase):
    """
    Test that the odoo module skeleton is created
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
        self.setUpPyfakefs()

    def test_01_create_module_directory(self):
        """
        Test that the module name is correctly created
        """
        self.assertFalse(os.path.isdir('/test_module'))
        self.assertFalse(os.path.isdir('/test_module/data'))
        self.assertFalse(os.path.isdir('/test_module/static'))
        self.assertFalse(os.path.isdir('/test_module/static/src'))
        self.assertFalse(os.path.isdir('/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('/test_module/static/src/img'))
        ModuleSkeleton('test_module', '')
        self.assertTrue(os.path.isdir('/test_module'))
        self.assertTrue(os.path.isdir('/test_module/data'))
        self.assertFalse(os.path.isdir('/test_module/data/data'))
        self.assertTrue(os.path.isdir('/test_module/static'))
        self.assertFalse(os.path.isdir('/test_module/static/static'))
        self.assertTrue(os.path.isdir('/test_module/static/src'))
        self.assertFalse(os.path.isdir('/test_module/static/src/src'))
        self.assertTrue(os.path.isdir('/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('/test_module/static/src/xml/xml'))
        self.assertTrue(os.path.isdir('/test_module/static/src/img'))
        self.assertFalse(os.path.isdir('/test_module/static/src/img/img'))

    def test_02_create_module_in_same_directory(self):
        """
        Test that given just a module name it puts the folder in the current
        directory
        """
        self.assertFalse(os.path.isdir('test_module'))
        self.assertFalse(os.path.isdir('test_module/data'))
        self.assertFalse(os.path.isdir('test_module/static'))
        self.assertFalse(os.path.isdir('test_module/static/src'))
        self.assertFalse(os.path.isdir('test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('test_module/static/src/img'))
        ModuleSkeleton('test_module')
        self.assertTrue(os.path.isdir('test_module'))
        self.assertTrue(os.path.isdir('test_module/data'))
        self.assertFalse(os.path.isdir('test_module/data/data'))
        self.assertTrue(os.path.isdir('test_module/static'))
        self.assertFalse(os.path.isdir('test_module/static/static'))
        self.assertTrue(os.path.isdir('test_module/static/src'))
        self.assertFalse(os.path.isdir('test_module/static/src/src'))
        self.assertTrue(os.path.isdir('test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('test_module/static/src/xml/xml'))
        self.assertTrue(os.path.isdir('test_module/static/src/img'))
        self.assertFalse(os.path.isdir('test_module/static/src/img/img'))
        
    def test_03_create_module_in_top_level_directory(self):
        """
        Test that given just a module name it puts the folder in the current
        directory
        """
        self.assertFalse(os.path.isdir('/opt/test_module'))
        self.assertFalse(os.path.isdir('/opt/test_module/data'))
        self.assertFalse(os.path.isdir('/opt/test_module/static'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src/img'))
        ModuleSkeleton('test_module', '/opt')
        self.assertTrue(os.path.isdir('/opt/test_module'))
        self.assertTrue(os.path.isdir('/opt/test_module/data'))
        self.assertFalse(os.path.isdir('/opt/test_module/data/data'))
        self.assertTrue(os.path.isdir('/opt/test_module/static'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/static'))
        self.assertTrue(os.path.isdir('/opt/test_module/static/src'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src/src'))
        self.assertTrue(os.path.isdir('/opt/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src/xml/xml'))
        self.assertTrue(os.path.isdir('/opt/test_module/static/src/img'))
        self.assertFalse(os.path.isdir('/opt/test_module/static/src/img/img'))
        
    def test_04_create_module_in_tilde_defined_directory(self):
        """
        Test that given just a module name it puts the folder in the current
        directory
        """
        self.assertFalse(os.path.isdir('~/test_module'))
        self.assertFalse(os.path.isdir('~/test_module/data'))
        self.assertFalse(os.path.isdir('~/test_module/static'))
        self.assertFalse(os.path.isdir('~/test_module/static/src'))
        self.assertFalse(os.path.isdir('~/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('~/test_module/static/src/img'))
        ModuleSkeleton('test_module', '~')
        self.assertTrue(os.path.isdir('~/test_module'))
        self.assertTrue(os.path.isdir('~/test_module/data'))
        self.assertFalse(os.path.isdir('~/test_module/data/data'))
        self.assertTrue(os.path.isdir('~/test_module/static'))
        self.assertFalse(os.path.isdir('~/test_module/static/static'))
        self.assertTrue(os.path.isdir('~/test_module/static/src'))
        self.assertFalse(os.path.isdir('~/test_module/static/src/src'))
        self.assertTrue(os.path.isdir('~/test_module/static/src/xml'))
        self.assertFalse(os.path.isdir('~/test_module/static/src/xml/xml'))
        self.assertTrue(os.path.isdir('~/test_module/static/src/img'))
        self.assertFalse(os.path.isdir('~/test_module/static/src/img/img'))
