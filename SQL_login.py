import tkinter
import tkinter.messagebox
class SQL:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #configure the window
        self.main_window.title('SQL Server Login')
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.email_label = tkinter.Label(self.top_frame, text="Login:")
        self.email_label.pack(side='left')
        self.email = tkinter.Entry(self.top_frame)
        self.email.pack(side='right')


        self.password_label = tkinter.Label(self.mid_frame, text='Password:')
        self.password_label.pack(side='left')
        self.password = tkinter.Entry(self.mid_frame,show="*") 
        self.password.pack(side='right')

        self.login_button = tkinter.Button(self.bottom_frame, text='Login',command=self.access_database)
        self.login_button.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def access_database(self):
        tkinter.messagebox.showinfo('SQL Server Login', 'You have successfully logged in')


myinstance = SQL()
