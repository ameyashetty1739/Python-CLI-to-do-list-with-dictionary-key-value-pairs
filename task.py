import typer 
import pickle
import sys
import os

from typer.main import Typer
from typing import Optional
app = typer.Typer(add_completion=False)






@app.command()
def help():
    y="""Usage :-\n
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list\n
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n
$ ./task del INDEX            # Delete the incomplete item with the given index\n
$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n
$ ./task help                 # Show usage\n
$ ./task report               # Statistics"""
    print(y)


@app.command()
def add(priority:Optional[str] = typer.Argument(None),task: Optional[str] = typer.Argument(None)):
    if priority==None and task==None:
        print("Error: Missing tasks string. Nothing added!")
    else:
        try:
            dict1={}
            dict1.update({task:priority})
            filesize1= os.stat('output.pickle').st_size
            if filesize1==0:
                pf=open("output.pickle","wb")
            else:
                pf=open("output.pickle","ab")
            pickle.dump(dict1, pf)
            pf.close()
            pf=open("output.pickle","rb")
            dict2={}
            while 1:
                try:
                    dict2.update(pickle.load(pf))
                except EOFError:
                    break
            pf.close()
            dict3={k:v for k,v in sorted(dict2.items(),key= lambda v:v[1])}
            print('Added task: "'+task+'" with priority '+str(priority))
    
            file1=open("ls.txt","w+")
    
            i=1
            for  key,value  in dict3.items():
                file1.write(str(i)+". "+key+ " ["+str(value)+"]"+"\n")
                i=i+1

        except:
            print("")


        
            
    

    
    
        
        
        

@app.command()
def ls():
    file1=open("ls.txt","r")
    filesize1= os.stat('ls.txt').st_size
    i=len(file1.readlines())

    if filesize1==0:
        print("There are no pending tasks!")
    else:
        file1=open("ls.txt","r")
        print(file1.read())
        file1.close()

    

@app.command()
def done(taskno:Optional[int] = typer.Argument(None)):
    if taskno==None:
        print("Error: Missing NUMBER for marking tasks as done.")
    else:
        dpf1=open("output.pickle","rb")
        dict4={}
        while 1:
            try:
                dict4.update(pickle.load(dpf1))
            except EOFError:
                break
        dpf1.close()
        dict4={k:v for k,v in sorted(dict4.items(),key= lambda v:v[1])}
        y=taskno
        c=0
        t=len(dict4.keys())
        
        for key,value in list(dict4.items()):
            c=c+1
            if c == y:
                dict5={}
                dict5.update({key:value})
                dpf2=open("Completed.txt","a+")
                filesize2 = os.stat('Completed.txt').st_size
                dpf2.close()


            
                if filesize2==0:
                    dpf2=open("Completed.txt","a+")
                    dpf2.write("1"+". "+key+ " ["+str(value)+"]\n")
                    dpf2.close()
                else:
                    dpf2=open("Completed.txt","r")
                    l=len(dpf2.readlines())+ 1
                    dpf2.close()
                    dpf2=open("Completed.txt","a+")
                    dpf2.write(str(l)+". "+key+ " ["+str(value)+"]\n")
                    dpf2.close()
            
                del dict4[key]
                dict4={k:v for k,v in sorted(dict4.items(),key= lambda v:v[1])}
                dpf3=open("output.pickle","wb")
                pickle.dump(dict4, dpf3)
                dpf3.close()
                file1=open("ls.txt","w+")
                i=1
                for  key,value  in dict4.items():
                    file1.write(str(i)+". "+key+ " ["+str(value)+"]"+ "\n")
                    i=i+1
            
            
                print("Marked item as done.")
        if (taskno==0 or c<t):
            print(f"Error: no incomplete item with index #{taskno} exists.")

    

    
        


@app.command()
def delete(taskno:Optional[int] = typer.Argument(None)):
    if(taskno==None):
        print("Error: Missing NUMBER for deleting tasks.")
    
    else:
        depf=open("output.pickle","rb")
        dict6={}
        while 1:
            try:
                dict6.update(pickle.load(depf))
            except EOFError:
                break
        dict6={k:v for k,v in sorted(dict6.items(),key= lambda v:v[1])} 
        depf.close()
        y= taskno
        c=0
        for key,value in list(dict6.items()):
            c=c+1
            if c == y:
                print(f"Deleted task #{c}")
                del dict6[key]

                dict6={k:v for k,v in sorted(dict6.items(),key= lambda v:v[1])}
                depf2=open("output.pickle","wb")
                pickle.dump(dict6, depf2)
                depf2.close()
                file1=open("ls.txt","w+")
                i=1
                for  key,value  in dict6.items():
                    file1.write(str(i)+". "+key+ " ["+str(value)+"]"+ "\n")
                    i=i+1
        if (taskno==0 or taskno>c):
            print(f"Error: task with index #{taskno} does not exist. Nothing deleted.")
        
    

    

@app.command()
def report():
    file1=open("ls.txt","r")
    y=len(file1.readlines())
    print("Pending : "+str(y))
    file1.close()
    file1=open("ls.txt","r")
    ls_lines = file1.read()
    print(ls_lines)
    file2=open("Completed.txt","r")
    z=len(file2.readlines())
    print("Completed : "+str(z))
    file2.close()
    file2=open("Completed.txt","r")
    compl_lines= file2.read()
    print(compl_lines)
    file2.close()

    
    




    






            


    
    



        



            



            



            
                           
            


         


    



    
    





if __name__=="__main__":
    if len(sys.argv)==1:
        help()
    else:
        app()

    
    
       
