import os
import csv
from data_source.data_source import DataSource

class FileDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = self._infer_file_type()

    def _infer_file_type(self) -> str:
        _, file_extension = os.path.splitext(self.file_path)
        return file_extension.lower().strip('.')

    def load_data(self):
        if self.file_type == 'csv':
            return self._load_from_csv()
        else:
            raise ValueError(f"Unsupported file type: {self.file_type}")

    def _load_from_csv(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
               yield row 