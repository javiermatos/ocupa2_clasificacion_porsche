import csv
import os.path
from shutil import copyfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DELIMITER = ';'


def get_filename_classification(dataset_file=os.path.join(BASE_DIR, 'dataset', 'dataset.csv')):
    with open(dataset_file) as f:
        csv_reader = csv.reader(f, delimiter=CSV_DELIMITER)
        next(csv_reader)  # skip first row with column names
        return {filename: classification for filename, classification in csv_reader}


def create_directories(directories):
    for directory in directories:
        directory_path = os.path.join(BASE_DIR, 'original_images', directory)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)


def classify_dataset(
    dataset_filename_classification,
    dataset_path=os.path.join(BASE_DIR, 'dataset', 'images'),
    classified_dataset_path=os.path.join(BASE_DIR, 'original_images'),
):
    for filename, classification in dataset_filename_classification.items():
        copyfile(
            os.path.join(dataset_path, filename),
            os.path.join(classified_dataset_path, classification, filename),
        )


def main():
    dataset_filename_classification = get_filename_classification()
    create_directories(set(dataset_filename_classification.values()))
    classify_dataset(dataset_filename_classification)


if __name__ == '__main__':
    main()
