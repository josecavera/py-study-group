def palindromo(sentencia):
    reves = sentencia[-1::-1].lower().replace(" ", "")
    print(reves)
    return sentencia.lower().replace(" ", "") == reves


print(palindromo("Super palindromo"))
