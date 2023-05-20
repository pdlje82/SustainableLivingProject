import os
import pickle
import datetime


def create_file(directory, projectname):
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M")

    # Add the timestamp to the filename
    new_filepath = f"{timestamp}_{projectname}"

    # Join the directory path and the new filename to get the full file path
    full_path = os.path.join(directory, new_filepath)

    # Create directory if it doesn't exist
    os.makedirs(full_path, exist_ok=True)

    return full_path

def save_object(obj, full_filename, directory):
    # If the directory does not exist, create it
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Open the file and use pickle to save the object
    with open(os.path.join(directory, full_filename), 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_object(filename, directory):
    """Loads an object from a file using pickle."""
    with open(os.path.join(directory, filename), 'rb') as input:
        obj = pickle.load(input)
    return obj
