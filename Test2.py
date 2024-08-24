lovely_loveseat_description = " Lovely Loveseat. Tufted polyeswter blend on wood. 32 inches high x 30 inches deep. Red or White" 

lovely_loveseat_price = 254.00

stylish_settee_description = "Sytlish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_description = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 56 inches tall. Brown with cream shade."
 
luxurious_lamp_price = 52.15

sales_tax = .088

# First Coustemer 

customer_one_total = 0 

customer_one_itemization = luxurious_lamp_description + "\n" + lovely_loveseat_description

customer_one_total += lovely_loveseat_price + luxurious_lamp_price

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print ('Customer One Iteams:')

print (customer_one_itemization)

print ('\n')

print ('Customer One Total')

print (customer_one_total)

