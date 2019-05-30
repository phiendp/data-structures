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
   assert sorted(find_files('.h', './testdir')) == ['./testdir/subdir1/a.h',
                                                   './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']

   assert sorted(find_files('.c', './testdir')) == ['./testdir/subdir1/a.c',
                                                   './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']


   assert sorted(find_files('.h', './testdir/subdir3/subsubdir1/b.h')
               ) == ['./testdir/subdir3/subsubdir1/b.h']

   assert sorted(find_files('.c', './testdir/subdir3/subsubdir1/b.h')) == []

   return 'Test passed!'


if __name__ == "__main__":
   print(test_cases())
