def is_palindromo(text):
  valid_palindromo = check_palindromo(text)

  print(f"{text} {valid_palindromo}")


def check_palindromo(text):
  text = clear_text(text)
  inverse_text = ""

  # longitud = len(text)
  # for i in range(longitud):
  #   inverse_text += text[longitud-i-1]

  for char in text:
    inverse_text = char + inverse_text


  return text == inverse_text


def clear_text(text):
  return text.lower().replace(' ', '')


is_palindromo("Hola Mundo")
is_palindromo("Reconocer")
