import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import os
import matplotlib.pyplot as plt
import numpy as np

class Match:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cricket Metrics ")
        self.window.geometry("800x800")
        self.label = tk.Label(self.window, text="Cricket Metrics",font=("Helvetica", 30   ,"bold"))
        self.label.pack(pady=50)
                
        self.itemset = [0]
        self.wiket_count = []
        self.real_data_for_ball = []
        self.real_data_for_other_ball = []
        self.real_data_display = [] 
        self.text_to_save = []
        self.total_runs = []
        self.run = 0
        self.team1_runs = 0
        self.team2_runs = 0
        self.counting = []

        self.chasing_runs = 0
        self.run_list = []

        self.label2 = tk.Label(self.window, text="Team 1 name : ",font=("Helvetica", 10 ,"bold"))
        self.label3 = tk.Label(self.window, text="Team 2 name : ",font=("Helvetica", 10 ,"bold"))
        self.text_box1 = tk.Entry(self.window)
        self.text_box2 = tk.Entry(self.window)
        self.button_s = tk.Button(self.window, text="Done", command=self.creat,font=(50))

        self.label1 = tk.Label(self.window, text="Over : ",font=("Helvetica", 10 ,"bold"))
        self.selection_values = ["5","10", "20", "50"]
        self.selected_value = tk.StringVar()
        self.selected_value.set(self.selection_values[0])  # Set default selection
        self.dropdown = ttk.Combobox(self.window, textvariable=self.selected_value, values=self.selection_values)
        
        self.label_toss = tk.Label(self.window, text="Toss : ",font=("Helvetica", 10 ,"bold"))
        self.selection_values_toss = ["Heads", "Tails"]
        self.selected_value_toss = tk.StringVar()
        self.selected_value_toss.set(self.selection_values_toss[0])  # Set default selection
        self.dropdown_toss = ttk.Combobox(self.window, textvariable =self.selected_value_toss, values=self.selection_values_toss)

        self.label1.place(x=250, y=250)
        self.label2.place(x=250, y=300)
        self.label3.place(x=250, y=350)
        self.dropdown.place(x=330, y=250)
        self.text_box1.place(x=360, y=303)
        self.text_box2.place(x=360, y=353)
        self.label_toss.place(x=250,y=400)
        self.dropdown_toss.place(x=330 , y=401) 
        self.button_s.place(x=360,y=500)

        self.window.mainloop()

    def creat(self):
        self.team_1 = self.text_box1.get()
        self.team_2 = self.text_box2.get()
        self.over = self.dropdown.get()
        
        if not self.team_1 or not self.team_2 :
            messagebox.showerror("Error", "Please enter team name in the text box.")
            
        elif self.team_1 ==" " or self.team_2 ==" ":
            messagebox.showerror("Error", "Please enter team name in the text box.")
        elif self.team_1 == self.team_2:
            messagebox.showerror("Error", "Please enter Both team name DIFFERENT in the text box.")
        else:
            self.window.destroy() 
            list1 = [1,2]
            self.toss = random.choices(list1)
            self.create_new_window_for_toss_and_csv_file_create(self.team_1,self.team_2,self.over,self.toss)

    def create_new_window_for_toss_and_csv_file_create(self,team1,team2,over,toss):
            
            self.toss_win = ""
            self.team1 =  team1.upper()
            self.team2 =  team2.upper()
            self.over =  over
            self.new_window = tk.Tk()
            self.new_window.title("Cricket Metrics")
            self.new_window.geometry("700x700")
            self.label = tk.Label(self.new_window,text="Cricket Toss",font=("Helvetica", 30   ,"bold"))
            self.label.pack(pady=20)

            if int(toss[0]) == 1:
                self.label_team = tk.Label(self.new_window, text=f"{self.team1} Won The Toss",font=("Helvetica", 40 ,"bold"),fg="green")
                self.toss_win = self.team1
                self.label_team.pack(pady=50)
            if int(toss[0]) == 2:
                self.label_team = tk.Label(self.new_window, text=f"{self.team2} Won The Toss",font=("Helvetica", 40 ,"bold"),fg="green")
                self.label_team.pack(pady=50)
                self.toss_win = self.team2

            list1 = {}
            list2 = []
            for i in range(1,11):
                if i <=11:
                    if i == 1:
                        for j in range(1,int(self.over)+1):
                            list2.append(j)      
                        list1.update({"Overs":list2})
                    
                    elif i < 8 :
                        list1.update({f"{i-1}":""})
                    else:
                        list1.update({"Wide Ball Runs":""})
                        list1.update({"Total":""})
                        break        
            df = pd.DataFrame(list1)

            self.path = f'./{self.team1} vs {self.team2}'
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            self.file_path1 = f"{self.team1} vs {self.team2}/{self.team1}.csv"
            self.file_path2 = f"{self.team1} vs {self.team2}/{self.team2}.csv"
            df.to_csv(f"{self.file_path1}",index=False)
            df.to_csv(f"{self.file_path2}",index=False)

            self.df1 = pd.read_csv(f"{self.file_path1}")
            self.df2 = pd.read_csv(f"{self.file_path2}")

            self.button_bat = tk.Button(self.new_window, text="Bat 🏏", command=lambda i=1 :self.destroy_windos(i),font=("Arial", 20, "bold"),width=10,height=1)
            self.button_ball = tk.Button(self.new_window, text="Ball ⚽", command=lambda i=0 :self.destroy_windos(i),font=("Arial", 20, "bold"),width=10,height=1)
            self.button_bat.place(x=150,y=280) 
            self.button_ball.place(x=360,y=280)
            self.new_window.mainloop()
    
    def destroy_windos(self,i):
        self.new_window.destroy()
        self.new_window_for_bat(i)

    def new_window_for_bat(self,j):

            self.batting_team_name = ""
            self.batting_team_name = self.toss_win

            
            if len(self.counting)!= 2 :
                self.wiket_count.clear()
                if j==1:
                    self.root = tk.Tk()
                    self.root.geometry("800x700")
                    self.root.state('zoomed')
                    self.root.title("Cricket Metrics Dasbored")
                    self.counting.append(1)
                    
                if j==0:
                    if self.toss_win != self.team1:
                        self.batting_team_name = self.team1
                    
                    if self.toss_win != self.team2:
                        self.batting_team_name = self.team2
                    
                    self.counting.append(1)
                    self.root = tk.Tk()
                    self.root.geometry("800x700")
                    self.root.state('zoomed')
                    self.root.title("Cricket Metrics Dasbored")
            
                self.label_text , self.over_count_text ,self.wiket_count_text ,self.temp_text,self.chasing = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()

                if len(self.counting) == 2:
                     self.chasing.set(' '.join(f"Target: {int(self.chasing_runs)}"))
                else:
                     self.chasing.set(' '.join("First Batting!"))                

                self.label = tk.Label(self.root,text=f"{self.batting_team_name} Bating 🏏",font=("Helvetica", 30 ,"bold"),fg="Purple")
                self.label.pack(pady=20)

                self.run_pannel = tk.Label(self.root, textvariable=self.chasing, font=("Calibri", 35,'bold'))
                self.run_pannel.pack(ipady=50)

                self.total_over = tk.Label(self.root, text=f"{self.over} Over Match!", font=("Calibri", 18))
                self.total_over.pack(pady=0)

                self.temp_text.set("Runs: 0")

                self.total_runs_text = tk.Label(self.root, textvariable=self.temp_text, font=("Segoe UI Black", 18),fg='blue')
                self.total_runs_text.pack(pady=0)

                self.over_count_text.set("Over : 0")
                self.over_count = tk.Label(self.root, textvariable = self.over_count_text, font=("Arial", 20,"bold"))
                self.over_count.pack(pady=2)

                self.wiket_count_text.set("Wiket : 0")

                self.label_wiket_count = tk.Label(self.root, textvariable = self.wiket_count_text, font=("Arial", 20,"bold"))
                self.label_wiket_count.pack(pady=0)

                self.label = tk.Label(self.root,textvariable=self.label_text, font=("Impact", 26,'bold'))
                self.label.pack(pady=50)


                self.button_frame = tk.Frame(self.root)
                self.button_frame.pack()

                self.button_frame_main = tk.Frame(self.root)
                self.button_frame_main.pack()

                # Create number buttons

                button_run_1 = tk.Button(self.button_frame, text=str(1), width=5, height=2, command=lambda i=1: self.add_digit(i))
                button_run_1.grid(row=0, column=0, padx=5, pady=5)

                button_run_2 = tk.Button(self.button_frame, text=str(2), width=5, height=2, command=lambda i=2: self.add_digit(i))
                button_run_2.grid(row=0, column=1, padx=5, pady=5)

                button_run_3 = tk.Button(self.button_frame, text=str(3), width=5, height=2, command=lambda i=3: self.add_digit(i))
                button_run_3.grid(row=0, column=2, padx=5, pady=5)

                button_run_4 = tk.Button(self.button_frame, text=str(4), width=5, height=2, command=lambda i=4: self.add_digit(i))
                button_run_4.grid(row=0, column=3, padx=5, pady=5)

                button_run_6 = tk.Button(self.button_frame, text=str(6), width=5, height=2, command=lambda i=6: self.add_digit(i))
                button_run_6.grid(row=0, column=4, padx=5, pady=5)

                button_wide_ball = tk.Button(self.button_frame, text='WB', width=5, height=2, command=lambda i='WB': self.add_digit(i))
                button_wide_ball.grid(row=0, column=6, padx=5, pady=5)

                button_dot_ball = tk.Button(self.button_frame, text='⚫', width=5, height=2, command=lambda i=0: self.add_digit(i))
                button_dot_ball.grid(row=0, column=7, padx=5, pady=5)

                button_Bounce_ball = tk.Button(self.button_frame, text='Out ✖️', width=8, height=2, command=lambda i='W': self.add_digit(i) )
                button_Bounce_ball.grid(row=0, column=9, padx=5, pady=5)

                # # Create back and save buttons
                back_button = tk.Button(self.button_frame_main, text="Back", width=5, height=2, command=self.remove_last_digit)
                back_button.grid(row=0, column=3, padx=10, pady=20)

                save_button = tk.Button(self.button_frame_main, text="Save", width=5, height=2, command=lambda i = j: self.save_text(i))
                save_button.grid(row=0, column=5, padx=10, pady=15)

                self.root.mainloop()

            else:
                self.root.destroy()
                self.save_data_in_csv()
   
    def save_text(self,x):
                total = 0
                global temp 
                
                if len(self.wiket_count)!=10:
                    if x==7:
                        answer = messagebox.askyesno(f"Huuree!", "You Won The Match! Do you want to save the over?")
                    else:
                        answer = messagebox.askyesno(f"Over {self.over}", "Do you want to save the over?")
                         
                    if answer:
                        self.text_to_save.append(self.label_text.get())

                        for s in  self.real_data_for_ball:    
                            if type(s) is int:
                                total = total + s
                        
                        if len(self.total_runs) != int(self.over):
                            total = total + self.real_data_for_other_ball.count('WB')
                            self.total_runs.append(total)

                        if len(self.real_data_for_ball) == 6 or int(x) ==7:

                            self.itemset[0] = self.itemset[0] + 1
                            temp = 0
                            for i in self.total_runs:
                                temp = temp + i

                            if len(self.counting)==1:    
                                for j in  range(1,len(self.real_data_for_ball)+1):
                                    self.df1.loc[self.itemset[0]-1,str(j)] = str(self.real_data_for_ball[j-1])
                                    self.df1.loc[self.itemset[0]-1,'Wide Ball Runs'] = int(len(self.real_data_for_other_ball))
                                    self.df1.loc[self.itemset[0]-1,'Total'] = int(total)
                                self.df1.to_csv(f"{self.team1} vs {self.team2}/{self.batting_team_name}.csv",index=False)


                            if len(self.counting)==2:    
                                for j in  range(1,len(self.real_data_for_ball)+1):
                                    self.df2.loc[self.itemset[0]-1,str(j)] = str(self.real_data_for_ball[j-1])
                                    self.df2.loc[self.itemset[0]-1,'Wide Ball Runs'] = len(self.real_data_for_other_ball)
                                    self.df2.loc[self.itemset[0]-1,'Total'] = total
                                self.df2.to_csv(f"{self.team1} vs {self.team2}/{self.batting_team_name}.csv",index=False)
                            
                            
                            
                            if self.itemset[0] != int(self.over) and x!=7:
                                self.over_count_text.set("Over : "+str(self.itemset[0]))
                                self.real_data_for_ball.clear()
                                self.real_data_for_other_ball.clear()
                                self.real_data_display.clear()
                                self.label_text.set(' '.join(self.real_data_display))
                                self.final(temp)
                                
                            else:
                                self.over_count_text.set("Over : "+str(self.itemset[0]))
                                self.real_data_for_ball.clear()
                                self.real_data_for_other_ball.clear()
                                self.real_data_display.clear()
                                self.label_text.set(' '.join('All The Best,Match End!'))
                                self.total_runs.clear()
                                self.itemset[0] = 0
                                self.final(temp)

                                if len(self.counting) == 1:
                                    
                                    self.df1.fillna(0)
                                    self.chasing_runs = self.df1['Total'].values.sum()
                                    self.chasing.set(' '.join("First Batting"))

                                if int(x) == 7:
                                    self.new_window_for_bat(x)
                                
                                elif int(x) == 0: 
                                    self.root.destroy()
                                    x = 1
                                    self.new_window_for_bat(x)

                                else:
                                    self.root.destroy()
                                    x = 0
                                    self.new_window_for_bat(x)                 

                        elif self.itemset[0] == int(self.over):
                            self.label_text.set(' '.join('All The Best,Match End!'))
                            self.final(temp)
                            self.new_window_for_bat(x)      

                        else:
                            messagebox.showwarning("Nothing to save!","Please Attempt All Balls!")
                    else:
                        pass

                else:
                    
                    for s in  self.real_data_for_ball:    
                            if type(s) is int:
                                total = total + s
                        
                    if len(self.total_runs) != int(self.over):
                                total = total + self.real_data_for_other_ball.count('WB')
                                self.total_runs.append(total)
                    temp = 0
                    for i in self.total_runs:
                        temp = temp + i
                    self.final(temp)
                    
                    if self.label_text.get() != 'A l l   T h e   B e s t , M a t c h   E n d !':
                                if len(self.counting)==1:    
                                    for j in  range(1,len(self.real_data_for_ball)+1):
                                        self.df1.loc[self.itemset[0]-1,str(j)] = str(self.real_data_for_ball[j-1])
                                        self.df1.loc[self.itemset[0]-1,'Wide Ball Runs'] = len(self.real_data_for_other_ball)
                                        self.df1.loc[self.itemset[0]-1,'Total'] = total
                                    self.df1.to_csv(f"{self.team1} vs {self.team2}/{self.batting_team_name}.csv",index=False)


                                if len(self.counting)==2:    
                                    for j in  range(1,len(self.real_data_for_ball)+1):
                                        self.df2.loc[self.itemset[0]-1,str(j)] = str(self.real_data_for_ball[j-1])
                                        self.df2.loc[self.itemset[0]-1,'Wide Ball Runs'] = len(self.real_data_for_other_ball)
                                        self.df2.loc[self.itemset[0]-1,'Total'] = total
                                    self.df2.to_csv(f"{self.team1} vs {self.team2}/{self.batting_team_name}.csv",index=False)
                                
                        
                                self.real_data_for_ball.clear()
                                self.real_data_for_other_ball.clear()
                                self.real_data_display.clear()
                                self.total_runs.clear()
                                self.itemset[0] = 0
                                
                                if len(self.counting) == 1:
                                            self.df1.fillna(0)
                                            self.chasing_runs = self.df1['Total'].values.sum()
                                            self.chasing.set(' '.join("First Batting"))


                                if int(x) == 7:
                                    self.root.destroy()
                                    self.new_window_for_bat(x)
                                        
                                elif int(x) == 0: 
                                    self.root.destroy()
                                    x = 1
                                    self.new_window_for_bat(x)

                                else:
                                    self.root.destroy()
                                    x = 0
                                    self.new_window_for_bat(x)
                    
                    self.label_text.set(' '.join('All The Best,Match End!')) 
                    messagebox.showwarning("Team All Out!!","Over Saved!")

    def final(self,t):
            self.run = t
            self.temp_text.set("Runs: "+str(t))
    
    def add_digit(self,digit):

            global ball

            if self.itemset[0] != int(self.over) and len(self.wiket_count)!=10:
                
                if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 6 or digit == 0 or digit == 'W':
                    
                    if 0 <= len(self.real_data_for_ball) <= 5 :    
                        
                        if digit == 'W' :
                            self.wiket_count.append(digit)
                            self.real_data_display.append(" || " + str(digit))
                            self.real_data_for_ball.append(digit)
                            
                            if len(self.counting) == 2:
                                self.run_list.append(0)

                        elif len(self.real_data_for_ball) == 0:
                            ball = len(self.real_data_for_ball)+1
                            self.real_data_for_ball.append(digit)
                            self.real_data_display.append(" || " + str(digit))   
                             
                            if len(self.counting) == 2:
                                self.run_list.append(digit)

                        else:    
                            self.real_data_for_ball.append(digit)
                            ball = len(self.real_data_for_ball)
                            self.real_data_display.append(" || " + str(digit))
                            
                            if len(self.counting) == 2:
                                self.run_list.append(digit)

                        self.over_count_text.set("Over : "+str(self.itemset[0])+"."+str(len(self.real_data_for_ball)))
                    
                    if len(self.real_data_for_ball) == 6:
                        
                        if self.real_data_display[-1] != (" || Over!"):
                            self.real_data_display.append(" || " + 'Over!')
                            self.over_count_text.set("Over : "+str(self.itemset[0])+"."+str(len(self.real_data_for_ball)))
                        
                        else:
                            pass
                
                if digit == 'WB':
                    
                    if len(self.real_data_for_ball) != 6: 
                        self.real_data_for_other_ball.append(digit)
                        self.real_data_display.append(" || " + digit)
                        
                        if len(self.counting) == 2:
                                self.run_list.append(1)


                self.label_text.set(' '.join(self.real_data_display))
                self.wiket_count_text.set("Wiket : " + str(len(self.wiket_count)))
                
                if len(self.counting) == 2:
                             t = 0
                             for i in self.run_list:
                                  t = t + i
                             self.temp_text.set("Runs: "+str(t))
                             
                             if t > self.chasing_runs:
                                  self.save_text(7)

            else:

                self.label_text.set(' '.join('All The Best,Match End!'))

            if len(self.wiket_count)==10:
                self.save_text(9)
                
    def remove_last_digit(self):

            if len(self.wiket_count)!=10:
                if len(self.real_data_display) > 0:
                
                    if self.real_data_display[-1] == (" || Over!"):
                        self.real_data_display.pop()

                    elif self.real_data_display[-1] == ' || WB':
                            self.real_data_for_other_ball.pop()
                            self.real_data_display.pop()

                            if len(self.counting) == 2:
                                self.run_list.pop()

                    elif self.real_data_display[-1] ==  ' || 0' or self.real_data_display[-1] == ' || 1' or self.real_data_display[-1] == ' || 2' or self.real_data_display[-1] == ' || 3' or self.real_data_display[-1] == ' || 4' or self.real_data_display[-1] == ' || 6' or self.real_data_display[-1] == ' || W':
                    
                            if self.real_data_display[-1] == ' || W':
                                self.wiket_count.pop()
                            
                            if len(self.counting) == 2:
                                self.run_list.pop()

                            self.real_data_for_ball.pop()
                            self.real_data_display.pop()
                
                print_data = []
                for i in self.real_data_display:
                    print_data.append (str(i))
                self.label_text.set(' '.join(print_data))
                
    def save_data_in_csv(self):
        

        self.ds1 = pd.read_csv(f"{self.file_path1}")
        self.ds2 = pd.read_csv(f"{self.file_path2}")

        x = self.ds1['Total'].dropna().sum()
        y = self.ds2['Total'].dropna().sum()


        self.team1_runs = x.sum()
        self.team2_runs = y.sum()

        self.result = tk.Tk()
        self.result.geometry("800x700")
        self.result.state('zoomed')
        self.result.title("Cricket Metrics Result Pannel")
         
        self.label1 = tk.Label(self.result,text="Result",font=("Helvetica", 35 ,"bold"),fg="Purple")
        self.label1.pack(pady=20)

        if self.team1_runs > self.team2_runs :
            self.label = tk.Label(self.result,text=f"{self.team1} Won The Match!",font=("Helvetica", 30 ,"bold"),fg="blue")
            self.label.pack(pady=20)
        
        if self.team1_runs < self.team2_runs :
            self.label = tk.Label(self.result,text=f"{self.team2} Won The Match!",font=("Helvetica", 30 ,"bold"),fg="blue")
            self.label.pack(pady=20)
        
        if self.team1_runs == self.team2_runs :
            self.label = tk.Label(self.result,text=f"Match Tay!",font=("Helvetica", 30 ,"bold"),fg="blue")
            self.label.pack(pady=20)

        self.label2 = tk.Label(self.result, text=f"{self.team1} Score: {self.team1_runs}", font=("Calibri", 30,'bold'))
        self.label2.pack(ipady=50)

        self.label3 = tk.Label(self.result, text=f"{self.team2} Score {self.team2_runs}", font=("Calibri", 30,'bold'))
        self.label3.pack(ipady=50)

        self.make_analytics_charts()

    def make_analytics_charts(self):

       try:
             
        if not os.path.exists(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/"):
            os.makedirs(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/")

        #1 comparison of both team on plot graph:
        plt.figure(figsize=(10,5))
        plt.title('Camparision Of Both Team Score',fontsize=18,fontweight='bold',fontfamily='serif')
        plt.plot(self.ds1['Overs'],self.ds1["Total"],color='black',label=f"{self.team1}",marker="o",markersize=10)
        plt.plot(self.ds2['Overs'],self.ds2["Total"],color='blue',label=f"{self.team2}",marker="o",markersize=10)
        plt.xlabel('Overs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.xticks(self.ds2["Overs"])
        plt.ylabel('Runs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.legend()
        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/Camparision Of Both Team Score in plot.png")         

        #2 team 1 Score In Each Over on bar graph:
        x = list(self.ds1["Overs"])
        y = list(self.ds1["Total"])

        plt.figure(figsize=(10,5))
        plt.bar(x,y,color='skyblue',width=0.5)
        plt.title(f'{self.team1} Score In Each Over',fontsize=15,fontweight='bold',fontfamily='serif')
        plt.xticks(x)
        plt.xlabel('Overs',fontsize=20,fontweight='bold',fontfamily='serif')
        plt.ylabel('Runs',fontsize=20,fontweight='bold',fontfamily='serif')

        for i, j in zip(x, y):
            plt.text(i, j, j, ha='center',fontweight='bold',fontsize=12)

        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/{self.team1} Score.png")

        #3 team 2 Score In Each Over on bar graph:
        x = list(self.ds2["Overs"])
        y = list(self.ds2["Total"])

        plt.figure(figsize=(10,5))
        plt.bar(x,y,color='cyan',width=0.5)
        plt.title(f'{self.team2} Score In Each Over',fontsize=15,fontweight='bold',fontfamily='serif')
        plt.xticks(x)
        plt.xlabel('Overs',fontsize=20,fontweight='bold',fontfamily='serif')
        plt.ylabel('Runs',fontsize=20,fontweight='bold',fontfamily='serif')

        for i, j in zip(x, y):
            plt.text(i, j, j, ha='center',fontweight='bold',fontsize=12)

        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/{self.team2} Score.png")

        #4 Team1 4's And 6's In Each Over:
                
        x1 = []
        w1 = []

        for i in range(0,len(self.ds1['Overs'].values)):
            x1.append(list(self.ds1.iloc[i,1:7].values).count(4))
            w1.append(list(self.ds1.iloc[i,1:7].values).count(6))


        plt.figure(figsize=(10,5))
        plt.title(f"{self.team1} 4's And 6's In Each Over",fontsize=18,fontweight='bold',fontfamily='serif')
        xaxis = np.arange(len(self.ds1["Overs"]))
        plt.bar(xaxis-0.1,x1,0.2,color='skyblue',label="4's")
        plt.bar(xaxis+0.1,w1,0.2,color='pink',label="6's")
        plt.xlabel('Overs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.xticks(xaxis,self.ds1["Overs"])
        plt.ylabel("4's And 6's",fontsize=12,fontweight='bold',fontfamily='serif')
        plt.legend()
        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/{self.team1}4's And 6's.png")

        #5 Team2 4's And 6's In Each Over:
                
        x1.clear()
        w1.clear()

        for i in range(0,len(self.ds2['Overs'].values)):
            x1.append(list(self.ds2.iloc[i,1:7].values).count(4))
            w1.append(list(self.ds2.iloc[i,1:7].values).count(6))

        plt.figure(figsize=(10,5))
        plt.title(f"{self.team2} 4's And 6's In Each Over",fontsize=18,fontweight='bold',fontfamily='serif')
        xaxis = np.arange(len(self.ds1["Overs"]))
        plt.bar(xaxis-0.1,x1,0.2,color='skyblue',label="4's")
        plt.bar(xaxis+0.1,w1,0.2,color='pink',label="6's")
        plt.xlabel('Overs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.xticks(xaxis,self.ds1["Overs"])
        plt.ylabel("4's And 6's",fontsize=12,fontweight='bold',fontfamily='serif')
        plt.legend()
        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/{self.team2}4's And 6's.png")

        #6 Camparision Of Both Team Score IN BAR:

        plt.figure(figsize=(10,5))
        plt.title('Camparision Of Both Team Score',fontsize=18,fontweight='bold',fontfamily='serif')
        xaxis = np.arange(len(self.ds1["Overs"]))
        plt.bar(xaxis-0.1,self.ds1["Total"],0.2,color='skyblue',label=f"{self.team1}")
        plt.bar(xaxis+0.1,self.ds2["Total"],0.2,color='black',label=f"{self.team2}")
        plt.xlabel('Overs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.xticks(xaxis,self.ds2["Overs"])
        plt.ylabel('Runs',fontsize=12,fontweight='bold',fontfamily='serif')
        plt.legend(fontsize=15)
        plt.savefig(f"{self.team1} vs {self.team2}/{self.team1} & {self.team2} Analitics/Camparision Of Both Team Score in bar.png")

       except Exception as E:
            print(E)
       

obj1 = Match()
