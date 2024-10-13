# Works on the Replit IDE with the Tkinter option.

# ALL IMPORTS USED

# Citing Tkinter: Lundh, F. (1999). An introduction to tkinter. URL: Www. Pythonware. Com/Library/Tkinter/Introduction/Index. Htm.
import tkinter as tk
from tkinter import *
# End Citing

# Citing random: Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation
import random
# End Citing

# Unchanging lists for values that will be used in password creation or text encryption

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
undercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '=', '[', ']', '{', '}']
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET2 = "abcdefghijklmnopqrstuvwxyz"

# Beginning of Graphics and introductory text for MAIN PAGE

main_window = tk.Tk()
main_window.title("H.C.")
#width = main_window.winfo_screenwidth()
#height = main_window.winfo_screenheight()
#main_window.geometry("%dx%d" % (width, height))
main_window.geometry("875x387")
main_window.configure(bg='white')

heading1 = tk.Label(text = "Welcome to the Hub", background = "white", font = "Times 20 italic")
heading1.place(relx = 0.2, rely = 0.05, anchor = 'center')

heading2 = tk.Label(text = "Of Cryptography", background = "white", font = "Times 25 italic bold underline")
heading2.place(relx = 0.21, rely = 0.15, anchor = 'center')

introtext = tk.Label(text = "Try out privacy-based \n solutions to protecting \n your data.", background = "white", font = "Times 13")
introtext.place(relx = 0.2, rely = 0.38, anchor = 'center')

introtext2 = tk.Label(text = "See how strong your \n password is, or encrypt \n and decrypt any text \n using our various \n cryptographic services.", background = "white", font = "Times 13")
introtext2.place(relx = 0.2, rely = 0.68, anchor = 'center')

# Functions for buttons to lead to different pages

# All content for SECOND PAGE
def passwordpage():
 second_window = Toplevel()
 second_window.title("H.C. - Password Generator")
 second_window.geometry("875x387")
 second_window.configure(bg='white')

 # Button leading back to MAIN PAGE
 main_page_button = tk.Button(second_window, text = "Home Page", foreground = "white", background = "black", command = second_window.destroy)
 main_page_button.place(relx = 0.07, rely = 0.95, anchor = 'center')

 # Label for Newly Generated Password
 newpasslabel = tk.Label(second_window, text = "", background = "white", font = "Times 13 bold")
 newpasslabel.place(relx = 0.25, rely = 0.675, anchor = 'center')

 # Actual Password Generator
 def checker():
  hithere = int(let_amount_entry.get())
  hithere2 = int(let_amount_entry2.get())
  hithere3 = int(let_amount_entry3.get())
  PASSWORD_num = ""
  PASSWORD_sym = ""
  PASSWORD_let = ""
  PASSWORD_new = ""
  for i in range(hithere):
   letterq = random.choice(letters)
   PASSWORD_let = PASSWORD_let + letterq
  #print(PASSWORD_let)
  for i in range(hithere2):
   numberq = random.choice(numbers)
   PASSWORD_num = PASSWORD_num + numberq
  #print(PASSWORD_num)
  for i in range(hithere3):
   symbolq = random.choice(symbols)
   PASSWORD_sym = PASSWORD_sym + symbolq
  #print(PASSWORD_sym)
  PASSWORD_new = PASSWORD_let + PASSWORD_num + PASSWORD_sym
  #print(PASSWORD_new)
  passwordlist = list(PASSWORD_new)
  passrandom = random.choice(passwordlist)
  newpassrandom = ""
  for i in range(len(passwordlist)):
   newpassrandom += passrandom
   passwordlist.remove(passrandom)
   if len(passwordlist) <= 0:
    break
   passrandom = random.choice(passwordlist)
  #print(newpassrandom)
  newpasslabel.configure(text = "New Password: " + str(newpassrandom))

 # User inputs

 let_amount_intro = tk.Label(second_window, text = "How many letters do you want in your password?", background = "white", font = "Times 12")
 let_amount_intro.place(relx = 0.25, rely = 0.07, anchor = 'center')
 let_amount_entry = tk.Entry(second_window, width = 50)
 let_amount_entry.place(relx = 0.25, rely = 0.125, anchor = 'center')

 letbutton = tk.Button(second_window, text = "Enter after filling out boxes above", foreground = "white", background = "black", command = checker)
 letbutton.place(relx = 0.25, rely = 0.565, anchor = 'center')

 let_amount_intro2 = tk.Label(second_window, text = "How many numbers do you want in your password?", background = "white", font = "Times 12")
 let_amount_intro2.place(relx = 0.25, rely = 0.235, anchor = 'center')
 let_amount_entry2 = tk.Entry(second_window, width = 50)
 let_amount_entry2.place(relx = 0.25, rely = 0.29, anchor = 'center')
 let_amount_intro3 = tk.Label(second_window, text = "How many symbols do you want in your password?", background = "white", font = "Times 12")
 let_amount_intro3.place(relx = 0.25, rely = 0.4, anchor = 'center')
 let_amount_entry3 = tk.Entry(second_window, width = 50)
 let_amount_entry3.place(relx = 0.25, rely = 0.455, anchor = 'center')

# All content for THIRD PAGE
def securitypage():
 third_window = Toplevel()
 third_window.title("H.C. - Password Security")
 third_window.geometry("875x387")
 third_window.configure(bg='white')

 securelabelmain = tk.Label(third_window, text = "Your password should have many letters, numbers, and symbols.", background = "white", font = "Times 15 italic")
 securelabelmain.pack()

 # Modifiable counts for different parts of password
 countlabel1 = tk.Label(third_window, text = "", background = "white", font = "Times 11")
 countlabel1.place(relx = 0.13, rely = 0.425, anchor = 'center')
 countlabel2 = tk.Label(third_window, text = "", background = "white", font = "Times 11")
 countlabel2.place(relx = 0.13, rely = 0.48, anchor = 'center')
 countlabel3 = tk.Label(third_window, text = "", background = "white", font = "Times 11")
 countlabel3.place(relx = 0.13, rely = 0.535, anchor = 'center')
 countlabel4 = tk.Label(third_window, text = "", background = "white", font = "Times 11")
 countlabel4.place(relx = 0.13, rely = 0.59, anchor = 'center')
 countlabel5 = tk.Label(third_window, text = "", background = "white", font = "Times 11")
 countlabel5.place(relx = 0.13, rely = 0.645, anchor = 'center')
 finallabel = tk.Label(third_window, text = "", background = "white", font = "Times 15 bold")
 finallabel.pack(side = BOTTOM)

 # Analysis of password given
 def security(user_password):
   global seplist
   seplist = []
   # Process of iterating through password and seeing what it contains
   if passwordentry.get() != "":
    seplist = list(passwordentry.get())
    #print(seplist)
   else:
    seplist = list(user_password)
    #print(seplist)
   lowercasecount = 0
   uppercasecount = 0
   numcount = 0
   symcount = 0
   #print("hi")
   for i in range(len(seplist)):
    for a in range(len(undercase_letters)):
     if seplist[i] == undercase_letters[a]:
       lowercasecount += 1
    for b in range(len(uppercase_letters)):
     if seplist[i] == uppercase_letters[b]:
       uppercasecount += 1
    for c in range(len(numbers)):
     if seplist[i] == numbers[c]:
       numcount += 1
    for d in range(len(symbols)):
     if seplist[i] == symbols[d]:
       symcount += 1
    #print(lowercasecount)
   countlabel1.configure(text = "Lowercase Letters: " + str(lowercasecount))
   #print(uppercasecount)
   countlabel2.configure(text = "Uppercase Letters: " + str(uppercasecount))
   #print(numcount)
   countlabel3.configure(text = "Numbers: " + str(numcount))
   #print(symcount)
   countlabel4.configure(text = "Symbols: " + str(symcount))
   countlabel5.configure(text = "Amount of Characters: " + str(len(seplist)))

   # Deducing if password is strong or not
   if len(seplist) >= 12:
     if lowercasecount >= 3 and uppercasecount >= 3 and numcount >= 3 and symcount >= 3:
      finallabel.configure(text = "Congrats! Your password is \n as strong as strong could be.", foreground = "red")
     elif lowercasecount < 3:
      finallabel.configure(text = "Your password is not secure, \n and it needs at least 3 lowercase letters.")
     elif uppercasecount < 3:
      finallabel.configure(text = "Your password is not secure, \n and it needs at least 3 uppercase letters.")
     elif numcount < 3:
      finallabel.configure(text = "Your password is not secure, \n and it needs at least 3 numbers.")
     elif symcount < 3:
      finallabel.configure(text = "Your password is not secure, \n and it needs at least 3 symbols.")
   else:
     finallabel.configure(text = "Your password is not at all secure. \n Add up to 12 characters.")

 def security_input():
  passwordentry.delete(0, END)
  static = 1
  while static == 1:
   staticinput = input("Enter your password to test its security: ")
   security(staticinput)
   print("Look above to read about your password's security!")
   print("")
   userq2 = input("Would you like to try again? 1 for yes, and 2 for no: ")
   if userq2 != "1":
    break

 # User input
 passwordintro = tk.Label(third_window, text = "Enter your password:", background = "white", font = "Times 12")
 passwordintro.place(relx = 0.13, rely = 0.15, anchor = 'center')
 passwordentry = tk.Entry(third_window, width = 40)
 passwordentry.place(relx = 0.20, rely = 0.205, anchor = 'center')
 passwordbutton = tk.Button(third_window, text = "Enter after filling out above", foreground = "white", background = "black", command = lambda: security(""))
 passwordbutton.place(relx = 0.20, rely = 0.315, anchor = 'center')
 alternative = tk.Button(third_window, text = "Click here if you want to use the console!", foreground = "white", background = "black", command = security_input)
 alternative.pack(side = BOTTOM)


 # Button leading back to MAIN PAGE
 main_page_button = tk.Button(third_window, text = "Home Page", foreground = "white", background = "black", command = third_window.destroy)
 main_page_button.place(relx = 0.07, rely = 0.95, anchor = 'center')

# All content for FOURTH PAGE
def caesarpage():
 fourth_window = Toplevel()
 fourth_window.title("H.C. - Caesar Cypher")
 fourth_window.geometry("875x387")
 fourth_window.configure(bg='white')

 # Functions for Caesar encryption and decryption

 def storevalue():
  secret_key = int(fourthshiftentry.get())
  #print(secret_key)
  return secret_key

 # Citing encrypt function from https://codehs.com/student/2019991/section/339406/assignment/55681830/
 def encrypt():
  encryptresult = ""
  encryptinput = str(fourthentry.get())
  encryptinput = encryptinput.upper()
  #print(encryptinput)
  for character in encryptinput:
   indexcheck = ALPHABET.find(character)
   if indexcheck >= 0:
    new_index = indexcheck + storevalue()
    new_index = new_index % len(ALPHABET)
    newchar = ALPHABET[new_index]
    encryptresult += newchar
   else:
    encryptresult += character
   fourthoutput.configure(text = "Encrypted Form: " + str(encryptresult))
 # End citing

 # Citing decrypt function from https://codehs.com/student/2019991/section/339406/assignment/55681831/
 def decrypt():
  decryptresult = ""
  decryptinput = str(fourthentry2.get())
  decryptinput = decryptinput.lower()
  #print(decryptinput)
  for character in decryptinput:
   indexcheck = ALPHABET2.find(character)
   if indexcheck >= 0:
    new_index = indexcheck + -(storevalue())
    new_index = new_index % len(ALPHABET2)
    newchar = ALPHABET2[new_index]
    decryptresult += newchar
   else:
    decryptresult += character
   fourthoutput2.configure(text = "Decrypted Form: " + str(decryptresult))
 # End citing

 # Encryption info
 fourthintro = tk.Label(fourth_window, text = "Encrypt your text below:", background = "white", font = "Times 12")
 fourthintro.place(relx = 0.25, rely = 0.07, anchor = 'center')
 fourthentry = tk.Entry(fourth_window, width = 50)
 fourthentry.place(relx = 0.25, rely = 0.125, anchor = 'center')
 fourthbutton = tk.Button(fourth_window, text = "Enter", foreground = "white", background = "black", command = encrypt)
 fourthbutton.place(relx = 0.65, rely = 0.125, anchor = 'center')
 fourthoutput = tk.Label(fourth_window, text = "", background = "white", font = "Times 12 bold")
 fourthoutput.place(relx = 0.25, rely = 0.235, anchor = 'center')

 # Decryption info
 fourthintro2 = tk.Label(fourth_window, text = "Decrypt your text below:", background = "white", font = "Times 12")
 fourthintro2.place(relx = 0.25, rely = 0.345, anchor = 'center')
 fourthentry2 = tk.Entry(fourth_window, width = 50)
 fourthentry2.place(relx = 0.25, rely = 0.4, anchor = 'center')
 fourthbutton2 = tk.Button(fourth_window, text = "Enter", foreground = "white", background = "black", command = decrypt)
 fourthbutton2.place(relx = 0.65, rely = 0.4, anchor = 'center')
 fourthoutput2 = tk.Label(fourth_window, text = "", background = "white", font = "Times 12 bold")
 fourthoutput2.place(relx = 0.25, rely = 0.51, anchor = 'center')

 # How much to shift
 fourthshift = tk.Label(fourth_window, text = "Shift Value: (To the right on alphabet)", background = "white", font = "Times 12 italic underline")
 fourthshift.place(relx = 0.25, rely = 0.62, anchor = 'center')
 fourthshiftentry = tk.Entry(fourth_window, width = 50)
 fourthshiftentry.place(relx = 0.25, rely = 0.675, anchor = 'center')
 fourthshiftbutton = tk.Button(fourth_window, text = "Enter", foreground = "white", background = "black", command = storevalue)
 fourthshiftbutton.place(relx = 0.65, rely = 0.675, anchor = 'center')

 # Button leading back to MAIN PAGE
 main_page_button = tk.Button(fourth_window, text = "Home Page", foreground = "white", background = "black", command = fourth_window.destroy)
 main_page_button.place(relx = 0.07, rely = 0.95, anchor = 'center')

# All content for FIFTH PAGE
def binarypage():
 fifth_window = Toplevel()
 fifth_window.title("H.C. - Binary Conversion")
 fifth_window.geometry("875x387")
 fifth_window.configure(bg='white')

 fifthinfo = tk.Label(fifth_window, text = "For a change,\n look at the console for the conversions!", background = "white", font = "Times 14 bold italic")
 fifthinfo.place(relx = 0.5, rely = 0.5, anchor = 'center')

 # Button leading back to MAIN PAGE
 main_page_button = tk.Button(fifth_window, text = "Home Page", foreground = "white", background = "black", command = fifth_window.destroy)
 main_page_button.place(relx = 0.07, rely = 0.95, anchor = 'center')

 def deca_bin(deca_num):
  # Converts the Unicode equivalent of user input into binary, and then into a string variable.
  # The [2:] removes any unnecessary characters in the binary--like "0b", which frequently appears.
  binary_value = str(bin(deca_num))[2:]
  # If the binary number does not need 8 bits, then it will add 0s to it until it reaches it, as 8 bits per byte is the standard.
  while len(binary_value) < 8:
   binary_value = "0" + binary_value
  return binary_value

 def encrypt_bin(binaryinput):
  binary_string = ""
  txtlist = list(binaryinput)
  for i in range(len(txtlist)):
   # Converts user input to Unicode characters 1 by 1 to ensure there is no mistranslation.
   numeric_value = ord(txtlist[i])
   # Converts each Unicode character to binary using previous function.
   binval = deca_bin(numeric_value)
   # Adds this binary number to string variable.
   binary_string += binval + " "
  return binary_string

 # User input for text-to-binary.
 def fifthprocess():
  encryptq = "1"
  while encryptq == "1":
   binaryinput = input("What text would you like to translate to binary?: ")
   finalencrypt = encrypt_bin(binaryinput)
   print(finalencrypt)
   encryptq2 = input("Do you want to encrypt more text? Enter 1 for yes, and 2 for no. \n")
   if encryptq2 != "1":
    print("Come back soon!")
    break

 fifthprocess()

# Text and buttons for application's features that the user can try out; all on MAIN PAGE

generatortext = tk.Label(text = "Generate a security password here:", background = "white", foreground = "lightblue", font = "Times 12 italic")
generatortext.place(relx = 0.7, rely = 0.05, anchor = 'center')

generatorbutton = tk.Button(text = "Click!", background = "black", foreground = "white", command = passwordpage)
generatorbutton.place(relx = 0.91, rely = 0.05, anchor = 'center')

securitytext = tk.Label(text = "Find out how secure your password is:", background = "white", foreground = "aquamarine3", font = "Times 12 italic")
securitytext.place(relx = 0.7, rely = 0.275, anchor = 'center')

securitybutton = tk.Button(text = "Click!", background = "black", foreground = "white", command = securitypage)
securitybutton.place(relx = 0.92, rely = 0.275, anchor = 'center')

caesartext = tk.Label(text = "Encrypt/Decrypt info with a Caesar cypher:", background = "white", foreground = "blue", font = "Times 12 italic")
caesartext.place(relx = 0.7, rely = 0.6, anchor = 'center')

caesarbutton = tk.Button(text = "Click!", background = "black", foreground = "white", command = caesarpage)
caesarbutton.place(relx = 0.94, rely = 0.6, anchor = 'center')

newcyphertext = tk.Label(text = "Encrypt/Decrypt info w/ Binary:", background = "white", foreground = "darkblue", font = "Times 12 italic")
newcyphertext.place(relx = 0.7, rely = 0.9, anchor = 'center')

newcypherbutton = tk.Button(text = "Click!", background = "black", foreground = "white", command = binarypage)
newcypherbutton.place(relx = 0.89, rely = 0.9, anchor = 'center')

# Loads MAIN PAGE
main_window.mainloop()