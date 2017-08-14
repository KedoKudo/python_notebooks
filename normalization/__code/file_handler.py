import os
from astropy.io import fits
import numpy as np
import pickle
import shutil
from PIL import Image


def test_image(file_name, threshold=5000):
    # check size of image and return False if size is below threshold 
    statinfo = os.stat(file_name)
    if statinfo.st_size < threshold:
        return False
    return True

def load_data(filename=''):
    '''
    load the various file_name format
    '''
    data_type = get_data_type(filename)
    if data_type == '.fits':
        hdulist = fits.open(filename, ignore_missing_end=True)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        hdulist.close()
        return _image
    elif (data_type == '.tiff') or (data_type == '.tif'):
        _image = Image.open(filename)
        return np.array(_image)
    else:
        return []
    
def save_data(data=[], filename=''):
    data_type = get_data_type(file_name)
    if data_type == '.fits':
        make_fits(data=data, filename=filename)
    elif (data_type == '.tiff') or (data_type == '.tif'):
        make_tiff(data=data, filename=filename)
    
def get_data_type(file_name):
    '''
    using the file name extension, will return the type of the data
    
    Arguments:
        full file name
        
    Returns:
        file extension    ex:.tif, .fits
    '''
    filename, file_extension = os.path.splitext(file_name)
    return file_extension.strip()

def save_file(folder='', base_file_name='', suffix='', dictionary={}):
    if folder == '':
        return
    
    output_file = folder + base_file_name + '_time_dictionary.dat'
    pickle.dump(dictionary, open(output_file, "wb"))
    
    return output_file
       
def make_tiff(data=[], filename=''):
    new_image = Image.fromarray(data)
    new_image.save(filename)
    
def make_fits(data=[], filename=''):
    fits.writeto(filename, data, clobber=True)
    
def make_or_reset_folder(folder_name):
    if os.path.exists(folder_name):
         shutil.rmtree(folder_name)
    os.makedirs(folder_name)         
    
def remove_SummedImg_from_list(list_files):
    base_name_and_extension = os.path.basename(list_files[0])
    dir_name = os.path.dirname(list_files[0])
    [base_name, _] = os.path.splitext(base_name_and_extension)
    base_base_name_array = base_name.split('_')
    name = '_'.join(base_base_name_array[0:-1])
    index = base_base_name_array[-1]
    file_to_remove = os.path.join(dir_name, name + '_SummedImg.fits')
    list_files_cleaned = []
    for _file in list_files:
        if _file == file_to_remove:
            continue
        list_files_cleaned.append(_file)
    return list_files_cleaned
    
def make_ascii_file(metadata=[], data=[], output_file_name='', dim='2d'):
    f = open(output_file_name, 'w')
    for _meta in metadata:
        _line = _meta + "\n"
        f.write(_line)
        
    for _data in data:
        if dim == '2d':
            _str_data = [str(_value) for _value in _data]
            _line = ",".join(_str_data) + "\n"
        else:
            _line = _data + '\n'
        f.write(_line)
       
    f.close()
    

   