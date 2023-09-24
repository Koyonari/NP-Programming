#An Yong Shyan, S10258126B

#Thought process:
#1. Define calculate_charge function
#2. Define calculate_gst function
#3. Prompt user for number of pages

#Code

#Define functions
def calculate_charge(pages: int):
    if pages <= 100:
        charge = 0.03 * pages
    elif pages <= 300 and pages > 100:
        charge = 0.03 * 100 + 0.02 * (pages - 100)
    else:
        charge = 0.03 * 100 + 0.02 * 200 + 0.01 * (pages - 300)

    return charge

def calculate_gst(charge: float):
    gst = 1.07 * charge
    return gst

#Prompt user for number of pages
pages = int(input("Enter number of pages: "))

#For loop to print
print("{:10} {:>10} {:>20}".format("Pages", "Charge($)", "Include gst($)"))
for pages in range(0, pages+1, 50):
    charge = calculate_charge(pages)
    inc_gst = calculate_gst(charge)

    print("{:<10} {:10.2f} {:20.2f}".format(pages, charge, inc_gst))