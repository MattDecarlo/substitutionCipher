from Tkinter import *
import tkFileDialog
import random

########################
# INITIAL VALUES
########################

root = Tk()
root.geometry('1050x540')
root.wm_title('Encrypt/Decrypt')
root.wm_iconbitmap(default = 'Key.ico')
##
# Makes intial Key
# Default is un adjusted
##
letters = list( ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
letters.append('\n')
key = list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
key.append('\n')
beginer_key = "".join(key)
##
phrase = ''
new_phrase = ''

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
                width = 20, height = 2)
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
    text = 'Phrase: %s \n\nNew Phrase: %s' % (phrase, new_phrase)
    label4.configure(state='normal')
    label4.delete(1.0,END)
    label4.insert(1.0,text)
    label4.configure(state='disabled')
    
def openFile():
    global textfile
    f = tkFileDialog.askopenfilename()
    entry2.delete(0,END)
    if f == 'None':
        print 'Nothing was chosen'
    else:
        file = open(f)
        textfile = file.read()
        file.close()
        entry2.insert(0,textfile)
        
def saveFile():
    global textfile
    u = tkFileDialog.asksaveasfilename()
    if u == 'None':
        print 'nothing was chosen'
    else:
        file = open(u,'w')
        file.write(new_phrase)
        file.close()
            
def saveKey():
    u = tkFileDialog.asksaveasfilename()
    file = open(u,'w')
    file.write(entry1.get())
    
def openKey():
    f = tkFileDialog.askopenfilename()
    file = open(f)
    x = file.read()
    placeText(x)
    
def encryptMain():   
    global key,new_phrase,phrase,var
    key = list(entry1.get())
    phrase = list(entry2.get())
    key_dict = createDictionary(letters,key)
    new_phrase = encrypt(phrase, key_dict)
    phrase = "".join(phrase)
    print 'Original Phrase: ',phrase
    print 'New Phrase: ',new_phrase
    
    
def decryptMain():
    global key,new_phrase,phrase
    key = list(entry1.get())
    phrase = list(entry2.get())
    key_dict = createDictionary(key,letters)
    new_phrase = encrypt(phrase,key_dict)
    phrase = "".join(phrase)
    print 'Original Phrase: ',phrase
    print 'New Phrase: ',new_phrase
    
def checkTextFile():
    global phrase
    if 'textfile' in globals():
        phrase = textfile
    else:
        return
def Main():
    global new_phrase
    phrase = entry2.get()
    checkTextFile()
    print 'phrase',phrase
    if var53.get() == 1 and var54.get() == 1:
        errorBox('You cant check\nboth')
    elif var53.get() == 1 and var54.get() == 0:
        encryptMain()
        updateText(phrase,new_phrase)
    elif var53.get() == 0 and var54.get() == 1:
        decryptMain()
        updateText(phrase,new_phrase)
    else:
        errorBox('You need to\ncheck a box')

        
########################
# BUILDING WIDGETS
########################

##########################################################################
'''Group 1 - KEY'''
##########################################################################
group1 = LabelFrame(root, text = 'Key', padx = 2, pady = 20,
                    width = 875, height = 88)
group1.place(x = 12, y = 12)

##
##Entry Box
##
entry1 = Entry(group1)
entry1.grid(row = 0, column = 0,padx = 6, pady = 1)
entry1.configure(width = 100)
entry1.insert(0,beginer_key)
##
## Generate Key Button
##
generateKeyButton = Button(group1, text = 'Generate a random key',command = generateKey,)
generateKeyButton.grid(row = 0, column = 1, padx = 6, pady = 1)
generateKeyButton.configure(width = 25)
##
## saveKeyButton
##
saveKeyButton = Button(group1,text = 'Save Key',command = saveKey)
saveKeyButton.grid(row = 0, column = 2, padx = 6, pady = 1)
saveKeyButton.configure(width = 25)

##########################################################################
'''Group 2 - TEXT'''
##########################################################################
group2 = LabelFrame(root, text = 'Text', padx = 2, pady = 1,
                    width = 875, height = 88)
group2.place(x = 12, y = 132)
##
## entry2
##
entry2 = Entry(group2)
entry2.configure(width = 100)
entry2.grid(row = 0, column = 0,padx = 6, pady = 20)
##
## encryptMainButton
##
encryptButton = Button(group2, text = 'Encrypt/Decrypt', command = Main, width = 54)
encryptButton.grid(row = 0, column = 1, padx = 6, pady = 1, columnspan = 2)
##
##encrypt checkbox
##
var53 = IntVar()
checkBox2 = Checkbutton(group2, text = 'Encrypt',variable = var53)
checkBox2.grid(row  = 1, column = 1)
##
##decrypt checkbox
##
var54 = IntVar()
checkBox3 = Checkbutton(group2, text = 'Decrypt',variable = var54)
checkBox3.grid(row  = 1, column = 2)



##########################################################################
'''Group 3 - NEW TEXT'''
##########################################################################
group3 = LabelFrame(root, text = 'New Text', padx = 2, pady = 20)
group3.place(x = 12, y = 275)
##
##label4
##
label4 = Text(group3, height=8, width = 126)
label4.insert(1.0, new_phrase)
label4.pack()
label4.configure(state='disabled')
label4.configure(bg=root.cget('bg'), relief=FLAT)


#####################
##Save Button
#####################
##
##save file button
##
saveFileButton = Button(root,text = 'Save a file',command = saveFile, width = 139)
saveFileButton.place(x=24,y = 476)

#####################
##Menu Bar
#####################
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
                
        
    
