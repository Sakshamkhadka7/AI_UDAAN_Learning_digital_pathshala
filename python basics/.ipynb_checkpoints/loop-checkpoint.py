
# for i in range(2,11,4):
#     print(i)


countries=['japan','brazil','norway']

for country in countries:
    print(country)

predictions_score=[70,90,21,50,60,99,95,91]

for score in predictions_score:
    if score > 80:
        print(score,"Good score")
    else:
        print(score,"Bad score")


email_lists=[
    "Bhatbateni ma 100 percent discount",
    "congratulation you won iphone",
    "what is your bank details",
    "what is your email password",
    "Tomorrow is meeting at 5 am"
]


for email in email_lists:
    if "congratulation" in email or "email" in email or "discount" in email or "won" in email:
        print("Email is scam : ",email)
    else:
        print("Not scam : ",email)