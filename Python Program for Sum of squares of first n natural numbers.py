# Programa Python3 para 
# encontre a soma do quadrado 
# do primeiro n natural  
# números 
  
  
# Retorna a soma de 
# quadrado do primeiro f— 
# números naturais 
def squaresum(n) : 
  
    # Iterar de 1 
    # e n achando 
    # quadrado de eu e 
    # adicione à soma. 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
  
# Programa orientado 
n = 4
print(squaresum(n)) 
  
# Este código é contribuído por Dorgival Fernando. * / 