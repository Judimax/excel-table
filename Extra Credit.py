from table import *
from Simplestack import *


print("Here you can have certain properties of your table displayed in this interface\n")


undo= Simplestack("$")
redo= Simplestack("$")
# for undo and redo purposes


c=0 #for raw print purposes

sort_stack = [] #for quicksort purposes
a=1
info = Table()
repeat_sort_i = [] #to give copy of concatenation a different memory location in order to nullify class-copying properties
repeat_sort_ii = []

class PrintError(Exception):
    def __init__(self,value):
        self.value = value

while True:

    if a == 0:
        undo.push(Table(first_one))
        a=1
    print(undo)

    
    command = str(input("Please enter the desired action\t"))
    
    if command == "q":
        break
        
    elif command == "help":
            print("q -- quits the program")
            print("help -- prints the help message")
            print("? -- same as help")
            print("load filename")
            print("save newfilename")
            print("print -- prints out list")
            print("dump")
            print("select  field > value")
            print("project field1,field2,field3")
            print("update key,value,changefield,changevalue")
            print("sort by field1,field2,field3")
            print("undo")
            print("redo\n")

            print("Enter command or ? for help:")

    elif command == "?":
            print("q -- quits the program")
            print("help -- prints the help message")
            print("? -- same as help")
            print("load filename")
            print("save newfilename")
            print("print -- prints out list")
            print("dump")
            print("select  field > value")
            print("project field1,field2,field3")
            print("update key,value,changefield,changevalue")
            print("sort by field1,field2,field3")
            print("undo")
            print("redo\n")

            print("Enter command or ? for help:")

    elif command.find("load") != -1:

        a=0
        
        command =command.strip("load ")
        first_one = command
        info = Table(command)  
        
        
        
    elif command.find("save") != -1:
        command = command.strip("save ")

        save_table = open(command,'w')

        original_form = ""
        next_original= ""

        for s in info.dictionary:
            if original_form == "":
                original_form =str(s)
            else:
                original_form += "," + str(s)
        original_form += "\n"
        

        for row in info.rows:

            for i in row:
                if i == row[0]:
                    next_original += str(i)
                elif next_original == "":
                    next_original = str(i)
                elif i.find('"') != -1:
                    next_original += "," + str(i)
                elif i.find(",") != -1:
                    next_original += "," + '"' + str(i) + '"'
                else:
                    next_original += "," + str(i)

            next_original += "\n"

            
        save_table.write(original_form)
        save_table.flush()
        save_table.write(next_original)
        save_table.flush()
        save_table.close()
        original_form = ""
        next_original = ""
        

    elif command == "print":
        try:
            if c ==1:
                c=0
                print(info,type(info))
            else:
                print(info.pretty_print())       
        except:
            raise PrintError(info)
            

    elif command == "dump":
        c =1
        """raw = Table.__str__(info) actually worked now I know how to get it if I need it"""

        

    elif command.find("select") != -1:
        command = command.strip("select ")
        select_stack = info.select(command)
        undo.push(select_stack)

        info = info.select(command)
        

        
    elif command.find("project") != -1:
        project= "project "
        command = command[len(project):]
        project_stack = info.project(command)
        undo.push(project_stack)

        info = info.project(command)



    elif command.find("update") != -1:
        update = "update "

        command = command[len(update):]
        command = command.split(",")
        
        info.update(command[0],command[1],command[2],command[3])

        update_stack = info
        undo.push(update_stack)
        
        
    elif command.find("sort by ") != -1:
        sort= "sort by "
        
        command = command[len(sort):]
        
        if command.count(",") == 2:

             
            info.sort(command)

            repeat_sort_i = info.dictionary
            repeat_sort_ii= info.rows

            repeat_sort = Table()
            repeat_sort.dictionary = repeat_sort_i
            repeat_sort.rows = repeat_sort_ii
            undo.push(repeat_sort)

            repeat_sort_i = []
            repeat_sort_ii = []
            
        elif command.count(",") == 1:
            
             
            info.sort(command)

            repeat_sort_i = info.dictionary
            repeat_sort_ii= info.rows

            repeat_sort = Table()
            repeat_sort.dictionary = repeat_sort_i
            repeat_sort.rows = repeat_sort_ii
            undo.push(repeat_sort)

            repeat_sort_i = []
            repeat_sort_ii = []
            
        
        else:
            info.sort(command)

            repeat_sort_i = info.dictionary
            repeat_sort_ii= info.rows

            repeat_sort = Table()
            repeat_sort.dictionary = repeat_sort_i
            repeat_sort.rows = repeat_sort_ii
            undo.push(repeat_sort)

            repeat_sort_i = []
            repeat_sort_ii = []

        
        
        
        
        #learn how to program reading-in args
        #fix quicksort to accept as many args

        

    elif command == "undo":

        if undo != []:

            last_one = undo.pop() #pop() is not working properly
            info = last_one
            redo.push(last_one)
            
                  
        else:
            print("Cannot undo")

        

    elif command == "redo":

        if redo != []:
            repeat_one = redo.last()
            info = repeat_one
            
        else:
            print("Cannot redo")

         
            
        
        
        
    

            

    

                
        
