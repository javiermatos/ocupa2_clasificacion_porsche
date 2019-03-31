import os
import os.path

import Augmentor

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, 'original_images')
OUTPUT_DIR = os.path.join(BASE_DIR, 'training_images')
SAMPLES = 1000


def image_augmentation(source_directory, output_directory, samples):
    p = Augmentor.Pipeline(
        source_directory=source_directory,
        output_directory=output_directory,
    )

    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
    p.flip_left_right(probability=0.5)

    p.sample(samples)


def main():
    root, directories, files = next(os.walk(SOURCE_DIR))
    for directory in directories:
        print('Augmented dataset for {}'.format(directory))
        image_augmentation(
            os.path.join(SOURCE_DIR, directory),
            os.path.join(OUTPUT_DIR, directory),
            SAMPLES,
        )


if __name__ == '__main__':
    main()
