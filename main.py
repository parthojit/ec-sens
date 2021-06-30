import tkinter as tk
import serial
import threading
import time

# % make command
# % Command is a text chain formatted in the following way
# % "pwd\nxxx\nxxx\nxxx\nxxx\nxxx\nxxx\nxxx\nxxx0\n"
# % where xxx is the percentage on each valve
# % the end 0 marks the end of the data stream
# % The FPGA need this formating

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x200')
        self.title('Mission Control')
        first_label = tk.Label(self,text="Odor blender",font=10)
        first_label.pack(pady=2,padx=2)
        self.threads = []
 
    def design(self):
        testbtn = tk.Button(self, text="TEST", width=25, command=self.test)
        startbtn = tk.Button(self, text="START", width=25, command=self.start)
        stopbtn = tk.Button(self, text="STOP", width=25, command=self.stop)
        quitbtn = tk.Button(self, text="QUIT", width=25, command=self.quit)
        testbtn.pack()
        startbtn.pack()
        stopbtn.pack()
        quitbtn.pack()

    def test(self):
        print("blender test")
   
    def start(self):
        print("blender start")
        self.meas_thread = threading.Thread(target=self.meas_proc,args=())
        self.threads.append(self.meas_thread)
        self.meas_thread.start()

    def stop(self):
        print("blender stop")
        for thread in self.threads:
            thread.join()

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

    def meas_proc(self):
        print("process done")


if __name__=="__main__":
    print("+++ gui started")
    app = Application()
    app.run()