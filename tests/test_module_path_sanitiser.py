import fake_filesystem_unittest
from configuration_generator.__main__ import sanitise_path


class TestSanitisesModulePath(fake_filesystem_unittest.TestCase):
    """
    Test that the module path sanitiser is working properly
    """

    def setUp(self):
        """
        We're using PyFakeFs to ensure we don't touch the filesystem so need
        to set it up - needed for os.expandpath
        """
        self.setUpPyfakefs()

    def test_01_top_level_directory(self):
        """
        Test that it returns '' on being given /
        """
        self.assertEqual(sanitise_path('/'), '',
                         'Incorrect top level directory returned')

    def test_02_top_level_defined_directory(self):
        """
        Test that it returns '/opt/foo' when given '/opt/foo'
        """
        self.assertEqual(sanitise_path('/opt/foo'), '/opt/foo',
                         'Incorrect top level defined directory returned')

    def test_03_relative_folder_directory(self):
        """
        Test returns 'folder' when given 'folder'
        """
        self.assertEqual(sanitise_path('folder'), 'folder',
                         'Incorrect top level directory returned')