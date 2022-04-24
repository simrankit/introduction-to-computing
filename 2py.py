gross_income=int(input("enter gross income"))
dependent=int(input("number of dependent"))
tax_income=gross_income-10000-(dependent*3000)
tax=tax_income*0.2
print(tax)
