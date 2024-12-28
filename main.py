def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  chars_dict = get_char_count(text)
  list_of_dicts = clean_dict(chars_dict)
  get_report(book_path, num_words, list_of_dicts)

  

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

def sort_on(dict):
  return dict['count']

def clean_dict(dict):
  chars = 'abcdefghijklmnopqrstuvwxyz'
  list_of_dicts = []
  for key, value in dict.items():
    if key in chars:
      list_of_dicts.append({'char' : key, 'count' : value})
  list_of_dicts.sort(reverse=True, key=sort_on)
  return list_of_dicts


def get_report(book_path, num_words, chars_dict):
  print(f'--- Begin report of {book_path} ---')
  print(f'{num_words} words were found in the document')
  print('')
  for item in chars_dict:
    print(f"The '{item['char']}' character was found {item['count']} times")
  print('--- End Report ---')

main()