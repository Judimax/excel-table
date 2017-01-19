import helper



class TableError(Exception):
    def __init__(self, value):
        self.value = value

class Table:
    def __init__ (self, filename=""):   #DON'T CHANGE!
        self.rows = []
        self.dictionary = []     # list of strings, which are field names
        if filename != "":
            self.read_table(filename)

    
    
    
    def _partition(self,fieldnamelist,i,k,indexer):

                low = 0
                high = 0;
                midpoint = 0
                pivot = 0
                temp = 0
                done = False

                midpoint = i +(k-i)//2
                pivot= fieldnamelist[midpoint][indexer]

                low=i
                high=k

                while not done:

                        while fieldnamelist[low][indexer] < pivot:
                                
                                low += 1
                                
                        while pivot < fieldnamelist[high][indexer]:
                                
                                high -=1

                        if low >= high:
                                done = True
                        else:
                                temp= fieldnamelist[low]
                                fieldnamelist[low]= fieldnamelist[high]
                                fieldnamelist[high]= temp

                                low +=1
                                high -=1
                
                return high

    
    # YOU REPLACE THIS WITH QUICKSORT
    def sort(self, args):     # changes this table's data, no return value
        ''' sorts the data table in place.  You give it a comma-separated string of field names
             (no spaces!) and it will sort by the first field first, then the second field within the first,
             and so on.'''
        
        field = []
        
        if  args == "":
            pass
        
        if args.count(",") == 0:

            indexer = self._getFIeldNumber(args)
            #print(indexer) to see if function performed as desired
            
            for row in self.rows:
                        
                field.append(row)
                        
            self.rows =self._quicksort(field, 0, len(field)-1,indexer) #sorts according to indexer
        
            return self.rows

        else:

            args = args.split(",")

            prime_indexer = self._getFIeldNumber(args[0]) #to let quicksort know what to sort by
            
            
            for row in self.rows:
                field.append(row)

            for_self_rows= self._quicksort(field,0,len(field)-1,prime_indexer)



                
            """--------------------------------get this to loop to deal w/ as many args -------------------------"""
            
            for t in range(len(args)-1):
                
                tabifier=[]
                dict_tab= []
                comp_tab=[]
                comb_tab = []
                this_tab= []

                for i in range(len(for_self_rows)):
                    pre_tab = []
                    pre_tab.append(for_self_rows[i][prime_indexer])
                    comp_tab.append(pre_tab)



                
                fst_indexer= self._getFIeldNumber(args[t])
                snd_indexer = self._getFIeldNumber(args[t+1])

                save_tab = [] #to minor sort comp_tab
                for i in range(len(for_self_rows)):
                    pre_tab = []
                    pre_tab.append(for_self_rows[i][prime_indexer])
                    save_tab.append(pre_tab)

                for i in range(len(for_self_rows)): 

                    save_tab[i].append(for_self_rows[i][prime_indexer])
                
            
                for value in range(len(for_self_rows)):                 #2 tabs to compare up to 3
                    dict_tab.append(for_self_rows[value][prime_indexer])
                

                for value in range(len(for_self_rows)):
                    tabifier.append(for_self_rows[value][fst_indexer])

                
                for i in dict_tab: #<-----------------------------------------
                    
                    this_tab.append(i)
                    comb_tab.append(this_tab)
                    this_tab = []

                

                
                for i in tabifier: #dont touch
                    
                    if tabifier.count(i) > 1:
                        tabifier.remove(i)



                for i in dict_tab: #dont touch

                    if dict_tab.count(i) > 1:
                        dict_tab.remove(i)



                for i in range(len(for_self_rows)): #<----------------------------------------------------

                    comp_tab[i].append(for_self_rows[i][fst_indexer])
                    this_tab = []

                for i in comp_tab: #don't touch

                    if comp_tab.count(i) > 1:
                        comp_tab.remove(i)

                for i in save_tab:
                    if save_tab.count(i) >1:
                        save_tab.remove(i)
 


                i =0
                while i == 0:
                    if True:
                        i = 0
                        for i in range(len(comp_tab)): #Would have used quicksort but it would take too much time and I have other work to take care of
                            if comp_tab[i][0] == comp_tab[i-1][0]:
                                if comp_tab[i][1] < comp_tab[i-1][1]:
                                    comp_tab[i][1],comp_tab[i-1][1] = comp_tab[i-1][1],comp_tab[i][1]
                    else:
                            i =1
                            break
                
                self._minor_sort(   comp_tab,    for_self_rows,     prime_indexer,    fst_indexer,     snd_indexer) #spaced out so you can see the args,

                comb_tab.clear()


                for i in range(len(for_self_rows)):
                    pre_tab = []
                    pre_tab.append(for_self_rows[i][prime_indexer])
                    comb_tab.append(pre_tab)



                comp_tab = comb_tab



    def _minor_sort(self,    tab,    sort_data,   indexer_prime,   indexer_i,    indexer_ii): # BTW: This was the last and hardest part of the project, but I got it

        self.rows = []


    

        for i in tab:

            minor_sort =[]

            k=0
            for sort in range(len(sort_data)):

                if sort_data[sort][indexer_prime] == i[0]:
                    
                    if sort_data[sort][indexer_i] == i[1]:


                        minor_sort.append(sort_data[sort])

                minor_sort == self._quicksort(minor_sort,0,len(minor_sort)-1,indexer_ii)

                    
            for i in minor_sort:

                self.rows.append(i)
        

          
    def _quicksort(self, names, i, k, indexer):
        j=0

        if i >= k:
            return
        else:
            j = self._partition(names,i,k,indexer)

            self._quicksort(names,i,j, indexer)
            self._quicksort(names, j + 1,k, indexer)
            
        # print(names)  to see if it actually did as intended 
        return names
     

    def _make_comparison_string(self, row, fieldnamelist):    #DON'T CHANGE!
        sortkey = ""
        for name in fieldnamelist:
            sortkey += self._getFieldValue(row, name) + ";"
        return sortkey
    
    def read_table(self, filename):    #  changes this table's data, no return value  #DON'T CHANGE!
        ''' reads a CSV file from the OS and loads the data into this table. ''
             The user must supply a filename. Gives titles table '''

        with open(filename) as f:
            lines = f.readlines()
    
        self.rows = []
        i = 0
        for line in lines:
            line = line.strip()
            linelist = helper.parseCSV(line)             # was linelist = line.split(",")
            row = [element.strip() for element in linelist]
            if i == 0:
                self.dictionary = row
            else:
                self.rows.append(row)
            i += 1
        print("Read table: ",filename)
        print(len(self.rows),"rows")
        print("self.dictionary=",self.dictionary)
        print("")

    def select(self, condition):     # returns a new Table    #DON'T CHANGE!
        ''' slices out certains rows that do not meet the condition.
             Returns a whole new table.
             The condition is a string that follows the convention of   field OP value
             where field is one of the named fields.  OP is  =, <>, <, >, <=, >=
             and value is either a string or a number.  If a string, no quotes are used!  '''

        newtab = Table()
        newtab.dictionary = self.dictionary
        condparts = Table._parseCommand(condition)
        newrows = []
        for row in self.rows:
            if self._fits(row, condparts):
                newrows += [row]
        newtab.rows = newrows
        return newtab

    # YOU ADD CODE TO THE END OF THIS
    def _fits(self, row, condparts):    # returns a boolean     
        ''' Internal method:  used by the select() method to actually test the
             condition and return its truth value. '''

        (varname, operator, target) = condparts
        fieldvalue = self._getFieldValue(row, varname)
        if operator == "=":
            return fieldvalue == target
        if operator == "<>":
            return fieldvalue != target
        if operator == "<":
            return fieldvalue < target
        if operator == ">":
            return fieldvalue > target
        if operator == "<=":
            return fieldvalue <= target
        if operator == ">=":
            return fieldvalue >= target
        

    def _parseCommand(command):   # returns a triple     #DON'T CHANGE!
        ''' Internal method:  used by the select() method.
             Breaks up the command by blanks and returns the three parts.
             Note, there must be at least one blank between the tokens.
             The form is                 FIELD OP VALUE
        '''

        varname = ""
        i = 0
        while i < len(command):                 # collect variable name,  can end in numbers
            ch = command[i]
            if ch.isalnum():
                varname += ch
                i += 1
            else: break 
        while i < len(command):                # skip over any blanks
            ch = command[i]
            if ch == ' ': i +=1
            else: break
        operator = ""
        opsymbols = "=<>"
        while i < len(command):                 # get the operator, =, <>  <, <=, >, >=
            ch = command[i]
            if ch in opsymbols:
                operator += ch
                i += 1
            else: break
        while i < len(command):                # skip over any blanks
            ch = command[i]
            if ch == ' ': i +=1
            else: break
        value = command [i:]                    # get the value or variable name
        return (varname, operator, value)

    def _getFieldValue(self, row, fieldname):   # returns an value    #DON'T CHANGE!
        ''' internal method:  looks up the fieldname in the dictionary and gets the position (an int)
             within each row.  Then it returns that part of the row. '''

        try:
            fieldnum = self.dictionary.index(fieldname)
        except ValueError as e:
            raise TableError("field: " + fieldname + " is not in the data dictionary")
        return row[fieldnum]
    
    

    def project(self, fieldnamelist):   # returns a new Table     #DON'T CHANGE!
        ''' slices out columns that do not appear in the fieldnamelist. 
             All the rows are kept, though (use select for that.) '''

        newtab = Table()
        newtab.dictionary = fieldnamelist.split(",")
        for row in self.rows:
            newrow = []
            for name in newtab.dictionary:
                newrow += [self._getFieldValue(row, name)]
            newtab.rows.append(newrow)
        return newtab

    #  YOU CHANGE THIS
    def __str__(self):  #  returns a str
            '''  Creates a string from the rows in this table and returns that string.
            Rows are separated by newlines. '''
        
            s = ""
            for name in self.dictionary:
                if s == "": s = name;
                
                else: s += "," + name
            s += "\n---------------------------------------------------\n"
            for row in self.rows:
                printable_row = ""
                for value in row:
                    if printable_row == "":
                        if value.find(',') != -1:
                            printable_row = '"' + value + '"'
                        else:
                            printable_row = value
                    elif value.find(",") != -1:
                        printable_row += "," +'"' + value + '"'                                                                
                    else:
                        printable_row += "," + value
                             
                s += "\n" + printable_row

            x =1
            return "\n" + s
        
        
    # YOU WRITE THIS
    def pretty_print(self):

        
        s  = ""
        format_i="%-" #becuase required formats will change deal with the problem as an int and concatenate str at the end
        format_ii= "s"
        format_list = []
        
        for x in range(len(self.dictionary)):
            
            formatter = 7#set equal to 10 to set apart at reasonable lengths if a row gets deleted, spaces left in between
            
            format_string = "%-10s" #to remember what ther are supposed to do 
            
            for row in self.rows:
                if len(row[x]) > formatter:
                    formatter = len(row[0])+3
            formatter += 5

            #print(formatter,formatter_i,formatter_ii,formatter_iii) used to keep track of format size make sure coded did as desired
                
            formatter = str(formatter) # so intrepreter reads formatter as one string and does not crash              
            format_string = format_i + formatter + format_ii
            format_list.append(format_string)
            
            #print(format_list) to see if updated formatters were updated correctly
                
        for q in range(len(format_list)):
                
            for name in range(len(self.dictionary)): #I used name instead of fieldnamelist becuase you had this in your _str_ function

                if q == name:
                    s += format_list[q] % (self.dictionary[name])

        s += "\n------------------------------------------------------------\n"
                                
        for row in self.rows:

            for i in range(len(row)): #takes care of double fields
                if row[i].find('"') != -1:
                    row[i] =row[i]
                elif row[i].find(",") != -1:
                    row[i]= '"' + row[i] + '"'

            for x in range(len(format_list)): #takes care of pretty print
                s += ((format_list[x]) % (row[x]))

            s += "\n"
        
            
        return "\n" + s
    # YOU WRITE THIS
    def _getFIeldNumber(self, fieldname):
        try:
            for i in range(len(self.dictionary)):
                if fieldname == self.dictionary[i]:
                    return i
                else:
                    pass    
        except:
            raise TableError("Value Not Found")
    def __int__(self):
        return ("%d" % (self.i))
        #YOU WRITE THIS
    def update(self, key_field, key_value, update_field, update_value):


        field_found=0 #break command did not work, used these as a flagger to let computer know what to do if value was really not in data, and if it wasn't do nothing
        value_found=0
        update_found=0
        
        for i in range(len(self.dictionary)): #used instead of getFieldNumber so I do not have to deal w/ Errors
            
            if self.dictionary[i] == key_field:
                
                indexer = i
                #print(key_field,indexer) to see what intrepreter was doing when I assigned values as desired
                field_found =1
        if field_found != 1 :
            pass
                
        for row in self.rows:
            
            if row[indexer]== key_value:
                #print (key_value) to see if it is in the row
                value_found =1
                
        if value_found != 1:
            pass 

        for j in range(len(self.dictionary)):
            if self.dictionary[j] == update_field:

                jindexer = j
                #print(update_field,jindexer) to see what intrepreter was doing when I assigned values as desired
                update_found = 1
        if update_found != 1 :
            pass

        elif update_found == 1:   
            for row in self.rows:
                if key_field == self.dictionary[indexer] and key_value == row[indexer]:
                    if update_value.find("/") != -1:
                        row[jindexer] = '"' + update_value + '"'
                    else:
                        row[jindexer] = update_value
                    
                    #print(row[jindexer]) to see what intrepreter was doing when I assigned values as desired

        
                    
        
                

        
          


                
                     
                    
                












        
        
        

