onroad_price=1753690
down_payment=160000
bank_intrest_rate=9/100
loan_period_years=5
loan_amount=onroad_price-down_payment
loan_period_months=loan_period_years*12

monthly_emi=bank_intrest_rate/12

x=(1+monthly_emi)**loan_period_months
y=loan_amount*monthly_emi*x
z=x-1
emi=y/z

total_payable=emi*loan_period_months

print(f"loan amount:{loan_amount}")
print(f"emi per month:{emi}")
print(f"payable amount:{total_payable}")
