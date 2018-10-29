from easygui import*
import sys
list1=[]
sum1=0
while 1:
  msgbox("welcome to e-bazar")
  i=buttonbox("which product do you want?","available products",choices=("chocolate","biscuit","soap"))
  if i=="chocolate":
      j=buttonbox("which chocolate do you want?","available chocolates",choices=("kitkat","munch","perk"))
      if j=="kitkat":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=10Rs","d mart=9.5Rs"))
       if k=="bigbazar=10Rs":
         l=10
       else:
         l=9.5
      elif j=="munch":
       k=buttonbox("from where to buy?","available veendors",choices=("bigbazar=4.5Rs","d mart=5Rs"))
       if k=="bigbazar=4.5Rs":
         l=4.5
       else:
         l=5
      elif j=="perk":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=7Rs","d mart=8Rs"))
       if k=="bigbazar=7Rs":
         l=7
       else:
         l=8 
  elif i=="biscuit": 
      j=buttonbox("which biscuit do you want?","available biscuits",choices=("oreo","marie","bourbon")) 
      if j=="oreo":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=20Rs","d mart=22Rs"))
       if k=="bigbazar=20Rs":
         l=20
       else:
         l=22
      elif j=="marie":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=35Rs","d mart=30Rs"))
       if k=="bigbazar=35Rs":
         l=35
       else:
         l=30
      elif j=="bourbon":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=45Rs","d mart=47Rs"))
       if k=="bigbazar=45Rs":
         l=45
       else:
         l=47
  elif i=="soap":
      j=buttonbox("which soap do you want?","available soaps",choices=("fiama","medimix","pears"))
      if j=="fiama":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=58Rs","d mart=55Rs"))
       if k=="bigbazar=58Rs":
         l=58
       else:
         l=55
      elif j=="medimix":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=39Rs","d mart=35Rs"))
       if k=="bigbazar=39Rs":
         l=39
       else:
         l=35
      elif j=="pears":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=70Rs","d mart=65Rs"))
       if k=="bigbazar=70Rs":
         l=70
       else:
         l=65
  msgbox("You chose: " + str(choices) +  "Survey Result")

  msg = "Do you want to continue?"
  title = "Please Confirm"
  if ccbox(msg, title):     # show a Continue/Cancel dialog
      pass  # user chose Continue
  else:
      textbox('purchase memo','bill desk',text=list1)
      sys.exit(0)

