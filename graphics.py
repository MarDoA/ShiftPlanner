from tkinter import Tk, BOTH, Canvas, Button,Frame, Label,StringVar,OptionMenu,ttk
from datetime import datetime
import calendar

DAYS = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
PEOPLE = ["ma","bo","gege"]

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Planner")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.sel_option = StringVar(self.__root)
        self.sel_option.set(PEOPLE[0])
        self.date = datetime.today()
        self.sel_month = StringVar(value=calendar.month_abbr[self.date.month])
        self.sel_year = StringVar(value=self.date.year)
        self.create_option_menu()
        self.create_datepicker()
        self.__grid_frame = Frame(self.__root)
        self.__grid_frame.place(x=20,y =80)
        S_grid(self,7,6)
        self.overlay_labels = []

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def create_datepicker(self):
        years = [str(y) for y in range(self.date.year -10, self.date.year +10)]
        months = calendar.month_abbr[1:]
        date_frame = Frame(self.__root)
        date_frame.place(x=20,y=40)
        year_spin = ttk.Spinbox(date_frame, values=years,textvariable=self.sel_year,width=4)
        month_spin = ttk.Spinbox(date_frame,values=months,textvariable=self.sel_month,width=3,wrap=True)
        print(self.sel_month)
        month_spin.pack(side="left",padx=5)
        year_spin.pack(side="right",padx=5)

    def create_btns(self,on_click,r,c):
        cell_frame = Frame(self.__grid_frame, width=100, height=60,highlightbackground="black",highlightthickness=1)
        cell_frame.grid(row=r,column=c,padx=2,pady=2)
        cell_frame.grid_propagate(False)

        btn1 = Button(cell_frame,text="", width=8,height=2,
                             command=lambda r=r, c=c:on_click(r,c,0,self.sel_option.get()))
        btn2 = Button(cell_frame,text="", width=8,height=2,
                             command=lambda r=r, c=c:on_click(r,c,1,self.sel_option.get()))
        btn1.pack(side="top",expand=True)
        btn2.pack(side="bottom",expand=True)
        lab = Label(cell_frame,text="",width=1,height=1)
        lab.place(x=2,y=2)
        return (btn1,btn2)
    
    def create_label(self,txt,row):
        day = Label(self.__grid_frame,text=txt,width=10)
        day.grid(row=row,column=6,padx=2,pady=2)

    def create_option_menu(self):
        dp_menu = OptionMenu(self.__root,self.sel_option,*PEOPLE)
        self.__canvas.create_window(900,50,window=dp_menu)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
    

class S_grid:
    def on_click(self,row, col,bn,txt):
        current = self.btns[row][col][bn]["text"]
        self.btns[row][col][bn]["text"] = txt if current == "" else ""
        print(row)
        print(col)
    def __init__(self,win, rows, cols):
        self.btns = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(win.create_btns(self.on_click,r,c))
            self.btns.append(row)
            win.create_label(DAYS[r],r)
            

        

        