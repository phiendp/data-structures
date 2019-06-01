import os

def find_files_recursive(suffix_files, suffix, path):
   if os.path.isfile(path):
      if path.endswith(suffix):
         suffix_files.append(path)
   else:
      for content in os.listdir(path):
         find_files_recursive(suffix_files, suffix, os.path.join(path, content))
   return suffix_files


def find_files(suffix, path):
   """
   Find all files beneath path with file name suffix.

   Note that a path may contain further subdirectories
   and those subdirectories may also contain further subdirectories.

   There are no limit to the depth of the subdirectories can be.

   Args:
   suffix(str): suffix if the file name to be found
   path(str): path of the file system

   Returns:
      a list of paths
   """

   if suffix is None or path is None:
      return None

   suffix_files = []
   find_files_recursive(suffix_files, suffix, path)
   return suffix_files


def test_cases():
   print("Print all files with .c extension")
   print(find_files(".c", "testdir"))
   print()

   print("Print all file with .h extension")
   print(find_files(".h", "testdir"))
   print()

   print("Print all the files in the directory")
   print()

   print(find_files("", "testdir"))
   print(find_files(None, "testdir"))


if __name__ == "__main__":
   print(test_cases())
