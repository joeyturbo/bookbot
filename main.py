def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  chars_dict = get_char_count(text)

  

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_word_count(text):
  return len(text.split())

def get_char_count(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

main()