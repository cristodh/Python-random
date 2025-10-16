"""Palindromo:
--palabra.split()-- separa la frase en palabras (quitando los espacios).
--''.join(...)-- une todas las palabras en una sola cadena, sin espacios.
--.lower()-- convierte todo a minúsculas. "Anita lava la tina" → "anitalavalatina"
--palabra_limpia[::-1]:-- invierte la cadena."""


def es_palindromo(palabra):
    palabra_limpia = ''.join(palabra.split()).lower()
    if palabra_limpia == palabra_limpia[::-1]:
        return "Es palíndromo"
    else:
        return "No es palíndromo"

def contar_vocales(texto):
  vocales = "aeiou"
  contador = 0
  for letra in texto:
    if letra.lower() in vocales:
      contador += 1
  return contador



