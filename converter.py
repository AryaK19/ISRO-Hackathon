# :)
import pandas as pd
import xml.etree.ElementTree as ET


tree = ET.parse('ch2_iir_nci_20240213T0543269734_d_img_d18\data\calibrated\\20240213\ch2_iir_nci_20240213T0543269734_d_img_d18.xml')
root = tree.getroot()


namespace = {'isda': 'http://pds.nasa.gov/pds4/pds/v1'}
    
band_bins = root.findall('.//isda:Band_Bin', namespace)

data = []

for band_bin in band_bins:
    band_number = int(band_bin.find('isda:band_number', namespace).text)
    center_wavelength = float(band_bin.find('isda:center_wavelength', namespace).text)
    band_width = float(band_bin.find('isda:band_width', namespace).text)
    data.append([band_number, center_wavelength, band_width])


df = pd.DataFrame(data, columns=['Band Number', 'Center Wavelength (nm)', 'Band Width (nm)'])

print(df)
df.to_excel('band_information.xlsx', index=False)

print("Excel file has been created successfully!")