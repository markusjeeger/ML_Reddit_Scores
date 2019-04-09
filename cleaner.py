from nltk.stem import PorterStemmer

st = PorterStemmer()
bad_file_name = "/Users/boro/school/Year4/CPS840/Project/posts.csv"
good_file_name = "/Users/boro/school/Year4/CPS840/Project/posts_clean.csv"

category_words = {}

category_words["work"] = list(map(lambda x: st.stem(x), "work/office/boss/job/project/presentation/fired/hired/promote/demote/company/business/secretary".split("/")))
category_words["school"] = list(map(lambda x: st.stem(x), "school/teacher/professor/class/student/homework/assignment/college/university/uni".split("/")))
category_words["home"] = list(map(lambda x: st.stem(x), "home/house/apartment/condo".split("/")))
category_words["boyfriend"] = list(map(lambda x: st.stem(x), "boyfriend/husband".split("/")))
category_words["girlfriend"] = list(map(lambda x: st.stem(x), "girlfriend/wife".split("/")))
category_words["pet"] = list(map(lambda x: st.stem(x), "pet/dog/cat/fish/bird/hamster/deer/vet".split("/")))
category_words["sex"] = list(map(lambda x: st.stem(x), "sex/porn/ass/cunt/dick/vagina/penis/cum/semen/squirt/pussy/bum/butt/head".split("/")))
category_words["food"] = list(map(lambda x: st.stem(x), "food/drink/eat/ate/munch/hungry/restaurant".split("/")))
category_words["body_fluids"] = list(map(lambda x: st.stem(x), "vomit/puke/shit/diarrhea/piss/pee/blood/pus/flem/phlegm".split("/")))
category_words["police"] = list(map(lambda x: st.stem(x), "police/cop/officer/handcuff/arrested/jail/prison/fuzz".split("/")))
category_words["hospital"] = list(map(lambda x: st.stem(x), "medical/hospital/doctor/nurse".split("/")))
category_words["car"] = list(map(lambda x: st.stem(x), "car/truck/suv/taxi/uber/bike/skateboard/boat/scooter".split("/")))
category_words["public_transit"] = list(map(lambda x: st.stem(x), "bus/subway/train".split("/")))
category_words["shop"] = list(map(lambda x: st.stem(x), "store/shop".split("/")))
category_words["bathroom"] = list(map(lambda x: st.stem(x), "bathroom/shower/toilet/bath".split("/")))
category_words["body"] = list(map(lambda x: st.stem(x), "body/arm/finger/foot/head/mouth".split("/")))
category_words["gun"] = list(map(lambda x: st.stem(x), "gun/rifle/bullet/shot/shoot".split("/")))
category_words["fire"] = list(map(lambda x: st.stem(x), "fire/explosion/boom/bang".split("/")))
category_words["drugs"] = list(map(lambda x: st.stem(x), "drugs/weed/high/coke/meth/marijuana/acid/ectasy/joint/adderal/beer/wine/liquor/alcohol/dope/munchies".split("/")))
category_words["death"] = list(map(lambda x: st.stem(x), "funeral/dead/grandma/grandpa/corpse/urn/ashes/killed".split("/")))


bad = open(bad_file_name, "r")
good = open(good_file_name, "a+")


good.write("""
Post ID,
Post Year,
Post Month,
Post Day,
Post Hour,
Post Minute,
Post Second,
Post Day of Week,
Post Score,
Permalink,
Post Comments,
Post NSFW,
Post Title Length,
Post Body Length,
Post Title,
Post Body,
Author Name,
Author ID,
Author Comment Karma,
Author Link Karma,
Author Is Gold,
Author Year,
Author Month,
Author Day,
Author Hour,
Author Minute,
Author Second,
Work,
School,
Home,
Boyfriend,
Girlfriend,
Pet,
Sex,
Food,
Bodily Fluids,
Police,
Hospital,
Car,
Public Transit,
Shop,
Bathroom,
Body,
Gun,
Fire,
Drugs,
Death\n
""".replace('\n', ''))

for line in bad:
    category_count = {}
    line_split = line.split(",")
    if len(line_split) != 27:
        continue
    if line_split[15] == "removed":
        continue
    if line_split[15] == "":
        continue

    for word in line_split[15].split(" "):
        for category, words in category_words.items():
            if st.stem(word) in words:
                if category in category_count:
                    category_count[category] += 1
                else:
                    category_count[category] = 1

    line = line.strip()
    for category in category_words:
        line += "," + str(category_count.get(category, 0))

    line += "\n"
    good.write(line)

bad.close()
good.close()

