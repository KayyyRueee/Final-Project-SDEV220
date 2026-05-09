# build a dictionary
interaction = {
    ("Warfarin", "Ibuprofen"): ("DANGEROUS", "Risk: Major bleeding (GI bleeding especially) because both affect clotting."),
    ("Lisinopril", "Aleve"): ("DANGEROUS", "Risk: Kidney damage and reduced blood pressure control."),
    ("Digoxin", "Tums"): ("DANGEROUS", "Risk: Reduced absorption of digoxin."),
    ("Sertraline", "Robitussin DM"): ("DANGEROUS", "Risk: Serotonin syndrome."),
    ("Furosemide", "Dulcolax"): ("DANGEROUS", "Risk: Electrolyte imbalance."),
    ("Lorazepam", "Benadryl"): ("DANGEROUS", "Risk: Excess sedation."),
    ("Warfarin", "Tylenol"): ("Safe", "Lower bleeding risk than ibuprofen."),
    ("Lisinopril", "Aspercreme Lidocaine"): ("Safe", "Avoids NSAID kidney risk."),
    ("Digoxin", "Pepcid AC"): ("Safe", "Lower interaction risk."),
    ("Sertraline", "Mucinex"): ("Safe", "Does not contain dextromethorphan."),
    ("Furosemide", "Metamucil"): ("Safe", "Lower dehydration risk."),
    ("Lorazepam", "Claritin"): ("Safe", "Less sedating.")
}

med_info = {
    "Ibuprofen": "(Advil/Motrin)",
    "Aleve": "(Naproxen Arthritis medications)",
    "Tums": "(Calcium carbonate Heartburn medications)",
    "Robitussin DM": "(Dextromethorphan Cough medications)",
    "Dulcolax": "(Bisacodyl Laxative medications)",
    "Benadryl": "(Diphenhydramine allergy medications)",
    "Tylenol": "(Cheaper alternative: Acetaminophen)",
    "Aspercreme Lidocaine": "(Cheaper alternative: Lidocaine topical)",
    "Pepcid AC": "(Cheaper alternative: Famotidine)",
    "Mucinex": "(Cheaper alternative: Guaifenesin)",
    "Metamucil": "(Cheaper alternative: Psyllium Husk)",
    "Claritin": "(Cheaper alternative: Loratadine)"
}


def run_checker(med2):

    result = ""

    for med_pair in interaction:

        if med2 in med_pair and interaction[med_pair][0] == "DANGEROUS":

            med1 = med_pair[0]

            result += f"{med1} + {med2} {med_info.get(med2,'')}:\n"
            result += "DANGEROUS!!!\n"
            result += interaction[med_pair][1] + "\n\n"

            # find safe alternative
            for safe_pair in interaction:

                if safe_pair[0] == med1 and interaction[safe_pair][0] == "Safe":

                    safe_med = safe_pair[1]

                    result += "Safer alternative:\n"
                    result += f"{safe_med}\n"
                    result += f"{med1} + {safe_med} : Safe!\n"
                    result += interaction[safe_pair][1] + "\n"
                    result += med_info.get(safe_med, "")

                    return result

    return "No known interaction found."