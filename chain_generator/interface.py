#!/usr/bin/python

import tkinter as tk
import program as pro
import webbrowser
#startup

root = tk.Tk()
root.title = 'ß- Decay Chain Generator'
root.geometry('400x450')

g0 = tk.Label(root,text = 'Welcome to the Beta Decay Chain Generator')

#the button is perfect now!
info = tk.Button(root,
    text='User Information',
    width=10,
    height=3,
    bg='black',
    fg='green',)
#that button opens the README.md file from github

def callback(url):
    webbrowser.open_new(url)
info.bind('<Button-1>', lambda e: callback('https://github.com/kwatts-4/beta-decay-chains/blob/main/README.md'))

#packing current widgets
ww0 = [g0,info]
for ww in ww0:
    ww.pack()
    
g1 = tk.Label(root,text = 'Please enter a nuclide')
g2 = tk.Label(root,text = 'eg. 88As')

e0 = tk.Entry()
ww1 = [g1,g2,e0]
for ww in ww1:
    ww.pack()

g3 = tk.Label(root,text = 'Where should your csv file be saved?')
g4 = tk.Label(root,text = 'Please enter the full file path \n including the final /')

e1 = tk.Entry()

v0 = tk.IntVar()
v1 = tk.IntVar()
c0 = tk.Checkbutton(root, text = 'Print to Console', variable = v0)
c1 = tk.Checkbutton(root, text = 'Fill Null Values', variable = v1)

generate = tk.Button(root,
    text='Generate Chains',
    width=10,
    height=3,
    bg='black',
    fg='green')

def run():
    nuclide = str(e0.get())
    filepath = str(e1.get())
    check0 = v0.get()
    check1 = v1.get()
    if check0 == 1 and check1 == 1:
        pro.main(nuclide,filepath,Print=True,noNULL=True)
        g5 = tk.Label(root,text = 'File Decay_Chains_'+str(nuclide)+'_Filled.csv has been saved')
    elif check0 == 1:
        pro.main(nuclide,filepath,Print=True)
        g5 = tk.Label(root,text = 'File Decay_Chains_'+str(nuclide)+'.csv has been saved')
    elif check1 == 1:
        pro.main(nuclide,filepath,noNULL=True)
        g5 = tk.Label(root,text = 'File Decay_Chains_'+str(nuclide)+'_Filled.csv has been saved')
    else: 
        pro.main(nuclide,filepath)
        g5 = tk.Label(root,text = 'File Decay_Chains_'+str(nuclide)+'.csv has been saved')
    
    g5.pack()
    

generate.bind('<Button-1>', lambda e: run())

ww2 = [g3,g4,e1,c0,c1,generate]
for ww in ww2:
    ww.pack()
    
root.mainloop()


