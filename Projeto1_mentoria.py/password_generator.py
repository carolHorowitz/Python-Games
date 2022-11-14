

def password_generator():

    print("Welcome!! Let´s start to create a new password.")
    characters = int(input("How many character should there be? Your password must contain a minimum of 4 and a maximum of 10 characters: "))
    upper = input("Should it have uppercase letter?; ")
    num = input("Should it have numbers?: ")
    esp = input("Should it have specials characters?: ")
    
    password_length = number_of_characters(characters)
    
def number_of_characters(characters):
    
        
