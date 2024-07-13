import os

def md_word_count_folder(dir_path):
  total_words = 0
  for root, _, files in os.walk(dir_path):
    for file in files:
      file_path = os.path.join(root,file)
      if os.path.isfile(file_path):
        try:
          with open(file_path,"r") as f:
            words = sum(1 for _ in f.read().split())
            total_words += words
        except (IOError,UnicodeError) as e:
          print(f"An error occured {dir_path} - {e}")
  return total_words

dir_path = "C:\\Users\\Researcher\\Stories\\The Obsession\\Scenes"
word_count = md_word_count_folder(dir_path)

print(f"{word_count} total words")