from Tkinter import *
import tkFileDialog
import random
########################
# INITIAL VALUES
########################
root = Tk()
root.geometry("690x449")
root.wm_title('Encrypt/Decrypt')
root.wm_iconbitmap(default = 'Key.ico')
letters = list( ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
letters.append('\n')
key = list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
key.append('\n')
random.shuffle(key)
beginer_key = "".join(key)
new_phrase = ''
phrase = ''
########################
# FUNCTIONS
########################
def errorBox(text):
    messageBox = Tk()
    messageBox.geometry('200x100')
    messageBox.wm_title('ERROR')
    messageBox.wm_iconbitmap(default = 'Error.ico')
    messageBox.configure(background = 'red')
    t = Label(messageBox, text  = text,font=('arial',15), background = 'red')
    t3 = Button(messageBox, text = 'OK',font=('arial',15),
                command = lambda:messageBox.destroy(),
                width = 20, height = 2
                )
    t.pack()
    t3.pack()
    
def createDictionary(letters, key):
    '''Creates a dictionary using the alphebet and the key
    The first letter in the dictionary is the alphebat
    The second letter is the key alphebet
    It should correlate them correctly
    returns key dictionary'''
    keydict = {}
    
    for i in range(len(letters)):
        keydict[letters[i]] = key[i]
    return keydict


def encrypt(phrase,keydict):
    '''Encrypts the message
    Returns the new encrypted message'''
    newphrase = []
    for i in range(len(phrase)):
        if phrase[i] not in keydict:
            print 'not in',phrase[i]
            print
            newphrase.append(phrase[i])
        else:
            
            newphrase.append(keydict[phrase[i]])
        
    
    newphrase = "".join(newphrase)
    return newphrase

def placeText(key):
    entry1.delete(0,END)
    entry1.insert(0,key)
    
def generateKey():
    global key
    key = list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    key.append('\n')
    random.shuffle(key)
    key = "".join(key)
    print 'New key: ',key
    placeText(key)

def updateText(phrase,new_phrase):
    text = 'Phrase: %s \nNew Phrase: %s' % (phrase, new_phrase)
    label4.configure(state='normal')
    label4.delete(1.0,END)
    label4.insert(1.0,text)
    label4.configure(state='disabled')
def openFile():
    global textfile
    f = tkFileDialog.askopenfilename()
    print f
    if f == 'None':
        print 'Nothing was chosen'
    else:
        file = open(f)
        textfile = file.read()
        print textfile
        textfile = textfile.strip('\n')
        print textfile
        file.close()
        updateText(textfile,'')
        
def saveFile():
    global textfile
    u = tkFileDialog.asksaveasfilename()
    if u == 'None':
        print 'nothing was chosen'
    else:
        if var53.get() == 1 and var54.get() == 1:
            errorBox('You cant check\nboth')
        elif var53.get() == 1 and var54.get() == 0:
            key = entry1.get()
            file = open(u,'w')
            textfile = list(textfile)
            key_dict = createDictionary(letters,key)
            new_phrase = encrypt(textfile,key_dict)
            file.write(new_phrase)
            file.close()
            "".join(textfile)
            updateText(textfile,new_phrase)
        elif var53.get() == 0 and var54.get() == 1:
            key = entry1.get()
            file = open(u,'w')
            textfile = list(textfile)
            key_dict = createDictionary(key,letters)
            new_phrase = encrypt(textfile,key_dict)
            file.write(textfile)
            file.close()
            "".join(textfile)
            updateText(textfile,new_phrase)
        else:
            errorBox('You need to\ncheck a box')
                
        
    

   
def encryptMain():
    
    global key,new_phrase,phrase,var
    key = list(entry1.get())
    phrase = list(entry2.get())
    key_dict = createDictionary(letters,key)
    new_phrase = encrypt(phrase, key_dict)
    phrase = "".join(phrase)
    print 'Original Phrase: ',phrase
    print 'New Phrase: ',new_phrase
    updateText(phrase,new_phrase)


    
def decryptMain():
    global key,new_phrase,phrase
    key = list(entry1.get())
    phrase = list(entry2.get())
    key_dict = createDictionary(key,letters)
    new_phrase = encrypt(phrase,key_dict)
    phrase = "".join(phrase)
    print 'Original Phrase: ',phrase
    print 'New Phrase: ',new_phrase
    updateText(phrase,new_phrase)
def Main():
    phrase = entry2.get()
    if len(phrase) >= 60:
        print 'ERROR, USE A TEXT FILE, THATS TOO BIG TO BE A PHRASE LOSER'
        errorBox('That\'s too much!\nUse a text file')
        return
    elif var53.get() == 1 and var54.get() == 1:
        errorBox('You cant check\nboth')
    elif var53.get() == 1 and var54.get() == 0:
        encryptMain()
    elif var53.get() == 0 and var54.get() == 1:
        decryptMain()
    else:
        errorBox('You need to\ncheck a box')
def saveKey():
    u = tkFileDialog.asksaveasfilename()
    file = open(u,'w')
    file.write(entry1.get())
def openKey():
    f = tkFileDialog.askopenfilename()
    file = open(f)
    x = file.read()
    placeText(x)
########################
# BUILDING WIDGETS
########################

##
## Label 1
##
label1 = Label(root, text = 'Enter a key')
label1.place(x = 12, y = 9)
##
## label 2
##
label2 = Label(root, text = 'Enter phrase')
label2.place(x = 12, y = 88)
## Label 4 // the encrypted/decrypted text
##
label4 = Text(root, height=8,)
label4.insert(1.0, new_phrase)
label4.place(x = 12, y = 230)
label4.configure(state='disabled')
label4.configure(bg=root.cget('bg'), relief=FLAT)

##
## entry 1
##
entry1 = Entry(root)
entry1.place(x = 15, y = 25)
entry1.configure(width = 663)
entry1.insert(0,beginer_key)
##
## entry2
##
entry2 = Entry(root)
entry2.configure(width = 663)
entry2.place(x = 15, y = 104)
## encryptMainButton
##
encryptButton = Button(root, text = 'GO', command = Main, width = 15)
encryptButton.place(x = 15, y = 145)
##
## decryptButton
##
##decryptButton = Button(root, text = 'Decrypt', command = decryptMain)
##decryptButton.place(x = 90, y = 187)
##
## generateKeyButton
##
generateKeyButton = Button(root, text = 'Generate a random key',                         command = generateKey,)
generateKeyButton.place( x = 12, y = 56)
##
## saveKeyButton
##
saveKeyButton = Button(root,text = 'Save Key',command = saveKey)
saveKeyButton.place(x = 180, y = 56)
##
## openKeyButton
##
saveKeyButton = Button(root,text = 'Open Key',command = openKey)
saveKeyButton.place(x = 250, y = 56)
##
##open file button
##
openFileButton = Button(root, text = 'Open a file',command = openFile)
openFileButton.place(x = 160,y=145)
##
##save file button
##
saveFileButton = Button(root,text = 'Save a file',command = saveFile)
saveFileButton.place(x=230,y = 145)
##
##encrypt checkbox
##
var53 = IntVar()
checkBox2 = Checkbutton(root, text = 'Encrypt',variable = var53)
checkBox2.place(x = 160, y = 187)
##
##decrypt checkbox
##
var54 = IntVar()
checkBox3 = Checkbutton(root, text = 'Decrypt',variable = var54)
checkBox3.place(x = 230, y = 187)
##
##test
##
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Key", command=openKey)
filemenu.add_command(label="Open Text File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= lambda:root.destroy())
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


##
## mainloop
##
root.mainloop()
