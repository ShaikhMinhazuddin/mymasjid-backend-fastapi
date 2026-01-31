
def generate_mosque_id(mosque_name:str, pincode: str) -> str:
    initials = "".join(
        word[0].upper() for word in mosque_name.split()
    )
    return f"{initials}{pincode}"
print(generate_mosque_id("Ispat Anjuman Jama Masjid","769003"))