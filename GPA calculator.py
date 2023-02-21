import customtkinter
import tkinter as tk
import os

gpa=["A+","A","B+","B","C+","C","D","F"]

gpa_value= {
    "A+":4,
    "A":3.667,
    "B+":3.334,
    "B":3,
    "C+":2.667,
    "C":2.334,
    "D":2,
    "F":0
    } 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
resaltion="1980x1024"
root=customtkinter.CTk()
root.geometry(resaltion)

root.title("GPA calculator")

frame=customtkinter.CTkFrame(master=root,corner_radius=0,fg_color="#17181c")
frame.pack(fill="both",expand=True)

frame1=customtkinter.CTkFrame(master=root,border_width=3,fg_color="#243b67",border_color="#ffffff")
frame1.place(x=0,y=0,width=400,height=1000,)


def semster():
    for widget in frame.winfo_children():
        widget.destroy()
        
    data=[]
    hour=[]
    def insertt():
        gpa=int(gpa_cr_in.get())*gpa_value[gpa_in.get()] 
        data.append(gpa)
        hour.append(int(gpa_cr_in.get()))
        view.insert("1.0",gpa_in.get()+"\n")
    def calcc():
        gpa_total=sum(data)/sum(hour)
        gpa_valuee.delete(0,"end")
        gpa_valuee.insert(10,gpa_total)
        
    titl=customtkinter.CTkLabel(master=frame,text="Semester GPA Calculator",font=("Roborto",24),text_color="#ffffff")
    titl.place(y=30,x=800)
 
        
    gpa_cr_in=customtkinter.CTkEntry(master=frame,placeholder_text="credit hour")
    gpa_cr_in.place(x=400,y=200)
    
    gpa_cr_in_label=customtkinter.CTkLabel(master=frame,text="Select GPA For Course",font=("Roborto",20),text_color="#ffffff")
    gpa_cr_in_label.place(x=500,y=100)

    gpa_in=customtkinter.CTkOptionMenu(master=frame,values=gpa,text_color="black",fg_color="#eaebed")
    gpa_in.place(x=600,y=200)

    insert=customtkinter.CTkButton(master=frame,text="Insert",text_color="black",fg_color="#eaebed",command=insertt)
    insert.place(x=500,y=250)
    
    calc=customtkinter.CTkButton(master=frame,text="Calc",text_color="black",fg_color="#eaebed",command=calcc)
    calc.place(x=500,y=350)
    
    gpa_value_label=customtkinter.CTkLabel(master=frame,text="Semseter GPA:",font=("Roborto",18),text_color="#ffffff")
    gpa_value_label.place(x=400,y=400)

    note=customtkinter.CTkLabel(master=frame,text="Notes:\n A+=4 \n A=3.667 \n B+=3.334 \n B=3 \n C+=2.667 \n C=2.334 \n D=2 \n F=0",font=("Roborto",18),text_color="#ffffff")
    note.place(x=1300,y=150)

    view=customtkinter.CTkTextbox(master=frame)
    view.place(x=900,y=150)
    
    
    gpa_valuee=customtkinter.CTkEntry(master=frame,placeholder_text="GPA")
    gpa_valuee.place(x=600,y=400)
    
    
def cumlative():
    for widget in frame.winfo_children():
        widget.destroy()
    
    def calcc():
        gp1=float(gpa_cr_in.get())*float(gpa_cr_v_in.get())
        gp2=float(n_gpa_cr_in.get())*float(n_gpa_cr_v_in.get())
        gp3=(gp1+gp2)/(float(gpa_cr_in.get())+float(n_gpa_cr_in.get()))
        
        gpa_cu.delete(0,"end")
        gpa_cu.insert(10,gp3)
        
    titl=customtkinter.CTkLabel(master=frame,text="Cumlative GPA Calculator",font=("Roborto",24),text_color="#ffffff")
    titl.place(y=30,x=800)
 
        
    gpa_cr_in=customtkinter.CTkEntry(master=frame,placeholder_text="credit hour")
    gpa_cr_in.place(x=600,y=200)
    
    gpa_cr_in_label=customtkinter.CTkLabel(master=frame,text="pervious credit hour:",font=("Roborto",18),text_color="#ffffff")
    gpa_cr_in_label.place(x=400,y=200)


    gpa_cr_v_in=customtkinter.CTkEntry(master=frame,placeholder_text="gpa")
    gpa_cr_v_in.place(x=950,y=200)
    
    gpa_cr_v_in_label=customtkinter.CTkLabel(master=frame,text="pervious gpa:",font=("Roborto",18),text_color="#ffffff")
    gpa_cr_v_in_label.place(x=800,y=200)

    
    n_gpa_cr_in=customtkinter.CTkEntry(master=frame,placeholder_text="credit hour")
    n_gpa_cr_in.place(x=600,y=300)
    
    n_gpa_cr_in_label=customtkinter.CTkLabel(master=frame,text="this semster credit hour:",font=("Roborto",18),text_color="#ffffff")
    n_gpa_cr_in_label.place(x=400,y=300)


    n_gpa_cr_v_in=customtkinter.CTkEntry(master=frame,placeholder_text="gpa")
    n_gpa_cr_v_in.place(x=950,y=300)
    
    n_gpa_cr_v_in_label=customtkinter.CTkLabel(master=frame,text="this semster gpa:",font=("Roborto",18),text_color="#ffffff")
    n_gpa_cr_v_in_label.place(x=800,y=300)
    
    calc=customtkinter.CTkButton(master=frame,text="Calc",text_color="black",fg_color="#eaebed",command=calcc)
    calc.place(y=400,x=650)
    
    gpa_cu=customtkinter.CTkEntry(master=frame,placeholder_text="gpa")
    gpa_cu.place(y=450,x=650)
    
    
    
title=customtkinter.CTkLabel(master=frame,text="GPA Calculator",font=("Roborto",24),text_color="#ffffff")
title.place(y=30,x=800)

left_title=customtkinter.CTkLabel(master=frame1,text="Options",font=("Roborto",24),text_color="#ffffff")
left_title.place(y=20,x=120)

add_button=customtkinter.CTkButton(master=frame1,text="semester GPA",text_color="black",fg_color="#eaebed",command=semster)
add_button.place(y=70,x=90)


update_button=customtkinter.CTkButton(master=frame1,text="cumlative GPA",text_color="black",fg_color="#eaebed",command=cumlative)
update_button.place(y=120,x=90)



title=customtkinter.CTkLabel(master=frame,text="GPA Calculator",font=("Roborto",24),text_color="#ffffff")
title.place(y=30,x=800)

title=customtkinter.CTkLabel(master=frame,text="Chosse an Option",font=("Roborto",24),text_color="#ffffff")
title.place(y=400,x=800)

root.mainloop()
