from xml.etree import ElementTree as ET
import shutil
import os
import sys


def parse_xml(xml_file):
    """
    Parsing XML file
    """
    try:
        xml_parse = ET.parse(xml_file)
        models = xml_parse.findall('file')
        saved_models = [i.attrib for i in models]
        return saved_models
    except FileNotFoundError:
        print('Can\'t find the file %s' % FileNotFoundError)
        print('Please check the file name')
    except Exception as ex:
        print('Got another exception %s' % Exception)


def copy_for_linux(xml_data):
    try:
        for item in xml_data:
            print(item)
    except TypeError:
        print('Wrong type for input data', TypeError)


def main():
    if sys.platform.lower() == 'linux' and os.path.sep == '/':
        copy_for_linux(parse_xml('csonfig.xml'))


#
# for item in saved_models_data:
#         try:
#             source = item['source_path']
#             target = item['destination_path']
#             file_name = item['file_name']
#             print(f'target\\'+file_name)
#             # shutil.copy(source, f'target\\' + file_name)
#             # os.chdir(target)
#             # os.system('copy 1.txt 2.txt')
#         except IOError as io_ex:
#             print(f'Unable to copy file {io_ex}')
#         except Exception:
#             print("Unexpected error:", sys.exc_info())

main()


