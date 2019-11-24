import os
from scipy.stats.mstats import gmean
from ipywidgets import widgets
from IPython.core.display import display, HTML
import numpy as np
from PIL import Image
import collections
import glob
import re

import ipywe.fileselector
from NeuNorm.normalization import Normalization

from __code import file_handler
from __code.metadata_handler import MetadataHandler

METADATA_ERROR = 1  # range +/- for which a metadata will be considered identical


class SequentialCombineImagesUsingMetadata(object):
    working_dir = ''
    default_metadata_to_select = [65044, 65040]

    def __init__(self, working_dir=''):
        self.working_dir = working_dir
        self.folder_selected = ''
        self.list_images = []
        self.dict_of_metadata = {} # key is 'tag->value' and value is 'tag'
        self.list_images_to_combine = None
        self.filename_regular_expression = "^\w*_(?P<run>run\d+)_\w*.tiff$"

    def select_folder(self):
        self.files_list_widget = ipywe.fileselector.FileSelectorPanel(instruction='select folder of images to combine',
                                                                      start_dir=self.working_dir,
                                                                      type='directory',
                                                                      next=self.info_folder_selected,
                                                                      multiple=False)
        self.files_list_widget.show()

    def info_folder_selected(self, selected):
        display(HTML('<span style="font-size: 20px; color:blue">You selected folder: ' + \
                     selected + '</span>'))
        self.folder_selected = selected

    def select_metadata_to_match(self):
        pass

    def get_list_of_images(self):
        list_of_images = glob.glob(self.folder_selected + "/*.tiff")
        list_of_images.sort()
        return list_of_images

    def display_metadata_list(self):
        self.list_images = self.get_list_of_images()
        list_images = self.list_images

        image0 = list_images[0]
        o_image0 = Image.open(image0)

        info = collections.OrderedDict(sorted(o_image0.tag_v2.items()))
        display_format = []
        list_default_value_selected = []
        dict_of_metadata = {}
        for tag, value in info.items():
            formatted_string = "{} -> {}".format(tag, value)
            dict_of_metadata[formatted_string] = tag
            display_format.append(formatted_string)
            if tag in self.default_metadata_to_select:
                list_default_value_selected.append(formatted_string)

        self.box1 = widgets.HBox([widgets.Label("Select Metadata:",
                                                layout=widgets.Layout(width='10%')),
                                  widgets.SelectMultiple(options=display_format,
                                                         value=list_default_value_selected,
                                                         layout=widgets.Layout(width='50%',
                                                                               height='300px'))])
        display(self.box1)
        self.dict_of_metadata = dict_of_metadata

    def how_to_combine(self):
        _file = open("__docs/combine_images/geometric_mean.png", 'rb')
        _geo_image = _file.read()
        geo_box = widgets.HBox([widgets.Label("Geometric Mean",
                                              layout=widgets.Layout(width='20%')),
                                widgets.Image(value=_geo_image,
                                              format='png')])
        _file = open("__docs/combine_images/algebric_mean.png", 'rb')
        _alge_image = _file.read()
        alge_box = widgets.HBox([widgets.Label("Arithmetic Mean",
                                              layout=widgets.Layout(width='20%')),
                                widgets.Image(value=_alge_image,
                                              format='png')])

        self.combine_method = widgets.RadioButtons(options=['add', 'arithmetic mean', 'geometric mean'],
                                                   value='arithmetic mean')

        vertical = widgets.VBox([alge_box, geo_box, self.combine_method])
        display(vertical)

    def create_merging_list(self, list_of_files=[]):
        """ this method will create a dictionary of files to combine by stepping one by one
        through the list of files and checking the metadata value selected

        {'run1':  {'position0' : {'list_of_files': [file1, file2, file3],
                                  'dict_metadata': {'meta1': value1,
                                                    'meta2': value2,
                                                   },
                                 },
                   'position1' : {'list_of_files' : [file4, file5, file6],
                                  'dict_metadata': {'meta1': value3,
                                                    'meta2': value4,
                                                   },
                                 },
                   ...
                  },
         ...
         }
        """

        # FOR DEBUGGING ONLY
        # FIXME (REMOVE_ME)
        # self.list_images = self.list_images[0:20]
        #

        create_list_progress = widgets.HBox([widgets.Label("Creating Merging List:",
                                                           layout=widgets.Layout(width='20%')),
                                             widgets.IntProgress(max=len(self.list_images),
                                                                 min=1,
                                                                 value=1,
                                                                 layout=widgets.Layout(width='80%'))])
        display(create_list_progress)
        progress_bar = create_list_progress.children[1]

        master_list_images_to_combine = collections.OrderedDict()
        list_images_to_combine = collections.OrderedDict()

        # retrieve list of tag selected (to match between runs)
        list_of_tag_selected = self.get_list_of_tag_selected()
        if not list_of_files:
            list_of_files = self.list_images

        position_prefix = 'position'
        position_counter = 0

        # delta_metadata = self.delta_metadata

        # initialization
        _list_files = [list_of_files[0]]
        _dict_metadata = {}

        _previous_metadata = MetadataHandler.get_metata(filename=list_of_files[0],
                                                        list_metadata=list_of_tag_selected)
        _previous_run = self.isolate_run_text_from_filename(list_of_files[0])

        for _index, _file in enumerate(list_of_files[1:]):

            _current_metadata = MetadataHandler.get_metata(filename=_file,
                                                          list_metadata=list_of_tag_selected)
            _current_run = self.isolate_run_text_from_filename(_file)

            if self.are_metadata_within_error_range(_current_metadata, _previous_metadata) and \
                    (_previous_run == _current_run):
                _list_files.append(_file)
            else:
                tag_name = "{}{}".format(position_prefix, position_counter)
                list_images_to_combine[tag_name] = {'list_of_files': _list_files,
                                                    'dict_metadata': _previous_metadata.copy(),
                                                   }

                position_counter += 1
                _list_files = [_file]

                if _previous_run != _current_run:
                    master_list_images_to_combine[_previous_run] = list_images_to_combine
                    list_images_to_combine = collections.OrderedDict()

                _previous_metadata = _current_metadata
                _previous_run = _current_run

        else:
            tag_name = "{}{}".format(position_prefix, position_counter)
            list_images_to_combine[tag_name] = {'list_of_files': _list_files,
                                                'dict_metadata': _previous_metadata.copy(),
                                                }
            master_list_images_to_combine[_previous_run] = list_images_to_combine
            progress_bar.value = _index+1

        create_list_progress.close()
        del create_list_progress

        self.master_list_images_to_combine = master_list_images_to_combine

    def are_metadata_within_error_range(self, metadata1, metadata2):
        """will go through all the metadata and make sure they are all identical, within the given
        METADATA_ERROR range"""
        for _key in metadata1.keys():
            if np.abs(self.isolate_value_from_metadata(metadata1[_key])
                      - self.isolate_value_from_metadata(metadata2[_key])) > METADATA_ERROR:
                return False
        return True

    def isolate_value_from_metadata(self, metadata_string):
        """Isolate the value from the metadatastring
        ex: metadata_string: MotLongAxis.RBV:300.345454
        will return: 300.345454
        """
        metadata_split = metadata_string.split(":")
        return np.float(metadata_split[1])

    def isolate_run_text_from_filename(self, full_file_name):
        basename = os.path.basename(full_file_name)
        regular_expression = self.filename_regular_expression
        m = re.search(regular_expression, basename)
        if m is not None:
            return m.group('run')
        else:
            return None

    def recap_merging_list(self):
        box0 = widgets.VBox([widgets.Label("List of Runs",
                                           layout=widgets.Layout(width='100%')),
                             widgets.Select(options=self.master_list_images_to_combine.keys(),
                                            layout=widgets.Layout(width='150px',
                                                                  height='300px'))],
                            layout=widgets.Layout(width="160px"))
        self.list_of_runs_ui = box0.children[1]

        box1 = widgets.VBox([widgets.Label("List of positions",
                                           layout=widgets.Layout(width='100%')),
                             widgets.Select(options=self.get_list_of_position_for_select_run(),
                                            layout=widgets.Layout(width='150px',
                                                                  height='300px'))],
                            layout=widgets.Layout(width="160px"))
        self.list_of_positions_ui = box1.children[1]

        box2 = widgets.VBox([widgets.Label("List of Files for this position",
                                           layout=widgets.Layout(width='100%')),
                             widgets.Select(options=self.get_list_of_files_for_selected_run_position(),
                                            layout=widgets.Layout(width='100%',
                                                                  height='500px'))],
                            layout=widgets.Layout(width="815px"))
        self.list_of_files_ui = box2.children[1]

        box3 = widgets.VBox([widgets.Label("Metadata"),
                             widgets.Textarea("",
                                              disabled=True),
                             widgets.Label("Error allowed: {}".format(METADATA_ERROR))],
                             layout=widgets.Layout(width="300px"))

        str_metadata = self.get_str_metadata(metadata_dict=self.get_metadata_for_selected_run_position())
        self.metadata_recap_textarea = box3.children[1]
        self.metadata_recap_textarea.value = str_metadata

        hori_box = widgets.HBox([box1, box2, box3],
                               layout=widgets.Layout(width='100%'))

        self.list_of_positions_ui.on_trait_change(self.recap_positions_changed, name='value')
        self.list_of_runs_ui.on_trait_change(self.recap_runs_changed, name='value')

        display(hori_box)

    def get_list_of_position_for_select_run(self):
        selected_run = self.list_of_runs_ui.value
        return self.master_list_images_to_combine[selected_run].keys()

    def get_list_of_files_for_selected_run_position(self):
        dict = self._get_dict_from_selected_run_position()
        return dict['list_of_files']

    def get_metadata_for_selected_run_position(self):
        _dict = self._get_dict_from_selected_run_position()
        return _dict['dict_metadata']

    def _get_dict_for_selected_run_position(self):
        selected_run = self.list_of_runs_ui.value
        selected_position = self.list_of_positions_ui.value
        return self.master_list_images_to_combine[selected_run][selected_position]

    def get_str_metadata(self, metadata_dict={}):
        """format the metadata to display them as a string"""
        str_metadata = ""
        for _key, _value in metadata_dict.items():
            str_metadata += "{} -> {}\n".format(_key, _value)
        return str_metadata

    def recap_positions_changed(self):
        position_selected = self.list_of_positions_ui.value
        run_selected = self.list_of_runs_ui.value

        list_files_of_files = self.master_list_images_to_combine[run_selected][position_selected]['list_of_files']
        self.list_of_files_ui.options = list_files_of_files

        str_metadata = self.get_str_metadata(position_key=position_selected)
        self.metadata_recap_textarea.value = str_metadata

    def recap_runs_changed(self):
        run_selected = self.list_of_runs_ui.value

        list_of_positions = self.master_list_images_to_combine[run_selected].keys()
        self.list_of_positions_ui.options = list_of_positions

        self.recap_positions_changed()

    def get_list_of_tag_selected(self):
        ui_selection = self.box1.children[1].value
        result = []
        for _selection_value in ui_selection:
            result.append(self.dict_of_metadata[_selection_value])

        return result

    def select_output_folder(self):
        self.output_folder_widget = ipywe.fileselector.FileSelectorPanel(instruction='select where to create the ' + \
                                                                                     'combined image ...',
                                                                         start_dir=self.working_dir,
                                                                         type='directory')

        self.output_folder_widget.show()

    def __get_formated_merging_algo_name(self):
        _algo = self.combine_method.value
        if _algo =='arithmetic mean':
            return 'arithmetic_mean'
        elif _algo == 'geometric mean':
            return 'geometric_mean'
        else:
            return _algo

    def define_output_filename(self):
        list_files = self.files_list_widget.selected
        short_list_files = [os.path.basename(_file) for _file in list_files]

        merging_algo = self.__get_formated_merging_algo_name()
        [default_new_name, ext] = self.__create_merged_file_name(list_files_names=short_list_files)

        top_label = widgets.Label("You have the option to change the default output file name")

        box = widgets.HBox([widgets.Label("Default File Name",
                                          layout=widgets.Layout(width='20%')),
                            widgets.Text(default_new_name,
                                         layout=widgets.Layout(width='60%')),
                            widgets.Label("_{}{}".format(merging_algo, ext),
                                          layout=widgets.Layout(width='20%')),
                            ])
        self.default_filename_ui = box.children[1]
        self.ext_ui = box.children[2]
        vertical_box = widgets.VBox([top_label, box])
        display(vertical_box)

    def merging(self):
        """combine images using algorithm provided"""

        list_files = self.files_list_widget.selected
        nbr_files = len(list_files)

        # get merging algorithm
        merging_algo = self.combine_method.value
        algorithm = self.__add
        if merging_algo =='arithmetic mean':
            algorithm = self.__arithmetic_mean
        elif merging_algo == 'geometric mean':
            algorithm = self.__geo_mean

        # get output folder
        output_folder = os.path.abspath(self.output_folder_widget.selected)

        o_load = Normalization()
        o_load.load(file=list_files, notebook=True)
        _data = o_load.data['sample']['data']

        merging_ui = widgets.HBox([widgets.Label("Merging Progress",
                                                 layout=widgets.Layout(width='20%')),
                                   widgets.IntProgress(max=2)])
        display(merging_ui)
        w1 = merging_ui.children[1]

        combined_data = self.__merging_algorithm(algorithm, _data)
        w1.value = 1

        #_new_name = self.__create_merged_file_name(list_files_names=o_load.data['sample']['file_name'])
        _new_name = self.default_filename_ui.value + self.ext_ui.value
        output_file_name = os.path.join(output_folder, _new_name)

        file_handler.save_data(data=combined_data, filename=output_file_name)

        w1.value = 2

        display(HTML('<span style="font-size: 20px; color:blue">File created: ' + \
                     os.path.basename(output_file_name) + '</span>'))
        display(HTML('<span style="font-size: 20px; color:blue">In Folder: ' + \
                     output_folder + '</span>'))

    def __create_merged_file_name(self, list_files_names=[]):
        """Create the new base name using a combine name of all the input file

        :param list_files_names: ['/Users/j35/image001.fits','/Users/j35/iamge002.fits']
        :return:
            'image001_image002.fits'
        """
        ext = ''
        list_base_name = []
        for _file in list_files_names:
            basename = os.path.basename(_file)
            [_name, ext] = os.path.splitext(basename)
            list_base_name.append(_name)

        return ('_'.join(list_base_name), ext)

    def __add(self, data_array):
        return np.sum(data_array, axis=0)

    def __arithmetic_mean(self, data_array):
        return np.mean(data_array, axis=0)

    def __geo_mean(self, data_array):
        return gmean(data_array, axis=0)

    def __merging_algorithm(self, function_, *args):
        return function_(*args)


