import sys

#Fatih OTER
#2210356119
#assignment3

#I write i/o functions
f = open(sys.argv[1], "r")
f2 = open("output.txt", "w")
dict = {}
letters = ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
           "X", "Y", "Z"]

#I start a for loop
for i in f:
    if (i.endswith("\n")):
        i = i[:-1]
    if (i.startswith("CREATECATEGORY")):   #if lines startswith "CREATECATEGORY" code create the category of stadium
        i = i[15:]
        categoryname, rows_columns = i.split(" ")
        a = []
        a.append(categoryname)
        a.append(rows_columns)
        rows, columns = a[1].split("x")
        a.append(rows)
        a.append(columns)
        a.remove(rows_columns)

        matrix = [["X" for x in range(int(a[2]))] for x in range (int(a[1]))]


        if categoryname in dict.keys():
            f2.write("Warning: Cannot create the category for the second time. The stadium has already " + categoryname+"\n")
        else:
            dict[categoryname] = matrix
            f2.write(
                "The category '" + categoryname + "' having " + str(int(a[1]) * int(a[2])) + " seats has been created"+"\n")

    elif (i.startswith("SELLTICKET")):  #if lines startswith "SELLTICKET" code sells the ticket(s) in the category.

            i = i[11:]
            b = []
            b = i.split(" ")

            customer_name = b[0]
            typeofticket = b[1]
            category_name = b[2]
            seats = b[3:]
            for seat in seats:
                try:
                    if "-" not in seat:
                        nameofrow = seat[0]
                        numberofseat = int(seat[1:])
                        matrix2 = dict[category_name]
                        rowNumber = len(matrix2[0])
                        columnNumber = len(matrix2)
                        b = -1
                        z = 0
                        for k in letters:
                            if letters[z] == nameofrow:
                                b = z
                            z += 1
                        if (numberofseat>=rowNumber):
                            f2.write("Error: The category '"+category_name+ "' has less column than the specified index", seat+"!"+"\n")
                            raise Exception("sa")

                        elif (b>=columnNumber):
                            f2.write("Error: The category '"+category_name+"' has less row than the specified index", seat+"!"+"\n")
                            raise Exception("sa")

                        if dict[category_name][b][numberofseat] == "X":
                            if typeofticket == "student":
                                dict[category_name][b][numberofseat] = "S"
                            elif typeofticket == "full":
                                dict[category_name][b][numberofseat] = "F"
                            elif typeofticket == "season":
                                dict[category_name][b][numberofseat] = "T"
                            f2.write("Success: " + customer_name + " has bought " + seat + " at " + category_name+"\n")
                        else:
                            f2.write(
                                "Warning: The seat " + seat + " cannot be sold to " + customer_name + " since it was already sold"+"\n")

                    elif "-" in seat:
                        fromseat, toseat = seat.split("-")
                        toseat = int(toseat)
                        nameofrow = fromseat[0]
                        numberofseat = int(fromseat[1:])
                        matrix4 = dict[category_name]
                        rowNumber = len(matrix4[0])
                        columnNumber = len(matrix4)
                        b = 0
                        z = 0
                        for k in letters:
                            if letters[z] == nameofrow:
                                b = z
                            z += 1
                        if (toseat >= rowNumber):
                            f2.write("Error: The category '"+ category_name+ "' has less column than the specified index "+ seat+"!"+"\n")
                            raise Exception("sa")

                        elif (b >= columnNumber):
                            f2.write("Error: The category '"+category_name+ "' has less row than the specified index "+ seat+"!"+"\n")
                            raise Exception("sa")
                        if dict[category_name][b][numberofseat] == "X":
                            if typeofticket == "student":
                                dict[category_name][b][int(numberofseat):int(int(toseat) + 1)] = "S" * (
                                            (int(toseat)) - (int(numberofseat)) + 1)
                            elif typeofticket == "full":
                                dict[category_name][b][int(numberofseat):int(toseat) + 1] = "F" * (
                                            (int(toseat)) - (int(numberofseat)) + 1)
                            elif typeofticket == "season":
                                dict[category_name][b][int(numberofseat):int(toseat) + 1] = "T" * (
                                            (int(toseat)) - (int(numberofseat)) + 1)
                            f2.write("Success: " + customer_name + " has bought " + seat + " at " + category_name+"\n")
                        else:
                            f2.write(
                                "Warning: The seats " + seat + " cannot be sold to " + customer_name + " due some of them have already been sold"+"\n")
                except:
                    aasd = 6

    elif(i.startswith("CANCELTICKET")):  #if lines startswith "CANCELTICKET" code canceled the ticket(s) in the category.
        i = i[13:]
        b = []
        b = i.split(" ")

        category_name = b[0]
        seats = b[1:]
        for seat in seats:
            try:
                nameofrow = seat[0]
                numberofseat = int(seat[1:])
                matrix2 = dict[category_name]
                rowNumber = len(matrix2[0])
                columnNumber = len(matrix2)
                b = -1
                z = 0
                for k in letters:
                    if letters[z] == nameofrow:
                        b = z
                    z += 1
                if (numberofseat >= rowNumber):
                    f2.write("Error: The category '" + category_name + "' has less column than the specified index "+ seat + "!"+"\n")
                    raise Exception("sa")

                elif (b >= columnNumber):
                    f2.write("Error: The category '" + category_name + "' has less row than the specified index "+ seat + "!"+"\n")
                    raise Exception("sa")
                if dict[category_name][b][numberofseat] != "X":
                    dict[category_name][b][numberofseat] = "X"
                    f2.write("Success: The seat " + seat + " at '" + category_name + "' has been canceled and now ready to sell again"+"\n")
                else:
                    f2.write("Error: The seat " + seat + " at " + category_name + "  has already been free! Nothing to cancel"+"\n")
            except:
                aasd = 6

    elif(i.startswith("BALANCE")): #if lines startswith "BALANCE" code balances revenue of the category.
        i = i[8:]
        category_name = i
        matrix2 = dict[category_name]
        seasonTicketNumber = 0
        studentTicketNumber = 0
        fullTicketNumber = 0
        for l in matrix2:
            for j in l:
                if j == "S":
                    studentTicketNumber +=1
                elif j =="T":
                    seasonTicketNumber +=1
                elif j =="F":
                    fullTicketNumber +=1
        revenues = studentTicketNumber*10 + fullTicketNumber*20 + seasonTicketNumber*250
        f2.write("Sum of students = "+ str(studentTicketNumber)+", Sum of full pay = "+ str(fullTicketNumber) +", Sum of season ticket = "+
              str(seasonTicketNumber)+", and Revenues = "+str(revenues)+" Dollars"+"\n")


    elif(i.startswith("SHOWCATEGORY")):  #if lines startswith "SHOWCATEGORY" code shows the category.
        i = i[13:]
        category_name = i
        matrix2 = dict[category_name]
        f2.write("Printing category layout of "+category_name+"\n")
        sizeOfMatrix2 = len(matrix2)

        lenghtOfMatrix2 = len(matrix2) -1
        while (lenghtOfMatrix2>=0):
            f2.write(letters[sizeOfMatrix2-1]+" ")
            l = matrix2[lenghtOfMatrix2]
            for j in l:
                f2.write(j+"  ")
            f2.write("\n")
            sizeOfMatrix2 -= 1
            lenghtOfMatrix2-=1
        list = matrix2[0]


        f2.write("  ")
        for i in range(len(list)):
            if len(str(i))==1:
                f2.write(str(i)+"  ")
            elif len(str(i))==2:
                f2.write(str(i)+" ")
        f2.write("\n")

        f2.write("category report of '" + category_name + "'\n")
        f2.write("--------------------------------\n")

