import random
def sample(population, k):
    result = []
    items = list(population)
    while len(result) < k and items:
        c = random.choice(items)
        result.append(c)
        items.remove(c)
    return result
print("Welcome to IMPOSTOR!")
print("Number of Players?")
print("3-10 players")
num_players = int(input())
impcount = int(input("Number of Impostors? "))
if impcount > num_players // 2:
    print("Too many impostors!")
elif impcount <= num_players // 2:
    print("Game starting with")
    print(num_players - impcount, "civilians and")
    print(impcount, "impostors.")
    names = []
    for i in range(num_players):
        print("Player", i + 1, "Name?")
        names.append(input())
    imps = sample(range(num_players), impcount)
    data = [
        ("America", "Liberty"), ("England", "Castle"), ("Ireland", "Shamrock"),
        ("Scotland", "Thistle"), ("India", "Curry"), ("China", "Dragon"),
        ("Japan", "Samurai"), ("France", "Wine"), ("Germany", "Autobahn"),
        ("Spain", "Flamenco"), ("Italy", "Colosseum"), ("Apple", "Orchard"),
        ("Banana", "Monkey"), ("Orange", "Vitamin"), ("Mango", "Tropical"),
        ("Pineapple", "Spiny"), ("Strawberry", "Seeds"), ("Blueberry", "Berry"),
        ("Raspberry", "Thorn"), ("Kiwi", "Fuzzy"), ("Watermelon", "Summer"),
        ("Grapes", "Vine"), ("Peach", "Fuzz"), ("Pear", "Juice"), ("Lemon", "Sour"),
        ("Lime", "Green"), ("Cherry", "Red"), ("Pizza", "Slice"), ("Burger", "Bun"),
        ("Pasta", "Noodles"), ("Sushi", "Rice"), ("Sandwich", "Bread"),
        ("Salad", "Lettuce"), ("Tacos", "Shell"), ("Rice", "Grain"),
        ("Soup", "Broth"), ("Pancakes", "Maple"), ("Waffles", "Grid"),
        ("Curry", "Spicy"), ("Steak", "Grill"), ("Fries", "Potato"),
        ("Hotdog", "Sausage"), ("Bagel", "Hole"), ("Omelette", "Egg"),
        ("Lasagna", "Layers"), ("Risotto", "Creamy"), ("Shepherd   s Pie", "Mash"),
        ("Samosa", "Triangle"), ("Falafel", "Chickpea"), ("Apple (company)", "iPhone"),
        ("Samsung", "Galaxy"), ("Microsoft", "Windows"), ("Google", "Search"),
        ("Sony", "Play"), ("Dell", "Laptop"), ("HP", "Printer"), ("Lenovo", "Think"),
        ("Intel", "Chip"), ("Nvidia", "Graphics"), ("Amazon", "Prime"),
        ("Huawei", "Phone"), ("Nike", "Swoosh"), ("Adidas", "Three"),
        ("Puma", "Cat"), ("Gucci", "Belt"), ("Louis Vuitton", "Bag"),
        ("H&M", "Affordable"), ("Zara", "Fashion"), ("Levi   s", "Jeans"),
        ("Versace", "Luxury"), ("Prada", "Designer"), ("Ralph Lauren", "Polo"),
        ("Supreme", "Logo"), ("Champion", "Sports"), ("Tesla", "Electric"),
        ("BMW", "Bavaria"), ("Mercedes", "Star"), ("Toyota", "Reliable"),
        ("Ford", "Truck"), ("Maths", "Numbers"), ("Physics", "Force"),
        ("Chemistry", "Elements"), ("Biology", "Life"), ("English", "Grammar"),
        ("History", "Past"), ("Geography", "Maps"), ("Computer Science", "Code"),
        ("Art", "Paint"), ("Music", "Melody"), ("Physical Education", "Exercise"),
        ("Economics", "Money"), ("Press conference", "Speaker"),
        ("Traffic light", "Intersection"), ("Washing machine", "Laundry"),
        ("Window sill", "Sunlight"), ("Clock", "Time"), ("Chair", "Table"),
        ("Sofa", "Lamp"), ("Mirror", "Curtains"), ("Frozen", "Refrigerator"),
        ("Oven", "Microwave"), ("Earbuds", "Music"), ("Headphones", "Sound"),
        ("Wallet", "Cash"), ("Keys", "Unlock"), ("Sunglasses", "Shades"),
        ("Watch", "Timepiece"), ("Backpack", "Bag"), ("Notebook", "Write"),
        ("Pen", "Write"), ("Pencil", "Graphite"), ("Eraser", "Mistake"),
        ("Granola", "Oats"), ("Honey", "Sweet"), ("Lamb", "Sheep"),
        ("Pork", "Pig"), ("Beef", "Cow"), ("Fish", "Water"), ("Chicken", "Egg"),
        ("Lion", "Savannah"), ("Tiger", "Stripe"), ("Elephant", "Tusks"),
        ("Giraffe", "Neck"), ("Zebra", "Stripes"), ("Kangaroo", "Pouch"),
        ("Panda", "Bamboo"), ("Koala", "Eucalyptus"), ("Monkey", "Tree"),
        ("Bear", "Hibernation"), ("Wolf", "Pack"), ("Fox", "Cunning"),
        ("Rabbit", "Burrow"), ("Deer", "Antlers"), ("Dolphin", "Intelligent"),
        ("Whale", "Ocean"), ("Eagle", "Flight"), ("Owl", "Night"),
        ("Cable", "Wire"), ("Ladder", "Steps"), ("Garden gloves", "Hands"),
        ("Watering can", "Water"), ("Rake", "Leaves"), ("Hose", "Spray"),
        ("Wheelbarrow", "Push"), ("Flower pot", "Plant"), ("Lawn mower", "Grass"),
        ("Building sandcastles", "Sand"), ("Sledding", "Snow"),
        ("Caroling", "Song"), ("Ice skating", "Ice")
    ]
    word, hint = random.choice(data)
    for i in range(num_players):
        print("Pass to",
               names[i])
        while True:
            ready = input("Press - then EXE \n"
            "When ready:")
            if ready == "-":
                break
        if i in imps:
            print("You are the")
            print("IMPOSTOR!")
            print("Your hint word is:")
            print(hint)
        else:
            print("You are a")
            print("CIVILIAN.")
            print("Your word is:")
            print(word)
        while True:
            cont = input("Memorised?\n"
            "Press - then EXE \n"
            "to continue:")
            if cont == "-":
                print("\n" * 10)
                break
    print("All roles assigned.\n"
    "Begin game!")
    player_start=random.choice(names)
    print("Player ",player_start,"starts!")
    print("Reveal impostor? \n"
    "Press - then EXE when ready")
    if input() == "-":  
        for n in imps:
            print("Impostor:",names[n])

#By Arpith Nair
#05/11/2025