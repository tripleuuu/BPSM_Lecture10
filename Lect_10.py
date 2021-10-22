#Programme for E1
con1="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A1=con1.count("A")
A2=con1.count("T")
A3=A1+A2


#Programme for E2
con2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
R1=con2.replace("A","t")
R2=R1.replace("T","a")
R3=R2.replace("G","c")
R4=R3.replace("C","g")
Com1=R4.upper()
print(Com1)

#Programme for E3
con3="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print(con3.count("GAATTC"))

#Q1
pos1=con3.find("GAATTC")
print(pos1)

#Q2
cutpos=pos1+1
print("The position of the cut is "+ str(cutpos))

#Q3
print("The length of second fragment is "+ str(len(con3[cutpos:])))

#Programme for E4
con4_1="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCT"
con4_2="ACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCT"
con4_3="ATCATCGATCGATATCGATGCATCGACTACTAT"
con4=con4_1+con4_2+con4_3

#to check its length
print("The length of the sequence is "+ str(len(con4)))

#Q1
exon1=con4[:63]
exon2=con4[90:]


