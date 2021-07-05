import tkinter as tk
from tkinter.constants import COMMAND
import serial
import threading
import time


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x250')
        self.title('Mission Control')
        first_label = tk.Label(self,text="Odor blender",font=10)
        first_label.pack(pady=2,padx=2)
        self.threads = []
 
    def design(self):
        self.setbtn = tk.Button(self, text="COM SET", width=25, command=self.comset)
        self.startbtn = tk.Button(self, text="START", width=25, command=self.start)
        self.autobtn = tk.Button(self, text="AUTO", width=25, command=self.auto)
        self.stopbtn = tk.Button(self, text="STOP", width=25, command=self.stop)
        self.quitbtn = tk.Button(self, text="QUIT", width=25, command=self.quit)
        self.console = tk.Label(self, text="")
        self.comtxt = tk.Text(self, height=1, width=10)
        self.timetxt = tk.Text(self, height=1, width=10)

        self.comtxt.pack()
        self.setbtn.pack()
        self.startbtn.pack()
        self.timetxt.pack()
        self.autobtn.pack()
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
        self.meas_thread.start()

    def auto(self):
        duration = self.timetxt.get(1.0,"end-1c")
        self.autobtn.config(bg="lawn green")
        
        self.console.config(text="duration set to %s sec" % duration)
        valves = [0,0,0,0,0,0,0,0]
        for i in range(0,8):
            cmd = "pwm\n"
            for j in range(0,len(valves)):
                cmd = cmd + " " + str(valves[i])
            cmd = cmd + " 0\n"
            self.write(cmd)
            # print(str(cmd))
            valves[i] = 50
            print(valves)
            time.sleep(duration)

    def write(self,cmd):
        with serial.Serial() as ser:
            ser.baudrate = 115200
            ser.port = 'COM4'
            ser.open()
            try:
                ser.write(cmd.encode('ascii'))
                self.console.config(text="blender start")
            except Exception as e:
                print(e)
        ser.close()

            
    
    def stop(self):
        print("blender stop")
        self.quit_thread = threading.Thread(target=self.quit_proc,args=())
        self.quit_thread.start()

    def write_all(self):
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
    
    def quit_all(self):
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

    def run(self):
        self.design()
        self.mainloop()

    def meas_proc(self):
        self.write_all()
    
    def quit_proc(self):
        self.quit_all()


if __name__=="__main__":
    print("+++ gui started")
    app = Application()
    app.run()