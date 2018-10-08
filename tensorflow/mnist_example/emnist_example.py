import os
import tensorflow as tf

def dataset(directory, images_file, labels_file):
    """Download and parse MNIST dataset."""

    #images_file = download(directory, images_file)
    #labels_file = download(directory, labels_file)



    #check_image_file_header(images_file)
    #check_labels_file_header(labels_file)

    def decode_image(image):
        # Normalize from [0, 255] to [0.0, 1.0]
        image = tf.decode_raw(image, tf.uint8)
        image = tf.cast(image, tf.float32)
        image = tf.reshape(image, [784])
        return image / 255.0

    def decode_label(label):
        label = tf.decode_raw(label, tf.uint8)  # tf.string -> [tf.uint8]
        label = tf.reshape(label, [])  # label is a scalar
        return tf.to_int32(label)

    images = tf.data.FixedLengthRecordDataset(
        images_file, 28 * 28, header_bytes=16).map(decode_image)
    labels = tf.data.FixedLengthRecordDataset(
        labels_file, 1, header_bytes=8).map(decode_label)
    return tf.data.Dataset.zip((images, labels))


def train(directory):
    """tf.data.Dataset object for MNIST training data."""
    return dataset(directory, 'train-images-idx3-ubyte',
                    'train-labels-idx1-ubyte')


def test(directory):
    """tf.data.Dataset object for MNIST test data."""
    return dataset(directory, 't10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte')

directory = '/home/philip/Desktop/emnist'#'/home/philip/Documnent/MNIST'
filename = 'emnist-balanced-train-images-idx3-ubyte'#'train-images-idx3-ubyte'
filepath = os.path.join(directory, filename)
print(filepath)
if tf.gfile.Exists(filepath):
    print("Exist")


def decode_image(image):
    # Normalize from [0, 255] to [0.0, 1.0]
    image = tf.decode_raw(image, tf.uint8)
    image = tf.cast(image, tf.float32)
    image = tf.reshape(image, [784])
    return image / 255.0
images = tf.data.FixedLengthRecordDataset(filepath, 28 * 28, header_bytes=16).map(decode_image)

print(images)