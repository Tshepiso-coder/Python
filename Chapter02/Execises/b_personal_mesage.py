# first_name = "tshepiso"
# last_name = "molapisi"
# full_name = first_name + " " + last_name

# # Print full_name
# print(full_name)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())

# # print(f"Hello {full_name}. Welcome to the Python class")
# author = "albert einstein" 
# #PRINT DIFFERENT WAYS OF WRITING QUOTE
# # quote = f'{author} once said “A person who never made a mistake never tried anything new.”'
# # quote = f"{author} once said 'A person who never made a mistake never tried anything new'"
# quote = f"{author.title()} once said \"A person who never made"
# quote += " a mistake never tried anything new\""
# print(quote)

#using STRIP LSTRP RSTRIP
# first_name = "tshepiso   "
# last_name = "   molapisi"
# last_name = "\tmolapisi"
# full_name = first_name.rstrip() + " " + last_name.lstrip()
# print(full_name)

#REMOVING USING REMOVEPREFFIX AND REMOVESUFFIX
my_url = "https://www.bokamoso.co.za/index.html"
print(my_url)
print(my_url.removeprefix("https://"))
print(my_url.removesuffix(".html"))
print(my_url.replace(".html",".HTMX"))
