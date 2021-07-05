import tkinter as tk
from tkinter.constants import COMMAND
import serial
import threading
import time


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x200')
        self.title('Mission Control')
        first_label = tk.Label(self,text="Odor blender",font=10)
        first_label.pack(pady=2,padx=2)
        self.threads = []
 
    def design(self):
        self.setbtn = tk.Button(self, text="COM SET", width=25, command=self.comset)
        self.startbtn = tk.Button(self, text="START", width=25, command=self.start)
        self.stopbtn = tk.Button(self, text="STOP", width=25, command=self.stop)
        self.quitbtn = tk.Button(self, text="QUIT", width=25, command=self.quit)
        self.console = tk.Label(self, text="")
        self.comtxt = tk.Text(self, height=1, width=10)
        self.comtxt.pack()
        self.setbtn.pack()
        self.startbtn.pack()
        self.stopbtn.pack()
        self.quitbtn.pack()
        self.console.pack()

    def comset(self):
        print("com port set to (%s)" % self.comtxt.get(1.0,"end-1c"))
        self.setbtn.config(bg="lawn green")
        self.console.config(text="com port set")
        
   
    def start(self):
        print("blender start")
        self.meas_thread = threading.Thread(target=self.meas_proc,args=())
        self.threads.append(self.meas_thread)
        self.meas_thread.start()

    def stop(self):
        print("blender stop")
        with serial.Serial() as ser:
            ser.baudrate = 115200
            ser.port = 'COM4'
            ser.open()
            try:
                cmd = "pwm\n0 0 0 0 0 0 0 0 0\n"
                ser.write(cmd.encode('ascii'))
                self.console.config(text="blender stop")
            except Exception as e:
                print(e)
        ser.close()


    def quit(self):
        print("quit")
        self.destroy()

    def write(self):
        print("blender start")
        with serial.Serial() as ser:
            ser.baudrate = 115200
            ser.port = 'COM4'
            ser.open()
            try:
                cmd = "pwm\n0 0 0 0 0 0 0 0 0\n"
                ser.write(cmd.encode('ascii'))
                self.console.config(text="blender start")
            except Exception as e:
                print(e)
        ser.close()

    def run(self):
        self.design()
        self.mainloop()

    def meas_proc(self):
        print("process done")


if __name__=="__main__":
    print("+++ gui started")
    app = Application()
    app.run()