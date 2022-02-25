#Functions with output

def format_name(f_name,l_name):
    first_name=f_name.title()
    last_name=l_name.title()
    return f"{first_name} {last_name}"

output_string=format_name("priyanshu","UpadhYay")
print(output_string)