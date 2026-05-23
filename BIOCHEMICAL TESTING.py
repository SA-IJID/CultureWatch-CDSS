# PHASE 3: BACTERIAL BIOCHEMICAL IDENTIFICATION
# Based on CLSI (Clinical and Laboratory Standards Institute) protocols

import sys  # Importing the sys module to allow for program exit functionality.

# Display phase title
print("\n--- PHASE 3: BACTERIAL BIOCHEMICAL IDENTIFICATION ---")
print("Enter biochemical test results using the allowed options below (yes/no for each test).\n")

# Function to get yes/no input


def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to test Gram-positive cocci


def test_gram_positive_cocci(cell_arrangement):
    print("\n--- GRAM-POSITIVE COCCI IDENTIFICATION ---")
    print("CLSI Protocol: Primary tests include Catalase, Coagulase, PYR, and Optochin.\n")

    catalase = get_yes_no_input("Catalase test positive? (yes/no): ")

    if catalase:
        # Staphylococcus species
        print("\n>>> Preliminary identification: Staphylococcus spp. (Catalase positive)")
        coagulase = get_yes_no_input("Coagulase test positive? (yes/no): ")

        if coagulase:
            print("\nConfirmed identification: Staphylococcus aureus")
            print("Key characteristics: Catalase+, Coagulase+, Oxidase-, Gram+ clusters")
            print(
                "Recommended antibiotics: Beta-lactamase-stable penicillins, Cephalosporins, Vancomycin")
        else:
            print("\nConfirmed identification: Coagulase-Negative Staphylococcus (CoNS)")
            print("   - Common species: S. epidermidis, S. saprophyticus, S. hominis")
            print("Key characteristics: Catalase+, Coagulase-, Oxidase-, Gram+ clusters")
            print("Recommended antibiotics: Cephalosporins, Vancomycin, Linezolid")
    else:
        # Streptococcus/Enterococcus species
        print("\n>>> Preliminary identification: Streptococcus spp. or Enterococcus spp. (Catalase negative)")

        pyr = get_yes_no_input("PYR test positive? (yes/no): ")

        if pyr:
            print("\nConfirmed identification: Enterococcus spp.")
            print("Key characteristics: Catalase-, PYR+, Gram+ pairs/chains")
            print("Common species: E. faecalis, E. faecium")
            print("Recommended antibiotics: Ampicillin, Penicillin G, Vancomycin")
        else:
            optochin = get_yes_no_input("Optochin test positive? (yes/no): ")

            if optochin:
                print("\nConfirmed identification: Streptococcus pneumoniae")
                print("Key characteristics: Catalase-, PYR-, Optochin+, Alpha-hemolytic")
                print(
                    "Recommended antibiotics: Penicillin G, Cephalosporins, Vancomycin, Fluoroquinolones")
            else:
                bile_esculin = get_yes_no_input(
                    "Bile-esculin test positive? (yes/no): ")

                if bile_esculin:
                    print(
                        "\nConfirmed identification: Group D Streptococcus (not Enterococcus)")
                    print("Likely species: S. bovis or S. gallolyticus")
                    print("Key characteristics: Catalase-, PYR-, Bile-esculin+")
                    print("Recommended antibiotics: Penicillin G, Cephalosporins")
                else:
                    print("\nConfirmed identification: Beta-hemolytic Streptococcus")
                    print(
                        "Likely species: Group A (S. pyogenes) or Group B (S. agalactiae)")

                    bacitracin = get_yes_no_input(
                        "Bacitracin test positive? (yes/no): ")
                    if bacitracin:
                        print(
                            "\n   >>> Streptococcus pyogenes (Group A Streptococcus)")
                        print(
                            "Key characteristics: Beta-hemolytic, Catalase-, Bacitracin+")
                    else:
                        print(
                            "\n   >>> Streptococcus agalactiae (Group B Streptococcus)")
                        print(
                            "Key characteristics: Beta-hemolytic, Catalase-, Bacitracin-")

                    print(
                        "Recommended antibiotics: Penicillin G, Cephalosporins, Macrolides")

# Function to test Gram-positive bacilli


def test_gram_positive_bacilli(cell_arrangement):
    print("\n--- GRAM-POSITIVE BACILLI IDENTIFICATION ---")
    print("CLSI Protocol: Primary tests include Catalase, Motility, Gram stain appearance.\n")

    catalase = get_yes_no_input("Catalase test positive? (yes/no): ")

    if catalase:
        # Bacillus species
        print("\n>>> Preliminary identification: Bacillus spp. (Catalase positive)")
        motility = get_yes_no_input("Motility positive? (yes/no): ")

        if motility:
            print(
                "\nConfirmed identification: Bacillus subtilis (or other motile Bacillus species)")
            print("Key characteristics: Catalase+, Motile, Gram+ rods, spore-forming")
            print("Clinical significance: Opportunistic pathogen")
            print("Recommended antibiotics: Penicillin G, Cephalosporins, Vancomycin")
        else:
            print(
                "\nConfirmed identification: Bacillus anthracis or B. cereus (non-motile)")
            print("Key characteristics: Catalase+, Non-motile, Gram+ rods")
            print(
                "Clinical significance: B. anthracis (bioterrorism agent), B. cereus (foodborne)")
            print("Recommended antibiotics: Penicillin G, Ciprofloxacin, Vancomycin")
    else:
        # Listeria or Corynebacterium
        print("\n>>> Preliminary identification: Listeria monocytogenes or Corynebacterium spp.")

        motility = get_yes_no_input(
            "Motility positive at room temperature (25°C)? (yes/no): ")

        if motility:
            print("\nConfirmed identification: Listeria monocytogenes")
            print(
                "Key characteristics: Catalase-, Motile (tumbling at 25°C), Gram+ short rods")
            print(
                "Clinical significance: Food-borne pathogen, especially in immunocompromised")
            print("Recommended antibiotics: Ampicillin, Penicillin G, TMP-SMX")
        else:
            print("\nConfirmed identification: Corynebacterium spp.")
            print("Common species: C. diphtheriae, C. jeikeium, C. aurantiacum")
            print(
                "Key characteristics: Catalase-, Non-motile, Gram+ with Chinese letter arrangement")

            fermentation = get_yes_no_input(
                "Glucose fermentation positive? (yes/no): ")
            if fermentation:
                print("   >>> Likely Corynebacterium diphtheriae")
                print("Clinical significance: Diphtheria toxin producer")

            print(
                "Recommended antibiotics: Erythromycin, Penicillin, Vancomycin, Ciprofloxacin")

# Function to test Gram-negative cocci


def test_gram_negative_cocci():
    print("\n--- GRAM-NEGATIVE COCCI IDENTIFICATION ---")
    print("CLSI Protocol: Primary tests include Oxidase, Glucose fermentation, Maltose fermentation.\n")

    oxidase = get_yes_no_input("Oxidase test positive? (yes/no): ")

    if oxidase:
        # Neisseria species
        print("\n>>> Preliminary identification: Neisseria spp. (Oxidase positive)")
        glucose = get_yes_no_input("Glucose fermentation positive? (yes/no): ")

        if glucose:
            maltose = get_yes_no_input(
                "Maltose fermentation positive? (yes/no): ")

            if maltose:
                print("\nConfirmed identification: Neisseria meningitidis")
                print(
                    "Key characteristics: Oxidase+, Gram- diplococci, Glucose+, Maltose+")
                print("Clinical significance: Meningitis, septicemia, meningococcemia")
                print(
                    "Recommended antibiotics: Cephalosporins (3rd gen), Penicillin G, Ciprofloxacin")
            else:
                print("\nConfirmed identification: Neisseria gonorrhoeae")
                print("Key characteristics: Oxidase+, Gram- diplococci, Glucose+ only")
                print("Clinical significance: Gonorrhea, PID, urethritis")
                print(
                    "Recommended antibiotics: Cephalosporins, Azithromycin, Fluoroquinolones")
    else:
        # Moraxella catarrhalis
        print("\nConfirmed identification: Moraxella catarrhalis")
        print("Key characteristics: Oxidase-, Gram- diplococci, Catalase+, Nitrate+")
        print("Clinical significance: Respiratory pathogen, otitis media, sinusitis")
        print("Recommended antibiotics: Beta-lactamase inhibitor combinations, Fluoroquinolones, Macrolides")

# Function to test Gram-negative bacilli


def test_gram_negative_bacilli(cell_arrangement):
    print("\n--- GRAM-NEGATIVE BACILLI IDENTIFICATION ---")
    print("CLSI Protocol: Primary tests include Oxidase, Glucose fermentation, Lactose fermentation.\n")

    oxidase = get_yes_no_input("Oxidase test positive? (yes/no): ")

    if oxidase:
        # Pseudomonas or other non-fermenter
        print("\n>>> Preliminary identification: Non-fermenting Gram-negative bacillus (Oxidase positive)")
        motility = get_yes_no_input("Motility positive? (yes/no): ")

        if motility:
            print("\nConfirmed identification: Pseudomonas aeruginosa")
            print("Key characteristics: Oxidase+, Gram- rods, Motile, Non-fermenter")
            print(
                "Clinical significance: Nosocomial infections, wound infections, respiratory")
            print(
                "Recommended antibiotics: Antipseudomonal beta-lactams, Fluoroquinolones, Aminoglycosides")
        else:
            print(
                "\nConfirmed identification: Acinetobacter baumannii or other Acinetobacter spp.")
            print(
                "Key characteristics: Oxidase-, Gram- coccobacillus, Non-motile, Non-fermenter")
            print("Clinical significance: Multidrug-resistant pathogen, nosocomial")
            print("Recommended antibiotics: Carbapenems, Colistin, Tigecycline")
    else:
        # Enterobacteriaceae (fermenters)
        print("\n>>> Preliminary identification: Enterobacteriaceae (Oxidase negative, fermenters)")

        glucose = get_yes_no_input("Glucose fermentation positive? (yes/no): ")

        if not glucose:
            print(
                "\n>>> Warning: Gram-negative bacilli should ferment glucose. Check results.")
            return

        lactose = get_yes_no_input("Lactose fermentation positive? (yes/no): ")
        indole = get_yes_no_input("Indole production positive? (yes/no): ")

        if lactose and indole:
            print("\nConfirmed identification: Escherichia coli")
            print("Key characteristics: Gram- rods, Lactose+, Indole+, Oxidase-")
            print("Clinical significance: UTI, gastroenteritis, bacteremia, meningitis")
            print(
                "Recommended antibiotics: Fluoroquinolones, Cephalosporins, Carbapenems")

        elif lactose and not indole:
            citrate = get_yes_no_input(
                "Citrate utilization positive? (yes/no): ")

            if citrate:
                print("\nConfirmed identification: Klebsiella pneumoniae")
                print("Key characteristics: Gram- rods, Lactose+, Indole-, Citrate+")
                print("Clinical significance: Respiratory infections, UTI, bacteremia")
                print(
                    "Recommended antibiotics: Cephalosporins, Carbapenems, Fluoroquinolones")
            else:
                print("\nConfirmed identification: Enterobacter spp.")
                print("Key characteristics: Gram- rods, Lactose+, Indole-, Citrate-")
                print("Common species: E. cloacae, E. aerogenes")
                print("Clinical significance: Nosocomial infections")
                print(
                    "Recommended antibiotics: Carbapenems, Cephalosporins, Fluoroquinolones")

        elif not lactose:
            urease = get_yes_no_input("Urease production positive? (yes/no): ")

            if urease:
                print("\nConfirmed identification: Proteus spp.")
                print("Key characteristics: Gram- rods, Lactose-, Urease+, Indole+/-")
                print("Clinical significance: UTI, wound infections, gastroenteritis")
                print(
                    "Recommended antibiotics: Fluoroquinolones, Cephalosporins, Carbapenems")
            else:
                citrate = get_yes_no_input(
                    "Citrate utilization positive? (yes/no): ")

                if citrate:
                    print("\nConfirmed identification: Salmonella spp.")
                    print("Key characteristics: Gram- rods, Lactose-, Citrate+")
                    print("Clinical significance: Gastroenteritis, bacteremia")
                    print(
                        "Recommended antibiotics: Fluoroquinolones, Cephalosporins, TMP-SMX")
                else:
                    print("\nConfirmed identification: Shigella spp.")
                    print(
                        "Key characteristics: Gram- rods, Lactose-, Citrate-, Motility-")
                    print("Clinical significance: Dysentery, gastroenteritis")
                    print(
                        "Recommended antibiotics: Fluoroquinolones, Cephalosporins, TMP-SMX")

# Function to test Gram-negative spirilla


def test_gram_negative_spirilla():
    print("\n--- GRAM-NEGATIVE SPIRILLA/CURVED BACILLI IDENTIFICATION ---")
    print("CLSI Protocol: Primary tests include Oxidase, Catalase, Motility, Urease.\n")

    oxidase = get_yes_no_input("Oxidase test positive? (yes/no): ")
    urease = get_yes_no_input("Urease test positive? (yes/no): ")

    if oxidase and urease:
        print("\nConfirmed identification: Helicobacter pylori")
        print("Key characteristics: Oxidase+, Urease+, Gram- curved bacillus, Motile")
        print("Clinical significance: Gastric ulcers, gastritis, gastric carcinoma")
        print("Recommended antibiotics: Triple/Quad therapy (Proton pump inhibitor + Bismuth + Antibiotics)")

    elif oxidase and not urease:
        print("\nConfirmed identification: Campylobacter spp.")
        print(
            "Key characteristics: Oxidase+, Urease-, Gram- spiral/curved bacillus, Motile")
        print("Common species: C. jejuni, C. coli")
        print("Clinical significance: Gastroenteritis, bacteremia")
        print("Recommended antibiotics: Macrolides (Erythromycin), Fluoroquinolones, Tetracyclines")

    else:
        print("\nConfirmed identification: Other Gram-negative curved bacillus")
        print("Possible species: Vibrio spp., Arcobacter spp.")
        print("Perform additional tests: Salt tolerance, Growth at different temperatures")


# Main program logic
print("="*70)
print("This program will guide you through biochemical identification")
print("following CLSI (Clinical and Laboratory Standards Institute) standards.")
print("="*70)

# Get initial Gram stain information from user (integrate with Phase 2 data if available)
print("\nFrom Gram's Stain Analysis:")
print("1. Gram-positive cocci")
print("2. Gram-positive bacilli")
print("3. Gram-negative cocci")
print("4. Gram-negative bacilli")
print("5. Gram-negative spirilla/curved bacilli")

while True:
    try:
        bacteria_type = int(input("\nSelect bacteria type (1-5): ").strip())
        if bacteria_type not in [1, 2, 3, 4, 5]:
            print("Invalid selection. Please enter 1-5.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1-5.")

# Route to appropriate testing function
if bacteria_type == 1:
    cell_arrangement = input(
        "Enter cell arrangement (clusters/chains/pairs): ").strip().lower()
    test_gram_positive_cocci(cell_arrangement)
elif bacteria_type == 2:
    cell_arrangement = input(
        "Enter cell arrangement (chains/pairs/single): ").strip().lower()
    test_gram_positive_bacilli(cell_arrangement)
elif bacteria_type == 3:
    test_gram_negative_cocci()
elif bacteria_type == 4:
    cell_arrangement = input(
        "Enter cell arrangement (chains/pairs/single): ").strip().lower()
    test_gram_negative_bacilli(cell_arrangement)
elif bacteria_type == 5:
    test_gram_negative_spirilla()

# Prompt user to continue or exit
print("\n" + "="*70)
while True:
    continue_choice = input(
        "\nDo you want to identify another pathogen? (yes/no): ").strip().lower()
    if continue_choice == "yes":
        print("\nRestarting biochemical identification process...\n")
        exec(open(__file__).read())  # Restart the script
    elif continue_choice == "no":
        print("Exiting the program. Thank you for using CDSS!")
        sys.exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
