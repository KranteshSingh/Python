high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print('Eligible')
else:
    print('Not Eligible')

if not student:
    print('Eligible')
else:
    print('Not Eligible')


if high_income and good_credit and not student:
    print("Eligible")
else:
    print('Not Eligible')
