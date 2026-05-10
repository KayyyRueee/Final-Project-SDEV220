#build a dictionary

interaction = {("Warfarin", "Ibuprofen"): ("DANGEROUS", "Risk: Major bleeding (GI bleeding especially) because both affect clotting. ") , #0
               ("Lisinopril", "Aleve"): ("DANGEROUS", "Risk: Kidney damage and reduced blood pressure control (“triple whammy” if a diuretic is also involved). ") , #1
               ("Digoxin", "Tums"): ("DANGEROUS", "Risk: Reduced absorption of digoxin → decreased effectiveness; can destabilize heart rhythm control. ") , #2
               ("Sertraline", "Robitussin DM"): ("DANGEROUS", "Risk: Serotonin syndrome (confusion, agitation, sweating, tremor). ") , #3
               ("Furosemide", "Dulcolax"): ("DANGEROUS", "Risk: Severe electrolyte imbalance (low potassium), dehydration, arrhythmias. ") , #4
               ("Lorazepam", "Benadryl"):( "DANGEROUS", "Risk: Excess sedation, confusion, falls, respiratory depression (especially dangerous in elderly patients). ") , #5
               ("Warfarin", "Tylenol"): ("Safe", "Lower bleeding risk than ibuprofen or naproxen. ") , #6
               ("Lisinopril", "Aspercreme Lidocaine"): ("Safe", "Avoids NSAID kidney interaction risk. ") , #7
               ("Digoxin", "Pepcid AC"): ("Safe", "Lower interaction risk than calcium carbonate antacids. ") ,  #8
               ("Sertraline", "Mucinex"): ("Safe", "Does not contain dextromethorphan. ") , #9
               ("Furosemide", "Metamucil"): ("Safe", "Lower dehydration and potassium-loss risk. ") , #10
               ("Lorazepam", "Claritin"): ("Safe", "Less sedating than diphenhydramine. ") , #11            
}

#I wanted to provide the brand name as well as specific drug that causes it to be dangerous or safe.
#I also provided a generic/cheaper alternative for the safe medications.

med_info = {
    "Ibuprofen": "(Advil/Motrin)", #0
    "Aleve": "(Naproxen Arthritis medications)", #1
    "Tums": "(Calcium carbonate Heartburn medications)", #2
    "Robitussin DM": "(Dextromethorphan Cough medications)", #3
    "Dulcolax": "(Bisacodyl Laxative medications)", #4
    "Benadryl": "(Diphenhydramine allergy medications)", #5
    "Tylenol": "(Cheaper alternative:Acetaminophen )", #6
    "Aspercreme Lidocaine": "(Cheaper alternative: Lidocaine Topical (or other topical pain relievers))", #7
    "Pepcid AC": "(Cheaper alternative: Famotidine)", #8
    "Mucinex": "(Cheaper alternative: Guaifenesin)", #9
    "Metamucil": "(Cheaper alternative: Psyllium Husk)", #10
    "Claritin": "(Cheaper alternative: Loratadine)" #11
}

#now build a function that checks for interactions and provides the appropriate message.
def check_interaction(med1, med2): #takes in two medications and checks for interactions
    key = (med1, med2)         #create a tuple key for the interaction dictionary
    if key in interaction:     #check if the key exists in the interaction dictionary
        severity, message = interaction[key]    #if it does, unpack the severity and message
        return f"Interaction between {med1} and {med2}: {severity}. {message}"      #returns a formatted message for the user, it displays the 2 medications, whether its safe or not and the explation text
    else:
        return f"No known interaction between {med1} and {med2}."

print("What syptoms is your client experiencing?") #asks the user for the symptoms their client is experiencing
print("1. Pain")
print("2. Cough")
print("3. Heartburn")
print("4. Allergies")
print("5. Constipation")
symptom_choice = input("Enter the number corresponding to the symptom: ") #takes in the user's choice of symptom
print("What OTC med are you suggesting?") #asks the user for the medications their client is taking
med2 = input("Enter OTC medication: ")

def run_checker(med2): #takes in the OTC medication and the symptom choice to run the checker
    safe_alternative = None  #creates a variable to store the safe alternative medication

    for med_pair in interaction:   #the beginning of the loop, we created med_pair to represent the key in the interaction dictionary, which is a tuple of two medications.

        # DANGEROUS interaction
        if med2 in med_pair and interaction[med_pair][0] == "DANGEROUS":

            med1 = med_pair[0]     #saves the frist med in the pair as med1 & med 1 is the prescription medication that is being taken by the client
                                 #med2 is the OTC medication that the user is suggesting
            print(f"{med1} + {med2} {med_info.get(med2, '')} :")  #prints the 2 meds, then looks up th OTC med info on why its bed 
            print("DANGEROUS!!!")
            print(interaction[med_pair][1]) #prints the RISK
            print()

            # find SAFE alternative using same prescription med
            for safe_pair in interaction:

                if safe_pair[0] == med1 and interaction[safe_pair][0] == "Safe":   #Double check if its safe

                    safe_alternative = safe_pair[1]  #saves ths safe OTC med as the safe alternative

                    print("Safer alternative:")
                    print(f"{safe_alternative}")

                    print(f"{med1} + {safe_alternative} : Safe!")

                    print(f"{safe_alternative} has {interaction[safe_pair][1]}")
                    print(med_info.get(safe_alternative, ''))

                    break

            break