from tkinter import Label,Button,Frame,Tk,RAISED
def button_num_click(num):
   global equation_text
   equation_text+=str(num)
   label.config(text=equation_text)
def equal():
   global equation_text
   for i in range(len(equation_text)):
      if equation_text[i]=='^':
         equation_text=equation_text[:i]+'**'+equation_text[i+1:]
      elif equation_text[i]=='÷':
         equation_text=equation_text[:i]+'/'+equation_text[i+1:]
      elif equation_text[i]=='x':
         equation_text=equation_text[:i]+'*'+equation_text[i+1:]
   try:
      total=str(eval(equation_text))
      label['text']=total
      equation_text=total
   except ZeroDivisionError :
      label['text']='ZeroDivisionError'
      equation_text=''
   except SyntaxError:
      label['text']='ArithmeticError'
      equation_text=''
def backspace():
   global equation_text
   equation_text=equation_text[0:-1]
   label['text']=equation_text
def clear():
   global equation_text
   equation_text=''
   label['text']=equation_text
def change():
   global number
   for i in number:
      if '.' == num_button['text']:
         num_button['text']=')'
         num_button['command']=lambda:button_num_click(')')
   bs_button['text']='('
   bs_button['command']=lambda:button_num_click('(')
   change_button['command']=rechange
def rechange():
   global number
   for i in number:
      if ')' == num_button['text']:
         num_button['text']='.'
         num_button['command']=lambda:button_num_click('.')
         change_button['command']=change
   bs_button['text']='DEL'
   bs_button['command']=backspace
   change_button['command']=change

window=Tk()

window.title('the calculator')
equation_text=''
number={1:[2,1],2:[2,2],3:[2,3],4:[3,1],5:[3,2],6:[3,3],7:[4,1],8:[4,2],9:[4,3],0:[5,2],
        '^':[1,1],'÷':[1,2],'x':[1,3],'-':[1,4],'+':[2,4,2],'.':[5,3]}
label=Label(window,font=('Consolas',20),bg='white',width=24,height=3)
label.pack()
frame=Frame(window,relief=RAISED)
frame.pack()

for i in number:
   try:
      num_button=Button(frame,text=i,height=9,width=9,font=35)
      num_button.grid(row=number[i][0],column=number[i][1],rowspan=number[i][2])
   except:
      num_button=Button(frame,text=i,height=4,width=9,font=35)
      num_button.grid(row=number[i][0],column=number[i][1])
   if i==1:
      num_button['command']=lambda:button_num_click(1)
   if i==2:
      num_button['command']=lambda:button_num_click(2)
   if i==3:
      num_button['command']=lambda:button_num_click(3)
   if i==4:
      num_button['command']=lambda:button_num_click(4)
   if i==5:
      num_button['command']=lambda:button_num_click(5)
   if i==6:
      num_button['command']=lambda:button_num_click(6)
   if i==7:
      num_button['command']=lambda:button_num_click(7)
   if i==8:
      num_button['command']=lambda:button_num_click(8)
   if i==9:
      num_button['command']=lambda:button_num_click(9)
   if i==0:
      num_button['command']=lambda:button_num_click(0)
   if i=='^':
      num_button['command']=lambda:button_num_click('^')
   if i=='÷':
      num_button['command']=lambda:button_num_click('÷')
   if i=='x':
      num_button['command']=lambda:button_num_click('x')
   if i=='-':
      num_button['command']=lambda:button_num_click('-')
   if i=='+':
      num_button['command']=lambda:button_num_click('+')
   if i=='.':
      num_button['command']=lambda:button_num_click('.')
bs_button=Button(frame,text='DEL',height=4,width=9,font=35,command=backspace)
bs_button.grid(row=5,column=1)
equal_button=Button(frame,text='=',height=9,width=9,font=35,command=equal)
equal_button.grid(row=4,column=4,rowspan=2)
clear_button=Button(frame,text='AC',height=4,width=29,font=35,command=clear)
clear_button.grid(row=6,column=1,columnspan=3)
change_button=Button(frame,text='c',height=4,width=9,font=40,command=change)
change_button.grid(row=6,column=4)


window.mainloop()
