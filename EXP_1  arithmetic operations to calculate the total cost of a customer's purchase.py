item_prices = [10, 20, 30]  
quantities = [3, 2, 1]     

discount_rate = 10  
tax_rate = 8        

total_cost_before_discount = sum(item_prices[i] * quantities[i] for i in range(len(item_prices)))


discount_amount = total_cost_before_discount * (discount_rate / 100)


total_cost_after_discount = total_cost_before_discount - discount_amount


tax_amount = total_cost_after_discount * (tax_rate / 100)

total_cost_with_tax = total_cost_after_discount + tax_amount

print(f"Total cost before discount: {total_cost_before_discount:.2f}")
print(f"Total discount: {discount_amount:.2f}")
print(f"Total cost after discount: {total_cost_after_discount:.2f}")
print(f"Total tax amount: {tax_amount:.2f}")
print(f"Total cost with tax: {total_cost_with_tax:.2f}")
