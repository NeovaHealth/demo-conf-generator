""" Module to create the skeleton needed to render files into """
import os
import errno


class ModuleSkeleton(object):
    """
    A class for creating the skeleton of an Odoo module
    """

    def __init__(self, module_name, module_path=None):
        """
        Do some sanity checks on the module name, if module_path is set then
        ensure we have permissions to write to it otherwise do in current
        working directory
        :param module_name: String to use as module folder's name
        :param module_path: A path to put the module
        """
        self.module_name = module_name
        self.module_path = module_path
        self.create_skeleton()

    def create_skeleton(self):
        """
        Put the folders in the right place
        - module folder
        - - data
        - - static
        - - - src
        - - - - img
        - - - - xml
        """
        dir_str = '{0}/{1}'
        module_folder = (dir_str.format(self.module_path, self.module_name),
                         self.module_name)
        data_folder = (dir_str.format(module_folder[0], 'data'), 'data')
        static_folder = (dir_str.format(module_folder[0], 'static'), 'static')
        src_folder = (dir_str.format(static_folder[0], 'src'), 'src')
        img_folder = (dir_str.format(src_folder[0], 'img'), 'img')
        xml_folder = (dir_str.format(src_folder[0], 'xml'), 'xml')
        folders = [module_folder, data_folder, static_folder,
                   src_folder, img_folder, xml_folder]
        for folder in folders:
            try:
                self.create_folder(folder[0], folder[1])
            except OSError:
                print 'Error encountered when creating module skeleton'

    @staticmethod
    def create_folder(path, name):
        """
        Create a folder in a given path with given name
        :param path: Where to put folder
        :param name: What to call folder
        """
        folder = '{0}/{1}'.format(path, name)
        try:
            os.makedirs(folder)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(folder):
                pass
            else:
                raise
