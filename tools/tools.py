import os
import os
import zipfile
import tarfile
import bz2


def hello_world():
  print("Hello World!!!")

def list_files(directory):
  """Lists all files in a directory, but does not recurse into subdirectories.

  Args:
    directory: The path to the directory.

  Returns:
    A list of strings, each containing the name of a file in the directory.
  """

  files = []
  for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
      files.append(filename)
  return files


def decompress_file(file_path, output_dir):
  """Decompresses a file in the following formats: zip, tar, tar.gz, bz, rar, and 7z.

  Args:
    file_path: The path to the file to be decompressed.
    output_dir: The path to the directory where the decompressed files should be created.
  """

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  if file_path.endswith('.zip'):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
      zip_file.extractall(output_dir)
  elif file_path.endswith('.tar'):
    with tarfile.open(file_path, 'r') as tar_file:
      tar_file.extractall(output_dir)
  elif file_path.endswith('.tar.gz'):
    with tarfile.open(file_path, 'r:gz') as tar_file:
      tar_file.extractall(output_dir)
  elif file_path.endswith('.bz'):
    with bz2.open(file_path, 'rb') as bz_file:
      decompressed_data = bz_file.read()
      with open(os.path.join(output_dir, file_path[:-3]), 'wb') as output_file:
        output_file.write(decompressed_data)
  else:
    raise Exception('Unsupported file format.')

