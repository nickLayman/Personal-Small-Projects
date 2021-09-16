def tax(x):
  print"Social Security= $" + str(round(x*.062)/100) #rounds to cents of calculated tax then converts back to dollars and saves as string in order to concatenate
  print"Medicare Employee= $" + str(round(x*.0145)/100)
  print"Illinois Withholdings= $" + str(round(x*.0375)/100)
  print"Total Taxes= $" + str(round(x*.114)/100)
  print"Net Pay= $" + str(round(x*.886)/100)
H=float(input("Hours Worked="))
R=float(input("Hourly Rate=$"))
print round((H*R)*100)/100
x=int(float(input("Gross Pay?"))*100) #converts floating point dollars to integer cents
tax(x)