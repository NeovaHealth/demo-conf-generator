""" Main coordinator of creating module """
import sys
import os
import argparse
from configuration_generator.module_skeleton import ModuleSkeleton
from configuration_generator.module_files import ModuleFiles


PARSER = argparse.ArgumentParser('Generate an Open-eObs Module')
PARSER.add_argument('module_name', type=str, help='Name of module folder')
PARSER.add_argument('--output_path', type=str,
                    help='Place to output the module folder')
PARSER.add_argument('--trust_name', type=str, help='Name of Trust')
PARSER.add_argument('--trust_status', type=str,
                    help='Status of Trust (NHS Trust, Foundation Trust etc)')
PARSER.add_argument('--trust_email', type=str, help='Email for Trust')
PARSER.add_argument('--trust_website', type=str, help='Website for Trust')


def main():
    """
    Parse the arguments sent via command line, create skeleton, render files
    into folders
    """
    args = PARSER.parse_args()
    module_name = sanitise_name(args.module_name)
    module_path = sanitise_path(args.output_path)
    trust_details = {
        'trust_name': args.trust_name,
        'trust_status': args.trust_status,
        'trust_email': args.trust_email,
        'trust_website': args.trust_website
    }
    try:
        ModuleSkeleton(module_name, module_path)
        ModuleFiles(module_name, module_path, trust_details)
    except OSError:
        print 'Error encountered creating module at {0}/{1}'.format(
            module_path, module_name)
    except RuntimeError:
        print 'Error encountered creating module at {0}/{1}'.format(
            module_path, module_name)
    print 'Successfully created module at {0}/{1}'.format(
        module_path, module_name)


def sanitise_name(module_name):
    """
    Remove all the white space and spaces from module name
    :param module_name: User supplied name for module
    :return: name without badness
    """
    return module_name.strip().replace(' ', '_')


def sanitise_path(module_path):
    """
    Make sure the path is correct
    :param module_path: User supplied path
    :return: A path that will work
    """
    if not module_path:
        return os.getcwd()
    elif module_path == '/':
        return ''

if __name__ == '__main__':
    sys.exit(main())
