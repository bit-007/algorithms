def stable_match(men_prefs, women_prefs):
    # Initialize all men and women as free
    free_men = list(men_prefs.keys())
    engagements = {}
    # While there are free men
    while free_men:
        man = free_men.pop(0)
        # Get the preferences of the man
        man_pref = men_prefs[man]
        # Propose to the first woman in the man's preference list
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)
        # If the woman is not engaged, engage her with the current man
        if not fiance:
            engagements[woman] = man
        else:
            # If the woman prefers the current man over her fiance
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman] = man
                free_men.append(fiance)
            else:
                # The woman rejects the proposal
                free_men.append(man)
    return engagements

def get_preferences(entity, count):
    prefs = {}
    print(f"Enter the preferences for {entity}:")
    for i in range(1, count + 1):
        key = f"{entity[0]}{i}"
        prefs_list = input(f"Enter the preferences for {key} separated by commas: ").strip().split(',')
        prefs[key] = [pref.strip() for pref in prefs_list]
    return prefs

print("Enter the men's preferences:")
men_prefs = get_preferences('men', 3)

print("Enter the women's preferences:")
women_prefs = get_preferences('women', 3)

stableMatches = stable_match(men_prefs, women_prefs)
print("Stable Matches:")
for woman, man in stableMatches.items():
    print(f"{man} engaged to {woman}")
