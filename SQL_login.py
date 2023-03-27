import tkinter
import tkinter.messagebox
import pyodbc
class SQL:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #configure the window
        self.main_window.title('SQL Server Login')
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.username_label = tkinter.Label(self.top_frame, text="Login:")
        self.username_label.pack(side='left')
        self.username = tkinter.Entry(self.top_frame)
        self.username.pack(side='right')


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
        login = self.username.get()
        pw = self.password.get()
        self.main_window.destroy()
        login='tanner_dougherty1'
        pw = 'MIS4322student'

        prelist={}
        cn_str=('Driver={SQL Server};''Server=MIS-SQLJB;''Database=School;''UID='+login+';''PWD='+pw+';')

        cn = pyodbc.connect(cn_str)
        cursor=cn.cursor()
        cursor.execute ('select name, budget from School.dbo.Department')
        data = cursor.fetchall()
        ##print(data)
        print(format('Dept Name', '25s'),format('Original Budget','20s'),format('New Budget','15s'), 'Increase')
        for row in data:
            name = row[1]
            budget = row[2]
            increase = budget*.1
            new_budget = budget+increase
            print(f'{name:25.2f}',f'${budget:20.2d}',f'${new_budget:15.2d}',f'${increase:.2d}')


'''courseid = str(input('Course ID: '))
courseList=[('1045','Calculus',4,7),('1050','Chemistry',4,1)]
for row in courseList:
    courseID = row[0]
    title = row[1]
    credit = row[2]
    departmentID=row[3]
    if courseID == courseid:
        print(f'Title: {title}',f'Credits:{credit}',f'DeptID:{departmentID}')
'''
            



myinstance = SQL()
