
# name = "shepisO molapisi"
# print(name.title())

# print(name.upper())

# print(name.lower())


# # USING FORMATTED STRING CONTAINING VARIABLES IN {}
# first_name = "tshepiso    "
# last_name = "molapisi"
# full_name = f"\n{first_name.strip()} {last_name}. How are you doing?\n"
# print(full_name.title())


# # PRINT WHITE SPACES AND NEW LINES
print("\tPython")
print("Languages:\n\tPython\nC\nJava")

#STRIPPING WHITE SPACES USING STRIP() RSTRIP() AND LSTRIP()
favorite_language = "python   "
print(favorite_language.rstrip())

# REMOVING PREFIXES
my_url = "https://bokamoso.co.za"
print(my_url.removeprefix("https://"))
print(my_url)

# REMOVING SUFFIXES
my_url = "https://bokamoso.co.za"
print(my_url.removesuffix(".co.za"))
print(my_url)