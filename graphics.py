from tkinter import Tk, BOTH, Canvas, Button,Frame, Label,StringVar,OptionMenu

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
        self.create_option_menu()
        self.__grid_frame = Frame(self.__root)
        self.__grid_frame.place(x=20,y =80)
        S_grid(self,7,6)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def create_btns(self,on_click,r,c):
        cell_frame = Frame(self.__grid_frame, width=100, height=60)
        cell_frame.grid(row=r,column=c,padx=2,pady=2)
        cell_frame.grid_propagate(False)

        btn1 = Button(cell_frame,text="", width=8,height=2,
                             command=lambda r=r, c=c:on_click(r,c,0,self.sel_option.get()))
        btn2 = Button(cell_frame,text="", width=8,height=2,
                             command=lambda r=r, c=c:on_click(r,c,1,self.sel_option.get()))
        btn1.pack(side="top",expand=True)
        btn2.pack(side="bottom",expand=True)
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
    def __init__(self,win, rows, cols):
        self.btns = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(win.create_btns(self.on_click,r,c))
            self.btns.append(row)
            win.create_label(DAYS[r],r)
            

        

        