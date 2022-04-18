from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox 
from tkinter.filedialog import askopenfilename
import threading
import os
from module import twitter
import time
class VMX:
    def __init__(self):
        test =  os.popen('vmrun list').read()

        self.window = Tk()

        self.window.title("TOOL AUTO VMX")

        self.window.geometry('1000x400')

        lbl = Label(self.window, text="DESIGN BY DEVELOPER TÀI NGUYỄN", font=("Arial Bold", 20), width=55, pady=10, bg="black" , fg="white",borderwidth=2, relief="raised")

        lh = Label(self.window, text="NHẬN CODE TOOL & THIẾT KẾ WEBSITE THEO YÊU CẦU - ZALO/SDT 0387865006", font=("Arial Bold", 12), width=93,pady=1 , fg="red",borderwidth=2, relief="raised")

        lbl.pack(fill=X)

        lh.pack(fill=X)

        fame1 = Frame(self.window)

        fame1.pack(fill=BOTH,side=BOTTOM)

        fame2 = Frame(self.window)

        fame2.pack(fill=BOTH,side=TOP)

        lbl1 = Label(fame2, text= 'Tg check list : ', font=("Arial", 11))

        lbl1.grid(column=0,row=0,padx=5,pady=5)

        sp1 = Spinbox(fame2,from_=1, to=999,width=3)

        sp1.grid(column=1,row=0,padx=5,pady=5,sticky='w')

        lbl2 = Label(fame2, text= 'vmw tối đa : ', font=("Arial", 11))

        lbl2.grid(column=2,row=0,padx=5,pady=5)

        sp2 = Spinbox(fame2,from_=1, to=999,width=3)

        sp2.grid(column=3,row=0,padx=5,pady=5,sticky='w')

        lbl3 = Label(fame2, text= 'Tg chờ mở vmw : ', font=("Arial", 11))

        lbl3.grid(column=4,row=0,padx=5,pady=5)

        sp3 = Spinbox(fame2,from_=1, to=999,width=3)

        sp3.grid(column=5,row=0,padx=5,pady=5,sticky='w')

        lbl4 = Label(fame2, text= 'numvcpus : ', font=("Arial", 11))

        lbl4.grid(column=6,row=0,padx=5,pady=5)

        sp4 = Entry(fame2,width=5)

        sp4.grid(column=7,row=0,padx=5,pady=5,sticky='w')

        lbl5 = Label(fame2, text= 'c.cPS : ', font=("Arial", 11))

        lbl5.grid(column=8,row=0,padx=5,pady=5)

        sp5 = Entry(fame2,width=5)

        sp5.grid(column=9,row=0,padx=5,pady=5,sticky='w')

        lbl6 = Label(fame2, text= 'memsize : ', font=("Arial", 11))

        lbl6.grid(column=10,row=0,padx=5,pady=5)

        sp6 = Entry(fame2,width=5)

        sp6.grid(column=11,row=0,padx=5,pady=5,sticky='w')

        i = IntVar()

        cb1= Checkbutton(fame2, text = "Loop", variable=i)

        cb1.grid(column=12,row=0,padx=5,pady=5,sticky='w')

        def callback3():
            self.name3 = filedialog.askopenfilename() 
            self.txt1.insert(INSERT,"Đã nhận đường dẫn file website :       " + self.name3 + '\n')
            self.file3 = twitter.xulyfile(self.name3)

        def callback2():
            self.name2 = filedialog.askopenfilename() 
            self.txt1.insert(INSERT,"Đã nhận đường dẫn file profile :       " + self.name2 + '\n')
            self.file2 = twitter.xulyfile(self.name2)

        def callback():
            self.name = filedialog.askopenfilename() 
            self.txt1.insert(INSERT,"Đã nhận đường dẫn file proxy :       " + self.name + '\n')
            self.file = twitter.xulyfile(self.name)
        def NEXT():
            self.top = True
        def START():
                file1 = twitter.xulyfile('data.txt')
                thoigian = sp1.get()
                cho = sp3.get()
                vmxmax = sp2.get()
                loop = i.get()
                numvcpus = sp4.get()
                coresPerSocket = sp5.get()
                memsize = sp6.get()
                self.window.update()
                threadings = threading.Thread(target=self.run_cmd, args=(file1,thoigian,vmxmax,loop,cho,numvcpus,coresPerSocket,memsize))
                threadings.start()
                time.sleep(1)
                    # except:
                    #     self.txt1.insert(INSERT,"Hệ thống lỗi - liên hệ thằng ở trên để fix :)\n")
                    #     self.window.update()
        # Button(fame2,text='Click to Open File', command=callback).grid(column=1,row=0,padx=5,pady=5)

        # Button(fame2,text='Click to Open File',command=callback2).grid(column=1,row=1,padx=5,pady=5)

        # Button(fame2,text='Click to Open File',command=callback3).grid(column=1,row=2,padx=5,pady=5)

        Button(fame2,text='START',command=START).grid(column=13,row=0,padx=10,pady=10)

        self.tv = ttk.Treeview(
            fame1, 
            columns=(1, 2, 3),takefocus='None',show='headings',selectmode='browse',height=12
            )

        sb = Scrollbar(fame1, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tv.config(yscrollcommand=sb.set)
        sb.config(command=self.tv.yview)

        self.tv.pack(fill=X,pady=5,padx=5)
        self.tv.column("#1",anchor=CENTER, stretch=NO,width=70)
        self.tv.column("#2",anchor=CENTER, stretch=NO,width=700)
        self.tv.column("#3",anchor=CENTER, stretch=NO,width=0)
        self.tv.heading('#1', text='STT')
        self.tv.heading('#2', text=' Link virtual machines running ')
        self.tv.heading('#3', text='')

        self.window.mainloop()        
    def run_cmd(self,file,thoigian,vmxmax,loop,cho,numvcpus,coresPerSocket,memsize):
        self.vitri = int(vmxmax) - 1
        def suafilevmx(link):
            with open(link,'r') as file:
                dulieu = file.read()
            if dulieu.find('numvcpus') != -1:
                tim_numvcpus = dulieu[dulieu.find('numvcpus'):dulieu.find('numvcpus') + 14]
                dulieu = dulieu.replace(tim_numvcpus,'numvcpus = "' + numvcpus + '"')
            if dulieu.find('cpuid.coresPerSocket') != -1:
                tim_coresPerSocket = dulieu[dulieu.find('cpuid.coresPerSocket'):dulieu.find('cpuid.coresPerSocket') + 26]
                dulieu = dulieu.replace(tim_coresPerSocket,'cpuid.coresPerSocket = "' + coresPerSocket + '"')
            if dulieu.find('memsize') != -1:
                tim_memsize = dulieu[dulieu.find('memsize'):dulieu.find('memsize') + 16]
                dulieu = dulieu.replace(tim_memsize,'memsize = "' + memsize + '"')
            with open(link,'w') as refile:
                refile.write(dulieu)
        def get_list():
            test =  os.popen('vmrun list').read()
            listdata1 = []
            while test.find('\n') != -1:
                listdata1.append(test[:test.find('\n')])
                test = test[test.find('\n') + 1:]
            if len(self.tv.get_children()) > 0:
                for i in self.tv.get_children():
                    self.tv.delete(i)
            for p in range(0,len(listdata1)):
                self.tv.insert(parent='', index=p, iid=p, values=(p, listdata1[p], ""))
            print(len(listdata1))
            if len(listdata1) != 0:
                if (len(listdata1) - 1) < int(vmxmax):
                    for a in range(0,int(vmxmax) - len(listdata1) + 1):
                        suafilevmx(file[self.vitri + 1])
                        os.system('vmrun start "' + file[self.vitri + 1] + '"')
                        self.vitri += 1
                        time.sleep(int(cho))
                    test =  os.popen('vmrun list').read()
                    listdata1 = []
                    while test.find('\n') != -1:
                        listdata1.append(test[:test.find('\n')])
                        test = test[test.find('\n') + 1:]
                    if len(self.tv.get_children()) > 0:
                        for i in self.tv.get_children():
                            self.tv.delete(i)
                    for p in range(0,len(listdata1)):
                        self.tv.insert(parent='', index=p, iid=p, values=(p, listdata1[p], ""))
            self.window.update()
        def auto():
            closec = 0
            while closec == 0:
                for v in range(0,int(vmxmax)):
                    suafilevmx(file[v])
                    os.system('vmrun start "' + file[v] + '"')
                    time.sleep(int(cho))
                thoigiancho = 0
                get_list()
                huy = True
                while huy == True:
                    if thoigiancho == int(thoigian):
                        get_list()
                        thoigiancho = 0
                    time.sleep(1)
                    thoigiancho += 1
                    if self.vitri == len(file) - 1:
                        huy = False
                if loop == 0:
                    closec = 1
        auto()
VMX()
