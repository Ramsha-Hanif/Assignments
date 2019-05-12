sindhi = int(input('Enter Marks Obtain in Sindhi (out of 75): '))
urdu = int(input('Enter Marks Obtain in Urdu (out of 75): '))
english1 = int(input('Enter Marks Obtain in English Paper 1 (out of 75): '))
english2 = int(input('Enter Marks Obtain in English Paper 2 (out of 75): '))
pakstd = int(input('Enter Mark Obtain in Pakistan Studies (out of 75): '))
islamiat = int(input('Enter Mark Obtain in Islamiat (out of 75): '))
maths = int(input('Enter Mark Obtain in Mathematics (out of 100): '))
biologyTh = int(input('Enter Mark Obtain in Biology/Computer Studies Theory (out of 75): '))
biologyPr = int(input('Enter Mark Obtain in Biology/Computer Studies Practical (out of 25): '))
chemistryTh = int(input('Enter Mark Obtain in Chemistry Theory (out of 85): '))
chemistryPr = int(input('Enter Mark Obtain in Chemistry Practical (out of 15): '))
PhysicsTh = int(input('Enter Mark Obtain in Physics Theory (out of 85): '))
PhysicsPr = int(input('Enter Mark Obtain in Physics Practical (out of 15): '))
grade =''

print('\n\t\t\t\tSTATEMENT OF MARKS')

print('SUBJECT\t\t\tMAX MARKS\t MINPASS MARKS\t MARKS OBTAIN\t STATUS')
if sindhi >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('SINDHI SALEES\t\t\t  075\t\t      025\t\t '+str(sindhi)+'\t  '+status)
if urdu >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('URDU NORMAL\t\t\t  075\t\t      025\t\t '+str(urdu)+'\t  '+status)
if english1 >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('ENGLISH PAPER 1\t\t\t  075\t\t      025\t\t '+str(english1)+'\t  '+status)
if english2 >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('ENGLISH PAPER 2\t\t\t  075\t\t      025\t\t '+str(english2)+'\t  '+status)
if pakstd >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('PAKISTAN STUDIES\t  075\t\t      025\t\t '+str(pakstd)+'\t  '+status)
if biologyTh >= 28:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('BIOLOGY/COMPUTER STUDIES THEORY\t\t  085\t\t      028\t\t '+str(biologyTh)+'\t  '+status)
if biologyPr >= 5:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('BIOLOGY/COMPUTER STUDIES PRACTICAL\t  015\t\t      005\t\t '+str(biologyPr)+'\t  '+status)
if chemistryTh >= 28:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('CHEMISTRY THEORY\t  085\t\t      025\t\t '+str(chemistryTh)+'\t  '+status)

if chemistryPr >= 5:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('CHEMISTRY PRACTICAL\t  015\t\t      005\t\t '+str(chemistryPr)+'\t  '+status)

totalMarksObt = sindhi + english1 + pakstd + biologyPr + biologyTh + chemistryPr + chemistryTh
percentageTotal = totalMarksObt / 425 * 100

if grade != 'F':
    if percentageTotal >= 80:
        grade = 'A+'
    elif (percentageTotal < 80 and percentageTotal >= 70):
        grade = 'A'
    elif (percentageTotal < 70 and percentageTotal >= 60):
        grade = 'B'
    elif (percentageTotal < 60 and percentageTotal >= 50):
        grade = 'C'
    elif (percentageTotal < 50 and percentageTotal >= 40):
        grade = 'D'
    elif (percentageTotal > 40):
        grade = 'E'

print('\n\nTOTAL MARKS OBTAIN   '+str(totalMarksObt)+'   OUT OF 425')
print('PERCENTAGE: '+str(round(percentageTotal,2))+'%')
print('GRADE: '+grade+'\n')