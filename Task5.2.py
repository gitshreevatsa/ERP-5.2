dict = {}
for i in range(2019,2022):   
    Year = i
    print(Year)
    N = int(input("Enter the number of students: "))
    AF1 = int(input("Enter the number of professors: "))
    AF2 = int(input("Enter the number of associate professors: "))
    AF3 = int(input("Enter the number of assistant professors: "))
    RF1 = (1/9)*(N/15)
    RF2 = (2/9)*(N/15)
    RF3 = (6/9)*(N/15)
    dict[Year] = {}
    dict[Year]['Total_Students'] = N
    dict[Year]['professors'] = AF1
    dict[Year]['Associate_professors'] = AF2
    dict[Year]['Assistant_professors'] = AF3
    dict[Year]['Required_professors'] = RF1
    dict[Year]['Required_associate_professors'] = RF2
    dict[Year]['Required_assistant_professors'] = RF3



average_AF1 = (dict[2019]['professors'] + dict[2020]['professors'] + dict[2021]['professors'])/3
average_AF2 = (dict[2019]['Associate_professors'] + dict[2020]['Associate_professors'] + dict[2021]['Associate_professors'])/3
average_AF3 = (dict[2019]['Assistant_professors'] + dict[2020]['Assistant_professors'] + dict[2021]['Assistant_professors'])/3
average_RF1 = (dict[2019]['Required_professors'] + dict[2020]['Required_professors'] + dict[2021]['Required_professors'])/3
average_RF2 = (dict[2019]['Required_associate_professors'] + dict[2020]['Required_associate_professors'] + dict[2021]['Required_associate_professors'])/3
average_RF3 = (dict[2019]['Required_assistant_professors'] + dict[2020]['Required_assistant_professors'] + dict[2021]['Required_assistant_professors'])/3

average_dict = {}
average_dict['a_af1'] = average_AF1
average_dict['a_af2'] = average_AF2
average_dict['a_af3'] = average_AF3
average_dict['a_rf1'] = average_RF1
average_dict['a_rf2'] = average_RF2
average_dict['a_rf3'] = average_RF3

dict['Output'] = average_dict

if(AF1 == AF2 == 0 ):
    Cadre_Ratio_Marks = 0
    print(Cadre_Ratio_Marks + "Marks")
else:
    Cadre_Ratio_Marks = ((average_AF1/average_RF1) + (average_AF2*0.6)/average_RF2 + (average_AF3*0.4)/average_RF3)*12.5
    if (Cadre_Ratio_Marks <= 25):
        print("Cadre Ratio Marks = " + str(Cadre_Ratio_Marks) + "Marks")
    else: 
        Cadre_Ratio_Marks = 25
        print(str(Cadre_Ratio_Marks) + " Marks")
dict['CDR'] = Cadre_Ratio_Marks

print(dict)