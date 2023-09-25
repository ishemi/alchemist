import os

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

