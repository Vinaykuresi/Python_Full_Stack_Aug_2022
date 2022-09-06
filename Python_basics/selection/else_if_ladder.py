person_name = "Vinay"
passport_Status = "Valid"

airline_laguage_limit = 15

peron_laguage_weight = 25

extra_laguage_charge = 0

# else-if ladder
if(passport_Status == "Valid"):
    # nested if
    if(peron_laguage_weight <= 15):
        pass # nothing to do
    elif(peron_laguage_weight > 15 and peron_laguage_weight <= 30):
        extra_laguage_charge = (peron_laguage_weight - airline_laguage_limit) * 250
    else:
        extra_laguage_charge = (peron_laguage_weight - airline_laguage_limit) * 500
else:
    print("Airport secuirty not cleared for : ", person_name)

if(extra_laguage_charge > 0):
    print("The extra lagauge charge for person : ", person_name, " is : ", extra_laguage_charge)
else:
    print("No laguage charge for : ", person_name)

    

