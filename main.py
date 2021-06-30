import tkinter as tk
import serial

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x200')
        self.title('Mission Control')
        first_label = tk.Label(self,text="Odor blender",font=10)
        first_label.pack(pady=2,padx=2)
 
    def design(self):
        startbtn = tk.Button(self, text="START", width=25, command=self.start)
        measbtn = tk.Button(self, text="MEASURE", width=25, command=self.meas)
        quitbtn = tk.Button(self, text="QUIT", width=25, command=self.quit)
        startbtn.pack()
        measbtn.pack()
        quitbtn.pack()

    def start(self):
        print("blender test")
   
    def meas(self):
        print("measurement start")

    def quit(self):
        print("quit")
        self.destroy()

    def write(self):
        with serial.Serial() as ser:
            ser.baudrate = 9600
            ser.port = 'COM4'
            ser.open()
            try:
                ser.write(b'')
            except Exception as e:
                print(e)
        ser.close()

    def run(self):
        self.design()
        self.mainloop()


if __name__=="__main__":
    print("+++ gui started")
    app = Application()
    app.run()