import tkinter as tk
from tkinter import *
from anti_virus_03_08_25 import *
# With thead we can use several windows(threads) at the same time
import threading
from tkinter import scrolledtext
from tkinter import filedialog
# to see all discs from the drive
import psutil


BASIC_IMG ="./imgForAntiVirus03/GUI - BG.png"
SCAN_BUTTON ="./imgForAntiVirus03/GUI - button.png"

FONT = "Monaco"
font = (FONT, 18, "bold")

class AntiVirusGui(AntiVirus):

    def __init__(self):

        # the function "super()" - he takes the elements from the parent(original) class and use them
        super().__init__()

        # The main window of a program.
        self._root = None

        # A space in the window where we can create artwork
        self._canvas = None

        # The xreation of BASIC_IMG, SCAN_BUTTON
        self._img_basic = None
        self._img_scan_btn = None

        # creating of two buttons
        self._btn_scan = None
        self._btn_stop_scaning = None

        self._scaning_running = False
        self.scan_thread = None

        # the empty box of scrolled text
        self.scroll_bar = None

        # the label for the folder
        self.folder_label =None
        #the entry of the folder 
        self.folder_entry = None
        # button to select folder
        self.slc_folder_btn = None
        # list of files
        self.exclude_folders = []

        # creating Gui components(buttons, labels etc)
        self.create_ui()


    def create_ui(self):

        self._root = tk.Tk()
        self._root.title("Anti Virus")

        # basic img
        self._img_basic = PhotoImage(file=BASIC_IMG)
        img_width = self._img_basic.width()
        img_height = self._img_basic.height()

        # the size of the window(img)
        self._root.geometry(f'{img_width}x{img_height}')
        self._root.resizable(False,False)

        # canvas creation
        self._canvas = tk.Canvas(self._root)
        self._canvas.config(width=img_width,height=img_height)
        self._canvas.pack(fill='both',expand=True)
        self._canvas.create_image(0,0,anchor="nw",image=self._img_basic)
        self._canvas.create_text(90,80,text='Anti Virus',font=('Calibri',28),fill='#808080')

        # img button
        self._img_btn = PhotoImage(file=SCAN_BUTTON)
        img_btn_w = self._img_btn.width()
        img_btn_h = self._img_btn.height()

        # img folder btn
        self.slc_folder_btn = PhotoImage(file=SCAN_BUTTON)
        img_btn_w = self.slc_folder_btn.width()
        img_btn_h = self.slc_folder_btn.height()

        # button - "escl_folder_btn"
        self.slc_folder_btn = tk.Button(self._canvas, text="Browse", font=('Calibri', 12), fg="#000000", bg="#C0C0C0", command=self.exclude_folder_from_brw)
        self.slc_folder_btn.place(x=650, y=250)

        # entry box
        self.folder_entry = tk.Entry(self._canvas, font=('Calibri',16), fg='black', width=30)
        self.folder_entry.place(x=50, y=170)

        #
        self.folder_label = tk.Label(self._canvas, text="Exclude folder:")
        self.folder_label.place(x=20, y=180)

        # button "scan"
        self._btn_scan = tk.Button(self._canvas,text="Scan",font=font,fg="#c0c0c0",compound="center",
                                    width=img_btn_w,height=img_btn_h,image=self._img_btn,bd=0,
                                    command=self.on_click_scan)
        self._btn_scan.place(x=650,y=50)

        # button "Stop" - _btn_stop_scaning
        self._btn_stop_scaning = tk.Button(self._canvas,text="Stop scaning",font=font,fg="#c0c0c0",compound="center",
                                        width=img_btn_w,height=img_btn_h,image=self._img_btn,bd=0,
                                        command=self.on_click_stop_scaning,state="disabled")
        self._btn_stop_scaning.place(x=650,y=130) 

        # scrolled bar - self.scroll_bar
        self.scroll_bar = scrolledtext.ScrolledText(self._root,font=font,fg="#c0c0c0", width=40, height=10, state="disabled")
        self.scroll_bar.place(x=20,y=140) 
        # self.append_text("This is some more text.")

    # Function that allows to select folder from the browser
    def exclude_folder_from_brw(self):

        exclude_folder = filedialog.askdirectory()
        if exclude_folder:
            # self.folder_entry.delete(0, tk.END)
            # self.folder_entry.insert(tk.END, exclude_folder)
            self.exclude_folders.append(exclude_folder)
            self.append_text(f"Excluded folder: {exclude_folder}")
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(tk.END, ', '.join(self.exclude_folders))

    # For the scrolle bar
    def append_text(self, text):

        self.scroll_bar.config(state="normal")
        self.scroll_bar.insert(tk.END, text + "\n")
        self.scroll_bar.see(tk.END)  # Scroll to the end
        self.scroll_bar.yview_moveto(2.0)
        self.scroll_bar.config(state="disabled")
           
    def on_click_scan(self):

        self._btn_scan.config(state="disabled")
        self._btn_stop_scaning.config(state="normal")
        self.scan_running = True
        # thread that the anti virus window after the click on the "scan" button will run at the same time while the program will run
        self.scan_thread = threading.Thread(target=self.start_scaning)
        self.scan_thread.start()

    def start_scaning(self):

        # directory = "C://Users//nastk//chat"
        drives = psutil.disk_partitions()
        for drive in drives:
            self.append_text(f"Drive: {drive.device}")

        self.iterate_files(drive.device, self.append_text, self.exclude_folders) 

    # def scan_loop(self):
    #     while self._scaning_running:
    #         print("Scanning is running")
    #         time.sleep(2)

    def on_click_stop_scaning(self):

        # self._entry_IP.config(state="normal")
        # self._entry_Port.config(state="normal")

        self._btn_scan.config(state="normal")
        self._btn_stop_scaning.config(state="disabled")

        self.stop_scaning()

    def stop_scaning(self):
        pass

    def run(self):
        self._root.mainloop()

if __name__ == "__main__":
    server = AntiVirusGui()
    server.run()



    


