from fractions import Fraction
def probability(b):
    global p2
    p=b[1]*100000*Fraction((b[3]))
    p1=(100000-p)*(1-b[1])
    p2=p/(p+p1)
    p2=round(100*p2,2)
    return p2
#defining the functions this part.
def list():
    f2.write('''Patient  Diagnosis   Disease          Disease    Treatment         Treatment
Name     Accurancy   Name             Incidence  Name              Risk\n''')
    f2.write("-----------------------------------------------------------------------------\n")
    for i in a:
        f2.write(i[0]+" "*(8-len(i[0]))+"%"+f'{100*i[1]:.2f}'+" "*(3)+i[2]+" "*(15-len(str(i[2])))+i[3]+
              " "*(10-len(i[3]))+i[4]+" "*(16-len(i[4]))+"%"+str(100*i[5])+" "*(7-len(str((i[5]))))+"\n")

f = open("doctors_aid_inputs.txt","r")
f2 = open("doctors_aid_outputs.txt","w")

a=[]
#adding the names to the list one by one with a loop
for i in f:
    if (i.endswith("\n")):
        i = i[:-1]
    if (i.startswith("create")):
        thereIsDuplication = 0
        i = i[7:]
        name, diagnosisAccurancy, diseaseName, diseaseIncidence, treatmentName, treatmentRisk = i.split(", ")
        for z in a:
            if (z[0] == name):
                f2.write("Patient " + str(z[0]) + " cannot be recorded due to duplication.\n")
                thereIsDuplication = 1
        if (thereIsDuplication == 0):
            b = []
            b.append(name)
            b.append(float(diagnosisAccurancy))
            b.append(diseaseName)
            b.append(diseaseIncidence)
            b.append(treatmentName)
            b.append(float(treatmentRisk))
            a.append(b)
            f2.write("Patient " + str(b[0]) + " is recorded.\n")
#removing the names to the list one by one with a loop which have elif block thats investigate that.
    elif (i.startswith("remove")):
        i = i[7:]
        removed = 0
        for k in a:
            if k[0] == i:
                a.remove(k)
                f2.write("Patient " + str(i) + " is removed.\n")
                removed = 1

        if (removed == 0):
            f2.write("Patient " + str(i) + " cannot be removed due to absence.\n")

#we calculate probability using information from text document
    elif (i.startswith("probability")):
        i = i[12:]
        found = 0
        for j in a:
            if j[0] == i:
                f2.write("Patient " + (j[0]) + " has a probability of " + str(probability(j)) + "% " + "of having " + j[2]+"."+"\n")
                found = 1

        if (found == 0):
            f2.write("Probability for " + str(i) + " cannot be calculated due to absence.\n")

    elif (i == "list"):
        list()
#we calculate recommendation using information from text document
    elif (i.startswith("recommendation")):
        i = i[15:]
        found = 0
        for j in a:
            if j[0] == i:
                probabilityValue = probability(j)
                found = 1
                if (probabilityValue >= (j[5]*100)):
                    f2.write("System suggests " + i + " to have the treatment.\n")
                else:
                    f2.write("System suggests " + i + " NOT to have the treatment.\n")

        if (found == 0):
            f2.write("Recommendation for " + str(i) + " cannot be calculated due to absence.\n")
f.close()
f2.close()

#Fatih ÖTER 2210356119