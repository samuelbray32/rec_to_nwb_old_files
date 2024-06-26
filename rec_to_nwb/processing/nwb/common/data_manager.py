import abc

import numpy as np


class DataManager(abc.ABC):
    def __init__(self, directories):
        self.directories = directories

        self.number_of_datasets = self.get_number_of_datasets()
        self.number_of_files_per_dataset = self.get_number_of_files_per_dataset()
        self.number_of_rows_per_file = self._get_number_of_rows_per_file()
        self.file_lengths_in_datasets = self._get_file_length(
            self.number_of_datasets)

    @abc.abstractmethod
    def read_data(self, dataset_id, file_id):
        pass

    def get_number_of_files_per_dataset(self):
        return np.shape(self.directories)[1]

    def _get_data_shape(self, dataset_num, file_num=0):
        dim1 = np.shape(self.read_data(dataset_num, file_num))[0]
        dim2 = np.shape(self.read_data(dataset_num, file_num))[1]
        return dim1, dim2

    def get_data_shape(self, dataset_num, file_num=0):
        return self._get_data_shape(dataset_num, file_num)

    def _get_file_length(self, number_of_datasets):
        return [self._get_data_shape(i)[1] for i in range(number_of_datasets)]

    def get_number_of_datasets(self):
        return np.shape(self.directories)[0]

    def get_final_data_shape(self):
        # return self.number_of_rows_per_file * self.number_of_files_per_dataset, sum(self.file_lengths_in_datasets)
        return (sum(self.number_of_rows_per_file), sum(self.file_lengths_in_datasets))

    def get_directories(self):
        return self.directories

    def _get_number_of_rows_per_file(self):
        dataset_num = 0   # assume that all datasets have identical structures
        # but files may have different numbers of rows
        return [np.shape(self.read_data(dataset_num, file_num))[0]
                for file_num in range(self.number_of_files_per_dataset)]

    def get_number_of_rows_per_file(self):
        return self.number_of_rows_per_file

    def get_file_lengths_in_datasets(self):
        return self.file_lengths_in_datasets
