# functions with outputs

def format_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    format_full_name = full_name.title()
    return format_full_name


output = format_name("FiOna", "kaMaraJ")
print(output)
