from tkinter import *
import datetime

months = [
	"January", "February", "March", "April", "May",
	"June", "July", "August", "September", "October",
	"November", "December" 
]

ranges = {}
	
ranges['January'],   ranges['February'] = ((31, 32), (1, 32), (1, 11)),  ((28, 32), (1, 29), (1, 11))
ranges['March'],     ranges['April']    = ((25, 29), (1, 32), (1, 8)),  ((25, 32), (1, 31), (1, 6))
ranges['May'],       ranges['June']     = ((29, 31), (1, 32), (1, 10)),  ((27, 32), (1, 31), (1, 8))

ranges['July'],      ranges['August']   = ((24, 31), (1, 32), (1, 5)),  ((29, 32), (1, 32), (1, 9))
ranges['September'], ranges['October']  = ((26, 32), (1, 31), (1, 7)),  ((30, 31), (1, 32), (1, 11))
ranges['November'],  ranges['December'] = ((28, 32), (1, 31), (1, 9)),  ((25, 31), (1, 32), (1, 6))

calendar = {}
for month, start_ends in ranges.items():
	calendar[month] = sum((list(range(*start_end)) for start_end in start_ends), [])

ht = 2
bg1 =  "white" #"#829356"
fg1 = "black"
bg2 =  "#FFD469" #"blue" "#829356"    
fg2 = "white"
bg3 = "black"
current_year = "2017"

def replace(month, operation): # "+" or "-"
	if operation == "+":
		if months.index(month) == 11:
			return months[0]
		else:	
			return months[months.index(month)+1]
	elif operation == "-":
		return months[months.index(month)-1]
		
def replace_back(*args):		
	l1.configure(text=replace(l1["text"], "-"))
	
	change_month(calendar[l1["text"]])
	load()
	
def replace_forward(*args):
	l1.configure(text=replace(l1["text"], "+"))
	
	change_month(calendar[l1["text"]])
	load()
		
def edit():
	text1.configure(state="normal")
	vb2.configure(state="normal")
	vb3.configure(state="normal")
	root.after(2000, normalize)
	
def normalize():
	vb2.configure(state="disabled")
	vb3.configure(state="disabled")

def save():
	s = open("Months 2018/"+l1["text"]+".txt", "w")
	text = text1.get(1.0, END)
	try:
		s.write(text.rstrip())
		s.write("\n")
	finally:
		s.close()
		current_month()

def load():
	text1.configure(state="normal")
	l2.configure(text=l1["text"]+" "+str(current_year))
	text = open("Months 2018/"+l1["text"]+".txt").read()
	text1.delete(1.0, END)
	text1.insert(END, text)
	text1.mark_set(INSERT, 1.0)
	text1.configure(state="disabled")

def check_em(button_name, new_months):
	month = datetime.datetime.now().month
	day = datetime.datetime.now().day
	button_name.configure(bg=bg1, fg=fg1, state="normal", command=lambda: text1.insert(END, "["+l1["text"]+" "+str(new_months)+"] "))
	if l1["text"] == months[month-1]:
		if new_months == day:
			button_name.configure(bg=bg3, fg=fg2)
		elif "["+l1["text"]+" "+str(new_months)+"]" in open("Months 2018/"+l1["text"]+".txt").read(): #removed +"\n"
			if new_months > day:
				button_name.configure(bg=bg2, fg=fg1) #changed from fg2 to fg1
			else: 
#				button_name.configure(bg=bg1, fg=fg1)
				button_name.configure(bg=bg1, fg="blue")
	else:
		if "["+l1["text"]+" "+str(new_months)+"]" in open("Months 2018/"+l1["text"]+".txt").read(): #removed +"\n"
			if months.index(l1["text"]) < month-1:
				button_name.configure(bg=bg1, fg="blue")
			else:
				button_name.configure(bg=bg2, fg=fg1) #changed from fg2 to fg1


def show_time():
	day = datetime.datetime.now().day
	hour = datetime.datetime.now().hour
	am_pm="AM"
	if hour > 12:
		hour-=12
		am_pm="PM"
	minute = datetime.datetime.now().minute
	second = datetime.datetime.now().second
	time_now = "{:01d}:{:02d}:{:02d}".format(hour, minute, second)
	l3.configure(text=time_now+" "+am_pm)
	time_show = root.after(100, show_time)

'''
def show_cancel():
	l2.configure(text="")
	root.after_cancel(root.after(100, show_time))
'''

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y-75))		

	
root = Tk()
root.focus_set()
root.geometry("650x400")
root.title("calendator")
#root.wm_attributes("-topmost", True)
#root.overrideredirect(1)
center(root)

top1_frame = Frame(root)
top1_frame.pack(expand=1, fill=BOTH)

#bottom1_frame = Frame(root)
#bottom1_frame.pack(expand=1, fill=BOTH)

buffer_frame = Frame(top1_frame, width=5)
buffer_frame2 = Frame(top1_frame, width=5)
buffer_frame3 = Frame(top1_frame, width=5)

buffer_frame.pack(side=LEFT, expand=0, fill=Y)

left_frame = Frame(top1_frame)
left_frame.pack(side=LEFT, expand=1, fill=BOTH)

buffer_frame2.pack(side=LEFT, expand=0, fill=Y)

right_frame = Frame(top1_frame)
right_frame.pack(side=LEFT, expan=1, fill=BOTH)

buffer_frame3.pack(side=LEFT, expand=0, fill=Y)

#l3 = Button(bottom1_frame, text="Testing...", font="Courier 12")
#l3.pack(expand=1, fill=BOTH)

buffer_frame4 = Frame(left_frame, height=5)
buffer_frame4.pack(expand=0, fill=X)

buffer_frame5 = Frame(left_frame, height=5)
buffer_frame5.pack(side=BOTTOM,expand=0, fill=X)

right_frame_top = Frame(right_frame)
right_frame_top.pack(expand=0,fill=X,side=TOP)

buffer_frame6 = Frame(right_frame_top, height=5)
buffer_frame6.pack(side=TOP,expand=0, fill=X)

l2 = Label(right_frame_top, text="January "+current_year,anchor=W,padx=0,font="Tahoma 12",height=1,pady=5)
l2.pack(expand=1, fill=X, side=LEFT)
l3 = Label(right_frame_top, text="time",anchor=E,padx=0,font="Tahoma 12")
l3.pack(expand=1, fill=X, side=LEFT)

right_frame_middle = Frame(right_frame)
right_frame_middle.pack(expand=1, fill=BOTH)

text1 = Text(right_frame_middle, height=15, width=25, wrap=WORD, bg="white") #"#FFD469" white
text1.pack(side=LEFT, expand=1, fill=BOTH)

scrolly = Scrollbar(right_frame_middle)
scrolly.pack(side=RIGHT, expand=0, fill=Y)
# scrollbar
text1.configure(yscrollcommand=scrolly.set)
scrolly.configure(command=text1.yview)


bottom1_frame2 = Frame(right_frame,height=45)
bottom1_frame2.pack(side=BOTTOM, expand=0, fill=BOTH)
bottom1_frame2.propagate(0)

vb1 = Button(bottom1_frame2, text="Edit", command=lambda: edit())
vb2 = Button(bottom1_frame2, text="Save", state="disabled", command=lambda: save())
vb3 = Button(bottom1_frame2, text="Cancel", state="disabled", command=lambda: load())

vb1.pack(side=LEFT, expand=1, fill=X)
vb2.pack(side=LEFT, expand=1, fill=X)
vb3.pack(side=LEFT, expand=1, fill=X)

jan = Frame(left_frame)
jan.pack(side=TOP, fill=X)

#buffer_frame7 = Frame(left_frame, height=5)
#buffer_frame7.pack(side=TOP,expand=0, fill=X)

frame_days = Frame(left_frame)
frame_days.pack(expand=0, fill=X)

root.bind("<Left>", replace_back)
root.bind("<Right>", replace_forward)

b1 = Button(jan, text="<", command=replace_back, width=5, bg="black", fg="white",relief=FLAT,font="Tahoma 10")
b1.pack(side=LEFT, expand=0, fill=Y)
l1 = Label(jan, text="January", font="Courier 24", bg="black", fg="white")
l1.pack(side=LEFT, expand=1, fill=X)
b2 = Button(jan, text=">", command=replace_forward, width=5, bg="black", fg="white",relief=FLAT,font="Tahoma 10")
b2.pack(side=LEFT, expand=0, fill=Y)

load()

Label(frame_days, text="Sun", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Mon", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Tue", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Wed", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Thu", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Fri", width=5).pack(side=LEFT, expand=1, fill=X)
Label(frame_days, text="Sat", width=5).pack(side=LEFT, expand=1, fill=X)

frame_weeks = []
for i in range(6):
	frame_weeks.append(Frame(left_frame))
	frame_weeks[i].pack(expand=1, fill=BOTH)
		
button_weeks = []
for i in frame_weeks:
	for x in range(7):
		button_weeks.append(Button(i))
			
for i in button_weeks:
	i.configure(text="", height=ht, width=5, anchor=NW,relief=GROOVE)
	i.pack(side=LEFT, expand=1, fill=BOTH)

def upper_check(button, new_months):
	if int(new_months) < 20:
		button.configure(bg=bg1, fg=fg1, state="normal", command=lambda: text1.insert(END, "\n["+l1["text"]+" "+str(new_months)+"] "))
		check_em(button, new_months)
	elif int(new_months) > 20:
		button.configure(bg="white", fg="black", state="disabled")

def lower_check(button, new_months):
	if int(new_months) > 20:
		button.configure(bg=bg1, fg=fg1, state="normal", command=lambda: text1.insert(END, "\n["+l1["text"]+" "+str(new_months)+"] "))
		check_em(button, new_months)
	elif int(new_months) < 20:
		button.configure(bg="white", fg="black", state="disabled")

def month_now():		
	month = datetime.datetime.now().month
	day = datetime.datetime.now().day
	
	l1.configure(text=months[month-1])
	
	change_month(calendar[l1["text"]])
	load()
		
def current_month():
	change_month(calendar[l1["text"]])
	load()
	
def change_month(new_months):
	jan.focus_set()
	month = str(new_months)
	
	for i in range(7):
		button_weeks[i].configure(text=new_months[i], bg=bg1, fg=fg1, command=lambda: text1.insert(END, "\n["+l1["text"]+"] "+str(new_months[i])+"]"),font="Tahoma 12")
		upper_check(button_weeks[i], new_months[i])
	
	for i in range(21):
		button_weeks[i+7].configure(text=new_months[i+7], bg=bg1, fg=fg1, command=lambda: text1.insert(END, "\n["+l1["text"]+"] "+str(new_months[i+7])+"]"),font="Tahoma 12")
		check_em(button_weeks[i+7], new_months[i+7])
	
	for i in range(14):
		button_weeks[i+28].configure(text=new_months[i+28], bg=bg1, fg=fg1, command=lambda: text1.insert(END, "\n["+l1["text"]+"] "+str(new_months[i+28])+"]"),font="Tahoma 12")
		lower_check(button_weeks[i+28], new_months[i+28])

show_time()	
month_now()	
root.mainloop() 