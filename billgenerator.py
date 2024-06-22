
itemp={'Soap':30,'Rice':50,'oil':175,'Bread':26.5,'Jam':20}
ordered_item=[]
item={1:'Soap',2:'Rice',3:'Oil',4:'Bread',5:'Jam'}
i=0
print('List of items')
print('1.Soap-Rs.30\n2.Rice-Rs.50\n3.Oil-Rs.175')
print('4.Bread-Rs.26.5\n5.Jam-Rs.20\n6.Exit')

#choices
print("Enter your choice 1 to 5 for purchase 6 for exit")
t=int(input())
while((t>=1)and(t<=5)):
    i=i+1
    print("Number of Quantity required")
    n=int(input()) #number of items quantity
    
    t1=item[t] #extracts the items name from the above
    t2=itemp[t1] #extracts price of an item
    total_amount=n*t2
    
    ordered_item=ordered_item+[item[t],itemp[t1],n,total_amount]
    print("List of items")
    print('1.Soap-Rs.30\n2.Rice-Rs.50\n3.Oil-Rs.175')
    print('4.Bread-Rs.26.5\n5.Jam-Rs.20\n6.Exit')
    
    t=int(input())
    
    print("Retail Bill System")
    print("...............................................")
    print("Name\t Price\t    Quantity\t Total")
    print("...............................................")
    ct=0 #cumulative total
    ind=0 # adding the list variable(index)
    
    for x in range(i):
        print("%s\t%0.2f\t\t%d\t\t%0.2f" %(ordered_item[ind],ordered_item[ind+1],ordered_item[ind+2],ordered_item[ind+3]))
        total_amount=total_amount+ordered_item[ind+3]
        ind=ind+4
    print("................................................")
    print("Total Amount %0.2f" %total_amount)