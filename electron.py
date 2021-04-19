import ooad_classes as ooad

#create_cart

item_list = []

dict = {"R":"Refrigerator", "T":"Television", "A":"Alexa", "G":"Google home mini"}

print()

print("The available items in electronics are: ")

for i in dict.values():
    item_list.append(i)

for i in dict:
    print(i, "-",dict[i])

print()

cust_item_list = []	

n = int(input("Please enter the NUMBER of items you'd like to PURCHASE: "))

for i in range(0, n):
	ele = str(input("	Enter the item name: "))
	
	cust_item_list.append(ele)

l = []

for i in cust_item_list:
    for j in dict:
        if i == j:
            l.append(dict[i])

cust_1 = ooad.create_cart(l)

print()

print("The cart is: {}".format( cust_1.cust_item_list))

#manage_cart

n = int(input("Please enter the NUMBER of items you'd like to REMOVE: "))

managed_list = cust_item_list.copy()

for i in range(0, n):
	ele = str(input("	Enter the item name: "))
	
	managed_list.remove(ele)

ml = []

for i in managed_list:
    for j in dict:
        if i == j:
            ml.append(dict[i])

managed_cust_1 = ooad.manage_cart(ml)

print()

print("The MODIFIED cart is: {}".format( managed_cust_1.managed_list))

#product_recommendation

recommender_list_category_1 = [1, 2]

recommended_product_list = []

for item in managed_cust_1.managed_list:
	
	if item in item_list:
		index = item_list.index(item)
		
		if index in recommender_list_category_1:
			for j in recommender_list_category_1:
				recommended_product_list.append(item_list[j])

cust_1_recommendations = ooad.product_recommendation(recommended_product_list)

print()

print("The recommended products are: {}".format( cust_1_recommendations.recommended_product_list))

ch = input("\nDo you want to continue Shopping?? (Y/y or N/n): ")

if (ch=="Y") or (ch=="y"):
	import first
else:
	print()