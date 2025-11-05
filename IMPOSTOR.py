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
impcount = int(input("How Many\n"
"Impostors?"))
if impcount > num_players // 2:
    print("Too many impostors!")
elif impcount <= num_players // 2:
    print("Game starting with")
    print(num_players - impcount, "civilians and")
    print(impcount, "impostors.")
    places = [
    ("Amsterdam", "Bicycles"),
    ("Argentina", "Tango"),
    ("Australia", "Outback"),
    ("Beijing", "Forbiddencity"),
    ("Beijing", "Capitalpower"),
    ("Berlin", "Wall"),
    ("Bern", "Alpsgovt"),
    ("Brazil", "Carnival"),
    ("Brussels", "Waffles"),
    ("Buenos Aires", "Football"),
    ("Cairo", "Pharaoh"),
    ("Canada", "Maple"),
    ("China", "Dragon"),
    ("China", "Manufacture"),
    ("Egypt", "Pyramids"),
    ("France", "Wine"),
    ("France", "Revolution"),
    ("Germany", "Autobahn"),
    ("India", "Bollywood"),
    ("India", "Spices"),
    ("Italy", "Pasta"),
    ("Japan", "Samurai"),
    ("Japan", "Nintendo"),
    ("Lisbon", "Explorers"),
    ("London", "Monarchy"),
    ("Madrid", "Bullfight"),
    ("Mexico", "Tacos"),
    ("Mexico City", "Megacity"),
    ("Milan", "Fashion"),
    ("Mumbai", "Bollywood"),
    ("Netherlands", "Windmills"),
    ("New York", "Broadway"),
    ("Ottawa", "Mounties"),
    ("Paris", "Love"),
    ("Portugal", "Navigate"),
    ("Pretoria", "Apartheid"),
    ("Rome", "Empire"),
    ("Rome", "Vatican"),
    ("Shanghai", "Megapolis"),
    ("South Africa", "Safari"),
    ("Spain", "Flamenco"),
    ("Switzerland", "Banks"),
    ("Sydney", "Harbour"),
    ("Tokyo", "Anime"),
    ("Tokyo", "Sushi"),
    ("Toronto", "Hockey"),
    ("United Kingdom", "Tea"),
    ("United States", "Liberty"),
    ("Washington D.C.", "Congress")
]
    items = [
    ("Anger", "Frustration"),
    ("Bag", "Carry"),
    ("Bed", "Sleep"),
    ("Blanket", "Warmth"),
    ("Bottle", "Container"),
    ("Chair", "Sit"),
    ("Charger", "Power"),
    ("Comfort", "Cozy"),
    ("Confidence", "Selfbelief"),
    ("Cup", "Drink"),
    ("Curiosity", "Wonder"),
    ("Door", "Entry"),
    ("Effort", "Work"),
    ("Failure", "Mistake"),
    ("Fear", "Threat"),
    ("Focus", "Attention"),
    ("Freedom", "Choice"),
    ("Friendship", "Bond"),
    ("Glasses", "Vision"),
    ("Habit", "Routine"),
    ("Happiness", "Joy"),
    ("Headphones", "Audio"),
    ("Health", "Wellbeing"),
    ("Hope", "Optimism"),
    ("Jacket", "Warm"),
    ("Keys", "Unlock"),
    ("Knowledge", "Learning"),
    ("Laptop", "Work"),
    ("Love", "Affection"),
    ("Memory", "Recall"),
    ("Mirror", "Reflection"),
    ("Motivation", "Drive"),
    ("Notebook", "Notes"),
    ("Patience", "Endurance"),
    ("Pen", "Write"),
    ("Phone", "Call"),
    ("Pillow", "Comfort"),
    ("Purpose", "Meaning"),
    ("Respect", "Value"),
    ("Shoes", "Wear"),
    ("Stress", "Pressure"),
    ("Success", "Achievement"),
    ("Table", "Dining"),
    ("Time", "Passing"),
    ("Toothbrush", "Clean"),
    ("Trust", "Confidence"),
    ("Umbrella", "Rain"),
    ("Wallet", "Money"),
    ("Watch", "Timepiece"),
    ("Water", "Hydrate")
]
    activities = [
("Archery","Bow"),
("Baking","Oven"),
("Boxing","Punch"),
("Camping","Tent"),
("Canoeing","Paddle"),
("Cleaning","Tidy"),
("Climbing","Rock"),
("Cooking","Meal"),
("Cycling","Bike"),
("Cycling","Road"),
("Dancing","Movement"),
("Drawing","Sketch"),
("Driving","Car"),
("Fishing","Catch"),
("Flying","Airplane"),
("Gardening","Plants"),
("Hiking","Trail"),
("Hiking Trail","Mountain"),
("Horse Riding","Saddle"),
("Jogging","Fitness"),
("Jogging","Park"),
("Jump Rope","Cord"),
("Kayaking","Paddle"),
("Martial Arts","Combat"),
("Painting","Art"),
("Photography","Camera"),
("Pilates","Core"),
("Playing Basketball","Hoop"),
("Playing Soccer","Goal"),
("Playing Tennis","Racket"),
("Playing Volleyball","Net"),
("Rock Climbing","Crag"),
("Rollerblading","Wheels"),
("Rowing","River"),
("Running","Exercise"),
("Running Errands","Tasks"),
("Sailing","Boat"),
("Shopping","Store"),
("Skateboarding","Trick"),
("Skating","Glide"),
("Skiing","Snow"),
("Snowboarding","Slope"),
("Surfing","Wave"),
("Surfing Waves","Beach"),
("Sweeping","Floor"),
("Swimming","Water"),
("Swimming Laps","Pool"),
("Vacuuming","Carpet"),
("Walking","Stroll"),
("Weightlifting","Strength"),
("Yoga","Stretch")
]
    school = [
("Art","Create"),
("Assembly","Gather"),
("Backpack","Carry"),
("Binder","Organize"),
("Cafeteria","Lunch"),
("Calculator","Compute"),
("Chair","Sit"),
("Club","Participate"),
("Compass","Circle"),
("Debate","Argue"),
("Desk","Study"),
("Drama","Perform"),
("Eraser","Correct"),
("Essay","Writeup"),
("Exam","Test"),
("Experiment","Lab"),
("Field trip","Travel"),
("Geography","Map"),
("Glue","Stick"),
("Highlighter","Highlight"),
("History","Learn"),
("Homework","Assignment"),
("Language","Vocabulary"),
("Laptop","Work"),
("Lecture","Listen"),
("Library","Books"),
("Marker","Draw"),
("Math","Calculate"),
("Music","Play"),
("Notebook","Write"),
("Pen","Ink"),
("Pencil","Sketch"),
("Physical education","Exercise"),
("Presentation","Speak"),
("Project","Presentation"),
("Protractor","Angle"),
("Quiz","Questions"),
("Reading","Practice"),
("Recess","Break"),
("Research","Investigate"),
("Ruler","Measure"),
("Science","Observe"),
("Scissors","Cut"),
("Sports","Compete"),
("Stapler","Fasten"),
("Study group","Review"),
("Textbook","Read"),
("Timetable","Schedule"),
("Volunteering","Help"),
("Whiteboard","Display"),
("Writing","Compose"),
]
    holidays = [
("Baking","Cookies"),
("Beach","Sand"),
("Beach volleyball","Game"),
("Bonfire","Warmth"),
("Campfire","Stories"),
("Camping","Tent"),
("Candles","Light"),
("Cards","Play"),
("Carnival","Parade"),
("Caroling","Sing"),
("Chocolate eggs","Treat"),
("Christmas","Celebration"),
("Costumes","Dress"),
("Cycling","Ride"),
("Decorating","Tree"),
("Diwali","Lights"),
("Easter","Egg hunt"),
("Feast","Family"),
("Fireworks","Display"),
("Fishing","Lake"),
("Gathering","Friends"),
("Gift exchange","Presents"),
("Gifts","Wrap"),
("Halloween","Costume"),
("Hanukkah","Menorah"),
("Hiking trail","Nature"),
("Ice skating","Rink"),
("Mountains","Hiking"),
("Museum visit","Culture"),
("New year","Fireworks"),
("Ornaments","Decorate"),
("Parade","Celebrate"),
("Passport","Identity"),
("Picnic","Outdoors"),
("Picnic blanket","Sit"),
("Relaxing","Rest"),
("Road trip","Drive"),
("Shopping","Gifts"),
("Shopping spree","Mall"),
("Skiing","Snow"),
("Sledding","Hill"),
("Snowball fight","Fun"),
("St. patrick's day","Shamrock"),
("Suitcase","Travel"),
("Sunglasses","Sun"),
("Sunscreen","Protect"),
("Surfing","Waves"),
("Swimming","Pool"),
("Thanksgiving","Feast"),
("Traveling","Journey"),
("Turkey","Meal"),
("Valentine's day","Love"),
]
    datasets = {
    "1": places,
    "2": items,
    "3": activities,
    "4": school,
    "5": holidays
}
    print("Choose an option:")
    print("1 - Places")
    print("2 - Items")
    print("3 - Activities")
    print("4 - School")
    print("5 - Holidays")
    choice = input("Option:").strip()
    if choice in datasets:
        data = datasets[choice]   
        word, hint = random.choice(data)
    else:
        print("Invalid choice, please select 1-5")
    names = []
    for i in range(num_players):
        print("Player", i + 1, "Name?")
        names.append(input())
    imps = sample(range(num_players), impcount)
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
    print(player_start,"starts!")
    print("Reveal impostor? \n"
    "Press - then EXE when ready")
    if input() == "-":  
        for n in imps:
            print("Impostor:",names[n])
#By Arpith Nair
#05/11/2025