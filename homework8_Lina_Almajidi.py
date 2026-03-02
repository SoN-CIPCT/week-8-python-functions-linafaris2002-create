# Homework 8 – Functions
# Lina Almajidi

def make_sandwich(*ingredients):
    print("You ordered a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print()

make_sandwich("turkey", "cheese", "lettuce")
make_sandwich("ham", "swiss", "tomato", "onion", "mustard")