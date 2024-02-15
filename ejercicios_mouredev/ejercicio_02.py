""" 
        ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
  """


def is_anagram(word1,word2):
    word1_low = word1.lower()
    word2_low = word2.lower()
    if word1_low == word2_low:
        return False
    return sorted(word1_low) == sorted(word2_low)


print(is_anagram("Amor","Roma"))