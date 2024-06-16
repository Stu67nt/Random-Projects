from letterUsage import letter_count

A_c = 0
B_c = 0
C_c = 0
D_c = 0
E_c = 0
F_c = 0
G_c = 0
H_c = 0
I_c = 0
J_c = 0
K_c = 0
L_c = 0
M_c = 0
N_c = 0
O_c = 0
P_c = 0
Q_c = 0
R_c = 0
S_c = 0
T_c = 0
U_c = 0
V_c = 0
W_c = 0
X_c = 0
Y_c = 0
Z_c = 0

file = open("wordledic.txt",'r')
lines = file.readlines() 

for line in lines:
  for letter in line:
    if letter == 'a':
      A_c = A_c+1
    if letter == 'b':
      B_c = B_c+1
    if letter == 'c':
      C_c = C_c+1
    if letter == 'd':
      D_c = D_c+1
    if letter == 'e':
      E_c = E_c+1
    if letter == 'f':
      F_c = F_c+1
    if letter == 'g':
      G_c = G_c+1
    if letter == 'h':
      H_c = H_c+1
    if letter == 'i':
      I_c = I_c+1
    if letter == 'j':
      J_c = J_c+1
    if letter == 'k':
      K_c = K_c+1
    if letter == 'l':
      L_c = L_c+1
    if letter == 'm':
      M_c = M_c+1
    if letter == 'n':
      N_c = N_c+1
    if letter == 'o':
      O_c = O_c+1
    if letter == 'p':
      P_c = P_c+1
    if letter == 'q':
      Q_c = Q_c+1
    if letter == 'r':
      R_c = R_c+1
    if letter == 's':
      S_c = S_c+1
    if letter == 't':
      T_c = T_c+1
    if letter == 'u':
      U_c = U_c+1
    if letter == 'v':
      V_c = V_c+1
    if letter == 'w':
      W_c = W_c+1
    if letter == 'x':
      X_c = X_c+1
    if letter == 'y':
      Y_c = Y_c+1
    if letter == 'z':
      Z_c = Z_c+1

while True:
  wordleLetter = input('Input a letter: ')
  wordleLetter = wordleLetter.upper()
  
  if wordleLetter == 'A':
    print(A_c)
    letter_count.update(
      {
        'A': A_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'B':
    print(B_c)
    letter_count.update(
      {
        'B': B_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'C':
    print(C_c)
    letter_count.update(
      {
        'C': C_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'D':
    print(D_c)
    letter_count.update(
      {
        'D': D_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'E':
    print(E_c)
    letter_count.update(
      {
        'E': E_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'F':
    print(F_c)
    letter_count.update(
      {
        'F': F_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'G':
    print(G_c)
    letter_count.update(
      {
        'G': G_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
  
  elif wordleLetter == 'H':
    print(H_c)
    letter_count.update(
      {
        'H': H_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'I':
    print(I_c)
    letter_count.update(
      {
        'I': I_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'J':
    print(J_c)
    letter_count.update(
      {
        'J': J_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'K':
    print(K_c)
    letter_count.update(
      {
        'K': K_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'L':
    print(L_c)
    letter_count.update(
      {
        'L': L_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'M':
    print(M_c)
    letter_count.update(
      {
        'M': M_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'N':
    print(N_c)
    letter_count.update(
      {
        'N': N_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'O':
    print(O_c)
    letter_count.update(
      {
        'O': O_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'P':
    print(P_c)
    letter_count.update(
      {
        'P': P_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'Q':
    print(Q_c)
    letter_count.update(
      {
        'Q': Q_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'R':
    print(R_c)
    letter_count.update(
      {
        'R': R_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'S':
    print(S_c)
    letter_count.update(
      {
        'S': S_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'T':
    print(T_c)
    letter_count.update(
      {
        'T': T_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'U':
    print(U_c)
    letter_count.update(
      {
        'U': U_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'V':
    print(V_c)
    letter_count.update(
      {
        'V': V_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'W':
    print(W_c)
    letter_count.update(
      {
        'W': W_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'X':
    print(X_c)
    letter_count.update(
      {
        'X': X_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'Y':
    print(Y_c)
    letter_count.update(
      {
        'Y': Y_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  elif wordleLetter == 'Z':
    print(Z_c)
    letter_count.update(
      {
        'Z': Z_c
      }
    )
    with open('letterUsage.py','w') as file:
      file.write('letter_count = '+str(letter_count))
    file.close()
    
  else:
    print('Invalid option please enter 1 letter of the english alphabet.(A-Z)')