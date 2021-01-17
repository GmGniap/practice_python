'''
def computepay(h,r):
    if h > 40:
        e = h - 40
        pay = (40*r)+(e*r*1.5)
    else:
        pay = (h * r)
    return pay

hrs = input("Enter Hours:")
rate = input("Rate:")
p = computepay(float(hrs),float(rate))
print("Pay",p)
'''

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)