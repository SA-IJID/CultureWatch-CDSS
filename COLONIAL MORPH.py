
# PHASE 0: PATIENT INFORMATION.
print("--- PHASE 0: PATIENT INFORMATION ---")
# This line prompts the user to enter a patient ID and converts it to an integer.
Patient_ID = int(input("Enter Patient ID: "))
# This line prompts the user to enter a patient name and stores it as a string.
Patient_Name = input("Enter Patient Name: ")

# PHASE 1: COLONIAL MORPHOLOGY OF PATHOGEN ON AGAR PLATE.
# This section prompts the user to enter various colony morphology characteristics of a pathogen grown on an agar plate. The user is guided to input specific features such as size, color, shape, elevation, margin, texture, opacity, consistency, odor, hemolysis, pigmentation, and surface. The program then uses these inputs to attempt a preliminary identification of the pathogen based on known patterns of colonial morphology.
print("--- PHASE 1: COLONIAL MORPHOLOGY OF PATHOGEN ON AGAR PLATE ---")

# This line provides instructions to the user on how to enter the colony morphology characteristics, indicating that they should use the allowed options provided in the subsequent list. This helps ensure that the user inputs valid and standardized values for each characteristic, which is crucial for accurate preliminary identification of the pathogen.
print("\nEnter colony morphology values using the allowed options below:")
print(" - Size: Small, Medium, Large")
print(" - Color: White, Brown, Red")
print(" - Shape: Round, Irregular")
print(" - Elevation: Flat, Raised, Convex")
print(" - Margin: Entire, Undulate")
print(" - Texture: Smooth, Rough")
print(" - Opacity: Opaque, Translucent")
print(" - Consistency: Butyrous, Viscous")
print(" - Odor: Fruity, Pungent")
print(" - Hemolysis: Alpha, Beta, Gamma")
print(" - Pigmentation: Non-pigmented, Pigmented")
print(" - Surface: Smooth, Rough")


def prompt_option(prompt, allowed_values):  # This function prompts the user to enter a value for a specific colony morphology characteristic and validates the input against a set of allowed options. The function takes two parameters: prompt (the message displayed to the user) and allowed_values (a dictionary mapping valid input options to their corresponding standardized values). The user's input is normalized to lowercase for comparison, and if it matches one of the allowed options, the corresponding standardized value is returned. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
    normalized = {key.lower(): value for key, value in allowed_values.items()}
    while True:  # This line starts an infinite loop that will continue until the user provides a valid input. Inside the loop, the program prompts the user for input and checks if it matches any of the allowed options. If a valid input is received, the loop will break and return the corresponding value; otherwise, an error message is displayed, and the loop continues to prompt the user.
        response = input(prompt).strip().lower()
        if response in normalized:
            return normalized[response]
        print("Invalid entry. Please choose from:",
              # This line prints an error message indicating that the user's input is invalid and provides a list of valid options to choose from. The allowed values are sorted and displayed in a comma-separated format to guide the user in entering a correct value for the colony morphology characteristic.
              ", ".join(sorted(set(normalized.values()))))


Colony_Size = prompt_option("Enter Colony Size (Small/Medium/Large): ", {
    "small": "Small",
    "medium": "Medium",
    "large": "Large",
    # This line prompts the user to enter the colony size and validates the input against allowed options (Small, Medium, Large). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Color = prompt_option("Enter Colony Color (White/Brown/Red): ", {
    "white": "White",
    "brown": "Brown",
    "red": "Red",
    # This line prompts the user to enter the colony color and validates the input against allowed options (White, Brown, Red). Similar to the previous prompt, the user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Shape = prompt_option("Enter Colony Shape (Round/Irregular): ", {
    "round": "Round",
    "irregular": "Irregular",
    # This line prompts the user to enter the colony shape and validates the input against allowed options (Round, Irregular). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Elevation = prompt_option("Enter Colony Elevation (Flat/Raised/Convex): ", {
    "flat": "Flat",
    "raised": "Raised",
    "convex": "Convex",
    # This line prompts the user to enter the colony elevation and validates the input against allowed options (Flat, Raised, Convex). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Margin = prompt_option("Enter Colony Margin (Entire/Undulate): ", {
    "entire": "Entire",
    "undulate": "Undulate",
    # This line prompts the user to enter the colony margin and validates the input against allowed options (Entire, Undulate). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Texture = prompt_option("Enter Colony Texture (Smooth/Rough): ", {
    "smooth": "Smooth",
    "rough": "Rough",
    # This line prompts the user to enter the colony texture and validates the input against allowed options (Smooth, Rough). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Opacity = prompt_option("Enter Colony Opacity (Opaque/Translucent): ", {
    "opaque": "Opaque",
    "translucent": "Translucent",
    # This line prompts the user to enter the colony opacity and validates the input against allowed options (Opaque, Translucent). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Consistency = prompt_option("Enter Colony Consistency (Butyrous/Viscous): ", {
    "butyrous": "Butyrous",
    "viscous": "Viscous",
    # This line prompts the user to enter the colony consistency and validates the input against allowed options (Butyrous, Viscous). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Odor = prompt_option("Enter Colony Odor (Fruity/Pungent): ", {
    "fruity": "Fruity",
    "pungent": "Pungent",
    # This line prompts the user to enter the colony odor and validates the input against allowed options (Fruity, Pungent). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Hemolysis = prompt_option("Enter Colony Hemolysis (Alpha/Beta/Gamma): ", {
    "alpha": "Alpha",
    "beta": "Beta",
    "gamma": "Gamma",
    # This line prompts the user to enter the colony hemolysis type and validates the input against allowed options (Alpha, Beta, Gamma). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Pigmentation = prompt_option("Enter Colony Pigmentation (Non-pigmented/Pigmented): ", {
    "non-pigmented": "Non-pigmented",
    "pigmented": "Pigmented",
    # This line prompts the user to enter the colony pigmentation and validates the input against allowed options (Non-pigmented, Pigmented). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})
Colony_Surface = prompt_option("Enter Colony Surface (Smooth/Rough): ", {
    "smooth": "Smooth",
    "rough": "Rough",
    # This line prompts the user to enter the colony surface texture and validates the input against allowed options (Smooth, Rough). The user's input is normalized to lowercase for comparison, and the corresponding value is returned if valid. If the input is invalid, an error message is displayed, and the user is prompted again until a valid entry is provided.
})

# This line prints a header for the preliminary report section, indicating that the following information will be based on the colonial morphology characteristics entered by the user.
# It separates this section from the previous input prompts and provides context for the results that will be displayed.
print("\n--- Preliminary Report ---")
feature_key = (
    Colony_Size,
    Colony_Color,
    Colony_Shape,
    Colony_Elevation,
    Colony_Margin,
    Colony_Texture,
    Colony_Opacity,
    Colony_Consistency,
    Colony_Odor,
    Colony_Hemolysis,
    Colony_Pigmentation,
    Colony_Surface,
)

# Clinical colony morphology is subjective. Use the most obvious features to suggest likely organisms, but do not treat this as a definitive identification.
candidate_profiles = {
    "Staphylococcus aureus": {
        "Size": {"Medium", "Large"},
        "Color": {"White"},
        "Shape": {"Round"},
        "Elevation": {"Raised", "Convex"},
        "Margin": {"Entire"},
        "Texture": {"Smooth"},
        "Opacity": {"Opaque"},
        "Consistency": {"Butyrous"},
        "Odor": {"Pungent"},
        "Hemolysis": {"Beta"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Smooth"},
    },
    "Streptococcus spp.": {
        "Size": {"Small", "Medium"},
        "Color": {"White", "Brown"},
        "Shape": {"Round"},
        "Elevation": {"Raised", "Convex"},
        "Margin": {"Entire"},
        "Texture": {"Smooth"},
        "Opacity": {"Translucent"},
        "Consistency": {"Butyrous"},
        "Hemolysis": {"Alpha", "Beta"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Smooth"},
    },
    "Escherichia coli": {
        "Size": {"Medium", "Large"},
        "Color": {"White"},
        "Shape": {"Round"},
        "Elevation": {"Flat", "Raised"},
        "Margin": {"Entire"},
        "Texture": {"Smooth"},
        "Opacity": {"Opaque", "Translucent"},
        "Consistency": {"Butyrous", "Viscous"},
        "Odor": {"Pungent"},
        "Hemolysis": {"Beta", "Gamma"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Smooth"},
    },
    "Pseudomonas aeruginosa": {
        "Size": {"Medium"},
        "Color": {"White", "Brown"},
        "Shape": {"Irregular"},
        "Elevation": {"Flat", "Raised"},
        "Margin": {"Undulate"},
        "Texture": {"Rough"},
        "Opacity": {"Translucent"},
        "Consistency": {"Viscous"},
        "Odor": {"Fruity", "Pungent"},
        "Hemolysis": {"Alpha", "Gamma"},
        "Pigmentation": {"Pigmented", "Non-pigmented"},
        "Surface": {"Rough"},
    },
    "Klebsiella pneumoniae": {
        "Size": {"Medium", "Large"},
        "Color": {"White"},
        "Shape": {"Round"},
        "Elevation": {"Convex", "Raised"},
        "Margin": {"Entire"},
        "Texture": {"Smooth"},
        "Opacity": {"Opaque"},
        "Consistency": {"Viscous"},
        "Hemolysis": {"Gamma"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Smooth"},
    },
    "Serratia marcescens": {
        "Size": {"Small", "Medium"},
        "Color": {"Red"},
        "Shape": {"Round"},
        "Elevation": {"Convex"},
        "Margin": {"Entire"},
        "Texture": {"Smooth"},
        "Opacity": {"Opaque"},
        "Consistency": {"Butyrous"},
        "Hemolysis": {"Gamma"},
        "Pigmentation": {"Pigmented"},
        "Surface": {"Smooth"},
    },
    "Proteus spp.": {
        "Size": {"Small", "Medium"},
        "Color": {"White", "Brown"},
        "Shape": {"Irregular"},
        "Margin": {"Undulate"},
        "Texture": {"Rough"},
        "Opacity": {"Translucent"},
        "Consistency": {"Viscous"},
        "Odor": {"Pungent"},
        "Hemolysis": {"Gamma"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Rough"},
    },
    "Salmonella spp.": {
        "Size": {"Medium", "Large"},
        "Color": {"White", "Brown"},
        "Shape": {"Irregular"},
        "Margin": {"Undulate"},
        "Texture": {"Rough"},
        "Opacity": {"Translucent"},
        "Consistency": {"Viscous"},
        "Odor": {"Pungent"},
        "Hemolysis": {"Gamma"},
        "Pigmentation": {"Non-pigmented"},
        "Surface": {"Rough"},
    },
}

feature_weights = {
    "Color": 3,
    "Hemolysis": 3,
    "Consistency": 2,
    "Texture": 2,
    "Odor": 2,
    "Shape": 1,
    "Size": 1,
    "Elevation": 1,
    "Margin": 1,
    "Opacity": 1,
    "Pigmentation": 1,
    "Surface": 1,
}

feature_values = {
    "Size": Colony_Size,
    "Color": Colony_Color,
    "Shape": Colony_Shape,
    "Elevation": Colony_Elevation,
    "Margin": Colony_Margin,
    "Texture": Colony_Texture,
    "Opacity": Colony_Opacity,
    "Consistency": Colony_Consistency,
    "Odor": Colony_Odor,
    "Hemolysis": Colony_Hemolysis,
    "Pigmentation": Colony_Pigmentation,
    "Surface": Colony_Surface,
}

scores = []
for species, profile in candidate_profiles.items():
    match_score = 0
    max_score = 0
    for feature, expected_values in profile.items():
        weight = feature_weights.get(feature, 1)
        max_score += weight
        if feature_values.get(feature) in expected_values:
            match_score += weight
    if max_score:
        scores.append((match_score / max_score, species))

scores.sort(reverse=True, key=lambda item: item[0])

identification = None
if scores:
    best_score, best_species = scores[0]
    if best_score >= 0.75:
        identification = f"Likely {best_species} ({best_score * 100:.0f}% match)"
    elif best_score >= 0.50:
        second_score = scores[1][0] if len(scores) > 1 else 0
        if second_score >= best_score - 0.10:
            other_species = scores[1][1]
            identification = (
                f"Possible {best_species} ({best_score * 100:.0f}% match); differential includes {other_species}."
            )
        else:
            identification = f"Possible {best_species} ({best_score * 100:.0f}% match)"
    else:
        identification = None

if identification:
    print("Preliminary Identification:", identification)
else:
    print("Preliminary Identification: Unidentified Pathogen - Further Testing Required.")
    print(
        "Note: Colonial morphology is highly subjective. This suggestion is based on the most obvious features and is not a definitive identification."
    )
