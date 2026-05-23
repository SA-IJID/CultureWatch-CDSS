# PHASE 2: GRAM'S STAIN CHARACTERISTICS OF PATHOGEN

# display phase title.
print("\n--- PHASE 2: GRAM'S STAIN CHARACTERISTICS OF PATHOGEN ---")
# prompt user for input.
print("Please provide the following information about the pathogen based on Gram's stain characteristics.")

while True:
    while True:
        Gram_Reaction = input(
            "Is the pathogen Gram-positive or Gram-negative? (Enter 'positive' or 'negative'): ").strip().lower()
        if Gram_Reaction not in ["positive", "negative"]:
            print("Invalid Gram reaction input. Please enter 'positive' or 'negative'.")
            continue

        Cell_Shape = input(
            "What is the shape of the pathogen's cells? (Enter 'cocci', 'bacilli', or 'spirilla'): ").strip().lower()
        if Cell_Shape not in ["cocci", "bacilli", "spirilla"]:
            print(
                "Invalid cell shape input. Please enter 'cocci', 'bacilli', or 'spirilla'.")
            continue

        Cell_Arrangement = input(
            "How are the cells arranged? (Enter 'clusters', 'chains', or 'pairs'): ").strip().lower()
        if Cell_Arrangement not in ["clusters", "chains", "pairs"]:
            print(
                "Invalid cell arrangement input. Please enter 'clusters', 'chains', or 'pairs'.")
            continue

        break

    # Logic for Gram - Positive Bacteria
    # Gram-positive bacteria retain the crystal violet stain and appear purple under the microscope.
    if Gram_Reaction == "positive":
        # Gram-positive cocci can be arranged in clusters (like grapes), chains, or pairs.
        if Cell_Shape == "cocci":
            if Cell_Arrangement == "clusters":
                print("\nThe pathogen is likely Staphylococcus spp.")
            elif Cell_Arrangement == "chains":
                print("\nThe pathogen is likely Streptococcus spp.")
            elif Cell_Arrangement == "pairs":
                print(
                    "\nThe pathogen is likely Streptococcus spp. (including S. pneumoniae) or Enterococcus spp.")
        # Gram-positive bacilli can be arranged singly, in chains, or in pairs, but clusters are uncommon.
        elif Cell_Shape == "bacilli":
            if Cell_Arrangement == "chains":
                print(
                    "\nThe pathogen is likely a chain-forming Gram-positive bacillus such as Bacillus spp.")
            elif Cell_Arrangement == "pairs":
                print(
                    "\nThe pathogen may represent Listeria monocytogenes or a coryneform bacillus.")
            elif Cell_Arrangement == "clusters":
                print(
                    "\nGram-positive rods are usually seen singly or in chains; clusters are atypical.")
        elif Cell_Shape == "spirilla":  # Gram-positive spiral-shaped bacteria are extremely rare and not commonly encountered in clinical microbiology. If you observe spiral-shaped cells that are Gram-positive, it may be due to a staining artifact or misinterpretation of the morphology. Consider re-evaluating the Gram stain and morphology to ensure accurate identification.
            print(
                "\nGram-positive bacteria are not typically spiral-shaped. Please check your inputs.")

    # Logic for Gram - Negative Bacteria
    # Gram-negative bacteria do not retain the crystal violet stain and appear pink or red under the microscope after counterstaining with safranin.
    elif Gram_Reaction == "negative":
        # Gram-negative cocci can be arranged in pairs (diplococci), chains, or clusters, but the most common arrangement is pairs.
        if Cell_Shape == "cocci":
            if Cell_Arrangement == "pairs":
                print(
                    "\nThe pathogen is likely Neisseria spp. or Moraxella catarrhalis.")
            elif Cell_Arrangement == "chains":
                print(
                    "\nGram-negative cocci rarely form true chains; consider verifying the Gram reaction and morphology.")
            elif Cell_Arrangement == "clusters":
                print(
                    "\nGram-negative cocci in clusters are unusual; verify the Gram reaction and morphology.")
        # Gram-negative bacilli can be arranged singly, in chains, or in pairs.
        elif Cell_Shape == "bacilli":
            if Cell_Arrangement == "chains":
                print("\nThe pathogen may be an Enterobacteriaceae organism such as Escherichia coli, Klebsiella spp., or Enterobacter spp.")
            elif Cell_Arrangement == "pairs":
                print(
                    "\nThe pathogen may be Acinetobacter spp. or another Gram-negative coccobacillus.")
            elif Cell_Arrangement == "clusters":
                print(
                    "\nGram-negative rods are usually single or in short chains; clusters are atypical.")
        # Gram-negative spiral-shaped bacteria are uncommon but can be encountered in clinical settings.
        elif Cell_Shape == "spirilla":
            print("\nThe pathogen is likely Helicobacter pylori, Campylobacter spp., or another curved/spiral Gram-negative bacillus.")

    while True:  # Prompt user to continue or exit the program.
        continue_choice = input(
            "\nDo you want to analyze another pathogen? (Enter 'yes' or 'no'): ").strip().lower()
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            print("Exiting the program.")
            exit()
        else:
            # Loop back to prompt user for valid input.
            print("Invalid input. Please enter 'yes' or 'no'.")
