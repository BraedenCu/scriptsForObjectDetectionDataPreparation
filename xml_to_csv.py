import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    #NEED TO CHANGE THE FOLLOWING LINE TO RESPECTIVE PATH
    image_path = os.path.join('/root/annotations')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('vex_labels.csv', index=None)
    #added the following to check if the file is empty, because I was having issues 
    #following path also needs to change
    df = pd.read_csv("/root/scriptsForObjectDetectionDataPreparation/vex_labels.csv") 
    if df.empty:
        print("error converting to csv, the pandas dataframe contained in the file is empty")
    else:
        print('Successfully converted xml to csv.')

main()
