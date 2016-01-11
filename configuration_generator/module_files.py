# pylint: disable=maybe-no-member
""" Module to create and render the files for the module """
import subprocess
import base64
from jinja2 import Environment, PackageLoader
from tempfile import NamedTemporaryFile


class ModuleFiles(object):
    """
    A class for creating the files of an Odoo module
    """

    def __init__(self, module_name, module_path=None, trust_details=None):
        """
        Do some sanity checks on the module name, if module_path is set then
        ensure we have permissions to write to it otherwise do in current
        working directory
        :param module_name: String to use as module folder's name
        :param module_path: A path to put the module
        :param trust_details: A dictionary of details for the trust
        """
        if not trust_details:
            raise RuntimeError('No trust details configured')
        self.trust_name = trust_details.get('trust_name', '')
        self.trust_status = trust_details.get('trust_status', '')
        self.trust_email = trust_details.get('trust_email', '')
        self.trust_website = trust_details.get('trust_website', '')
        self.env = Environment(loader=PackageLoader('configuration_generator',
                                                    'templates'))
        if module_path:
            self.module_root = '{0}/{1}'.format(module_path, module_name)
        else:
            self.module_root = '{0}'.format(module_name)
        self.render_config_file()
        self.render_logo_file()
        self.render_data_file()
        self.render_view_override_file(module_name)

    def render_config_file(self):
        """
        render __init__.py and __openerp__.py
        """
        conf_temp = self.env.get_template('__openerp__.py.j2')
        # Save __init__.py
        with open('{0}/{1}'.format(self.module_root, '__init__.py'), 'wb') \
                as init_file:
            init_file.write('')

        # Render __openerp__.py
        conf_file = conf_temp.render(trust_name=self.trust_name,
                                     trust_status=self.trust_status)
        # Save __openerp__.py
        with open('{0}/{1}'.format(self.module_root, '__openerp__.py'), 'wb') \
                as openerp_file:
            openerp_file.write(conf_file)

    def render_logo_file(self):
        """
        render logo file into static folder
        """
        logo_temp = self.env.get_template('logo.svg.j2')
        # render logo.svg
        svg_width =  200 + (len(self.trust_name) * 17) # 745
        if len(self.trust_status) > len(self.trust_name):
        	svg_width = 200 + (len(self.trust_status) * 17)
        logo_offset = svg_width - 200  # 545
        text_width = logo_offset - 25  # 520
        logo_file = logo_temp.render(trust_name=self.trust_name,
                                     trust_status=self.trust_status,
                                     svg_width=svg_width,
                                     text_width=text_width,
                                     logo_offset=logo_offset)

        # create logo.png file stream
        svg_tmp = NamedTemporaryFile(delete=False)
        svg_tmp.write(logo_file)
        svg_tmp.close()
        png_name = '{0}/{1}'.format(self.module_root,
                                    'static/src/img/trust_logo.png')
        try:
            subprocess.check_output(['cairosvg', svg_tmp.name, '-f', 'png',
                                     '-o', png_name, '-d', '0.01'])
        except OSError, exception:
            print exception.message
            raise RuntimeError('CairoSVG binary not found')
        except subprocess.CalledProcessError:
            raise

    def render_data_file(self):
        """
        render data/master_data.xml
        """
        data_temp = self.env.get_template('master_data.xml.j2')
        png_name = '{0}/{1}'.format(self.module_root,
                                    'static/src/img/trust_logo.png')
        # create base64 encoding of file stream
        with open(png_name, 'rb') as png_file:
            base_logo = png_file.read()
        encoded_logo = base64.b64encode(base_logo)

        # render master_data.xml
        data_file = data_temp.render(trust_name=self.trust_name,
                                     trust_status=self.trust_status,
                                     trust_email=self.trust_email,
                                     trust_website=self.trust_website,
                                     trust_logo_encoded=encoded_logo)

        # Save master_data.xml
        dpath = 'data/master_data.xml'
        with open('{0}/{1}'.format(self.module_root, dpath), 'wb') \
                as master_data_file:
            master_data_file.write(data_file)

    def render_view_override_file(self, module_name):
        """
        Render static/src/xml/view_override.xml
        """
        view_temp = self.env.get_template('view_override.xml.j2')

        # render view_override.xml
        view_file = view_temp.render(module_name=module_name)

        # save view_override.xml
        vpath = 'static/src/xml/view_override.xml'
        with open('{0}/{1}'.format(self.module_root, vpath), 'wb') \
                as xml_view_file:
            xml_view_file.write(view_file)
