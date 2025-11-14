import random
def sample(population, k):
    result = []
    items = list(population)
    while len(result) < k and items:
        c = random.choice(items)
        result.append(c)
        items.remove(c)
    return result
places=[
("Argentina","Tango"),
("Arctic","Polar"),
("Australia","Outback"),
("Athens","Acropolis"),
("Atlantis","Lost"),
("Barcelona","Gaudi"),
("Beijing","Forbidden"),
("Berlin","Wall"),
("Birmingham","Industry"),
("Brazil","Carnival"),
("Camelot","King Arthur"),
("Canada","Maple"),
("Cairo","Pyramids"),
("Chicago","Windy"),
("China","Dragon"),
("Delhi","Bollywood"),
("Diagon Alley","Shops"),
("Disney World","Magic"),
("Disneyland Paris","Castle"),
("Dharavi","Dense"),
("Dubai","Burj"),
("Earth","Planet"),
("France","Wine"),
("Gotham City","Dark"),
("Germany","Autobahn"),
("Great Wall","Ancient"),
("Hogwarts","Wizards"),
("Houston","Space"),
("Istanbul","Bosporus"),
("Japan","Samurai"),
("Las Vegas","Gambling"),
("Legoland","Bricks"),
("London","Monarchy"),
("Los Angeles","Hollywood"),
("Madrid","Bullfight"),
("Manchester","Football"),
("Mars","Planet"),
("Mercury","Planet"),
("Metropolis","Heroes"),
("Mexico","Tacos"),
("Mexico City","Aztecs"),
("Miami","Beaches"),
("Mordor","Fire"),
("Mumbai","Spices"),
("Naples","Pizza"),
("Narnia","Wardrobe"),
("Neverland","Flying"),
("New York","Broadway"),
("North Korea","Dictator"),
("Orlando","Theme Park"),
("Oz","Emerald"),
("Paris","Romance"),
("Pisa","Leaning"),
("Poland","Pierogi"),
("Rio De Janeiro","Carnival"),
("Rome","Colosseum"),
("Russia","Vodka"),
("Sydney","Opera"),
("Spain","Flamenco"),
("Sun","Star"),
("Thailand","Elephants"),
("Tokyo","Sushi"),
("United Kingdom","Tea"),
("United States","Liberty"),
("Venice","Gondola"),
("Wakanda","Vibranium"),
("Washington D.C.","Congress"),
("Home","Comfort"),
("Moon","Satellite"),
("Jupiter","Planet"),
("Saturn","Planet"),
("Uranus","Planet"),
("Neptune","Planet"),
("Universal Studios","Rides"),
("SeaWorld","Marine")
]
items=[
("Door","Entrance"),
("Window","View"),
("Floor","Step"),
("Ceiling","Above"),
("Wall","Boundary"),
("Chair","Sit"),
("Table","Surface"),
("Lamp","Light"),
("Book","Read"),
("Cup","Drink"),
("Plate","Hold"),
("Spoon","Scoop"),
("Fork","Pierce"),
("Knife","Cut"),
("Bottle","Liquid"),
("Bag","Carry"),
("Shoes","Walk"),
("Hat","Head"),
("Coat","Warm"),
("Gloves","Hands"),
("Scarf","Neck"),
("Socks","Feet"),
("Pillow","Rest"),
("Blanket","Cover"),
("Bed","Sleep"),
("Curtains","Shade"),
("Brush","Clean"),
("Comb","Tidy"),
("Toothbrush","Teeth"),
("Toothpaste","Paste"),
("Towel","Dry"),
("Soap","Wash"),
("Shampoo","Hair"),
("Pan","Cook"),
("Pot","Boil"),
("Sponge","Scrub"),
("Bucket","Carry"),
("Broom","Sweep"),
("Rug","Floor"),
("Mat","Entry"),
("Clock","Time"),
("Phone","Call"),
("Wallet","Money"),
("Key","Unlock"),
("Notebook","Notes"),
("Pen","Write"),
("Pencil","Sketch"),
("Marker","Highlight"),
("Eraser","Correct"),
("Ruler","Measure"),
("Stapler","Bind"),
("Paperclip","Hold"),
("Chairleg","Support"),
("Doorknob","Twist"),
("Windowpane","Glass"),
("Shelf","Store"),
("Drawer","Slide"),
("Curtainrod","Hang"),
("Ceilingfan","Spin"),
("Lightbulb","Bright"),
("Switch","Toggle"),
("Outlet","Plug"),
("Remote","Control"),
("Cushion","Soft"),
("Trashcan","Dispose"),
("Basin","Wash"),
("Faucet","Flow"),
("Shower","Spray"),
("Bathtub","Soak"),
("Toilet","Flush"),
("Mirror","Reflect"),
("Doormat","Wipe"),
("Coatrack","Hang"),
("Windowblind","Cover"),
("Desk","Work")
]
activities=[
("Archery","Aim"),
("Baking","Heat"),
("Boxing","Strike"),
("Camping","Outdoors"),
("Canoeing","Stroke"),
("Climbing","Grip"),
("Cooking","Prepare"),
("Cycling","Ride"),
("Cycling","Road"),
("Dancing","Move"),
("Drawing","Lines"),
("Driving","Vehicle"),
("Fishing","Catch"),
("Flying","Air"),
("Golf","Swing"),
("Hiking","Trail"),
("Hiking Trail","Mountain"),
("Horse Riding","Saddle"),
("Ice Skating","Glide"),
("Jogging","Fitness"),
("Jogging","Park"),
("Jump Rope","Cord"),
("Kayaking","Stroke"),
("Martial Arts","Combat"),
("Painting","Color"),
("Photography","Lens"),
("Pilates","Core"),
("Basketball","Hoop"),
("Soccer","Goal"),
("Tennis","Racket"),
("Volleyball","Net"),
("Reading","Pages"),
("Rock Climbing","Crag"),
("Rollerblading","Wheels"),
("Rowing","River"),
("Running","Move"),
("Running Errands","Tasks"),
("Sailing","Boat"),
("Shopping","Store"),
("Skating","Slide"),
("Skiing","Snow"),
("Snowboarding","Slope"),
("Soccer Practice","Field"),
("Surfing","Wave"),
("Surfing Waves","Beach"),
("Swimming","Water"),
("Swimming","Pool"),
("Vacuuming","Floor"),
("Walking","Stroll"),
("Weightlifting","Lift"),
("Woodworking","Tools"),
("Yoga","Stretch"),
("Bird Watching","View"),
("Bowling","Roll"),
("Card Games","Deck"),
("Cleaning","Sort"),
("Cooking","Stove"),
("Crossfit","Strength"),
("Darts","Board"),
("Fishing","Lake"),
("Flying Drone","Remote"),
("Gardening","Soil"),
("Harvesting","Growth"),
("Hiking","Forest"),
("Horse Grooming","Brush"),
("Knitting","Yarn"),
("Painting","Brush"),
("Chess","Board"),
("Guitar","Strings"),
("Marathon","Track"),
("Skateboarding","Ramp"),
("Swimming Lessons","Instructor"),
("Table Tennis","Paddle"),
("Dog Walking","Leash"),
("Yoga","Mat")
]
school=[
("Art","Draw"),
("Assembly","Meet"),
("Backpack","Bag"),
("Binder","Hold"),
("Board","Show"),
("Book","Read"),
("Calculator","Calc"),
("Campus","Yard"),
("Chair","Sit"),
("Chalk","Mark"),
("Cafeteria","Food"),
("Cafeteria Tray","Carry"),
("Club","Join"),
("Compass","Circle"),
("Debate","Talk"),
("Desk","Work"),
("Drama","Act"),
("Easel","Stand"),
("Eraser","Rub"),
("Essay","Write"),
("Exam","Test"),
("Experiment","Mix"),
("Folder","Hold"),
("Geography","Map"),
("Hallway","Pass"),
("Highlighter","Mark"),
("History","Past"),
("Homework","Task"),
("Ink","Write"),
("Language","Words"),
("Laptop","Tech"),
("Lecture","Hear"),
("Library","Books"),
("Locker","Store"),
("Lunchbox","Food"),
("Marker","Mark"),
("Math","Calc"),
("Microscope","Zoom"),
("Music","Play"),
("Notebook Divider","Split"),
("Pen","Ink"),
("Pen Case","Hold"),
("Pencil","Point"),
("Pencil Sharpener","Point"),
("Physical education","Move"),
("Presentation","Show"),
("Project","Task"),
("Projector","Screen"),
("Protractor","Angle"),
("PE Kit","Gear"),
("Quiz","Test"),
("Reading","Read"),
("Recess","Break"),
("Research","Find"),
("Ruler","Line"),
("Rubber Bands","Stretch"),
("Scissors","Cut"),
("School Bell","Ring"),
("School Bus","Ride"),
("School Gym","Play"),
("Sports","Game"),
("Sports Field","Play"),
("Stapler","Bind"),
("Staple Remover","Pull"),
("Study group","Team"),
("Tape","Stick"),
("Textbook","Book"),
("Textbook Pages","Turn"),
("Timetable","Plan"),
("Volunteering","Help"),
("Whiteboard","Show"),
("Marker","Ink"),
("Writing","Write"),
("Teacher","Guide"),
("Test","Paper")
]
miscellaneous=[
("Baking","Warm"),
("Beach","Open"),
("Bonfire","Glow"),
("Camping","Adventure"),
("Candles","Flicker"),
("Cards","Chance"),
("Caroling","Tune"),
("Chocolate Eggs","Sweet"),
("Christmas","Joy"),
("Costumes","Mask"),
("Cycling","Move"),
("Diwali","Bright"),
("Easter","Spring"),
("Fireworks","Spark"),
("Fishing","Wait"),
("Gathering","People"),
("Gifts","Wrap"),
("Halloween","Night"),
("Hanukkah","Light"),
("Hiking Trail","Walk"),
("Ice Skating","Glide"),
("Mountains","Peak"),
("Museum Visit","Explore"),
("New Year","Celebrate"),
("Ornaments","Decor"),
("Parade","March"),
("Passport","Travel"),
("Picnic","Relax"),
("Picnic Blanket","Sit"),
("Relaxing","Pause"),
("Road Trip","Drive"),
("Shopping","Buy"),
("Skiing","Slide"),
("Sledding","Fun"),
("Snowball Fight","Throw"),
("St. Patrick's Day","Green"),
("Suitcase","Pack"),
("Sunglasses","Shade"),
("Sunscreen","Protect"),
("Surfing","Balance"),
("Swimming","Move"),
("Thanksgiving","Family"),
("Traveling","Journey"),
("Turkey","Meal"),
("Valentine's Day","Heart"),
("Politics","Power"),
("Fear","Feeling"),
("Thought","Mind"),
("Knowledge","Learn"),
("Memory","Recall"),
("Dreams","Imagine"),
("Wisdom","Guide"),
("Justice","Fair"),
("Courage","Brave"),
("Freedom","Choice"),
("Adventure","Excite"),
("Challenge","Test"),
("Journey","Path"),
("Music","Sound"),
("Art","Color"),
("Game","Play"),
("Strategy","Plan"),
("Luck","Chance"),
("Surprise","Shock"),
("Light","Glow"),
("Shadow","Dark"),
("Mystery","Unknown"),
("Secret","Hidden"),
("Idea","Spark"),
("Hope","Wish"),
("Peace","Calm"),
("Emotion","Feel"),
("Energy","Move"),
("Time","Pass"),
("Space","Vast"),
("Civilian","Impostor"),
("Impostor","YOU"),
("Game","Impostor"),
("fx-CG50","THIS")
]
datasets = {
    "1": places,
    "2": items,
    "3": activities,
    "4": school,
    "5": miscellaneous
    }
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
    print("Choose an option:")
    print("1 - Places")
    print("2 - Items")
    print("3 - Activities")
    print("4 - School")
    print("5 - Miscellaneous")
    print("Option(1-5):")
    def valid_choice(datasets):
        while True:
            choice = input().strip()
            if choice == "" or choice not in datasets:
                print("Enter a number(1-5):\n")
                continue
            data = datasets[choice]
            word, hint = random.choice(data)
            return word, hint
    word, hint = valid_choice(datasets)    
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
    "Press - then EXE\n" \
    "When ready")
    if input() == "-":  
        for n in imps:
            print("Impostor:",names[n])
#By Arpith Nair
#14/11/2025