import os
import shutil
from xml.etree import ElementTree as ET


def parse_xml(xml_file):
    try:
        xml_parse = ET.parse(xml_file)
        models = xml_parse.findall('file')
        saved_models = [i.attrib for i in models]
        return saved_models
    except FileNotFoundError:
        print('Can\'t find the file %s' % FileNotFoundError)
        print('Please check the file name')
    except Exception as ex:
        print('Got another exception %s' % ex)


def copy_files(xml_data):
    for item in xml_data:
        if item['source_path'].__contains__(os.path.sep):
            source = item['source_path']
            destination = item['destination_path']
            file_name = item['file_name']
            try:
                shutil.copy(f'{source}/' + file_name, destination)
                shutil.copy(f'{source}\\' + file_name, destination)
            except TypeError:
                print('Wrong type for input data', TypeError)
            except FileNotFoundError:
                print(f'Can\'t find {file_name} file in {source} path')
            except PermissionError:
                print(f'Permission denied, can\'t copy {file_name} to {destination}')
                pass
            except Exception as ex:
                print(f'Processed {ex} exception')
            else:
                print('Copying finished perfect')


def main():
    copy_files(parse_xml('config.xml'))
    return 'Done!'


if __name__ == '__main__':
    main()
