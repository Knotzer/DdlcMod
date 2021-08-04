label story:
mc "Ugh..."
"And thus begins another school day."
"And as usual, it starts..."
"With a searing headache."
"I hop out of bed, stumbling slightly."
"I grab a bottle of Ibuprofen from my nightstand and take one with a glass of lukewarm (but at least refreshing) water."
"I begin to get ready for school."
scene bg residential_day
s "[player]! There you are. What took you so long?"
"Sayori's voice rings out from the direction her house is in."
show sayori 1c at t11
"The bright-eyed girl seems overjoyed, as usual."
mc "Sorry, I got caught up with something."
"Sayori gives me a curious look."
show sayori 1b at t11
s "Ooh, with what?"
mc "None of your business, that's what."
s 4j "Hey, that was mean!"
"I realize a bit too late that that could be rude."
mc "I'm sorry, I have a really bad headache."
s "I understand."
s 1a "Well, let's just go to school. We're gonna be late if we stall any longer."
mc "Alright."
scene bg corridor
"Testing."
"God, so much testing."
"With the blessing of semester's end, the curse of countless tests looms over the entire school."
"After a long day of guessing my way through said tests, I walk into the Literature Club."
scene bg club_day
"I'm greeted by the usual scene."
show monika 1a at t41
"Monika..."
show sayori 1a at t42
"Sayori..."
show natsuki 1a at t43
"Natsuki..."
show yuri 1a at t44
"And Yuri."
"Everyone seemed to be talking, but that ceased as I entered."
"This is unusual..."
mc "Hey guys, what's going on?"
m 2k "Oh, hey, [player]!"
mc "What are you guys talking about?"
m 2m "N-nothing, don't worry about it."
"I notice Nat and Yuri are still whispering to each other, but I can't hear them."
mc "Alright..."
"Weird."
"I notice the absence of any clear club activity."
"Monika usually has them working by now."
m 2l "Anyways, how has life been, [player]?"
mc "Busy, as usual, but fine other than that. How about you, Monika?"

m 4n "Fine..."
m "Just fine, [player]."
"She says this with a hint of worry in her voice, and I can't help but wonder what for.."
"I'll try to talk to her about it later, but for now I'll catch up with Sayori."
"She went on a camping trip for a week, so I figure I'll ask about it."
mc "Hey, Sayori, how was your trip?"
s 1a "Oh, it was good, kinda boring though."
mc "Ah, yeah."
mc "Hey, uh... did anything happen to Monika while I was gone?"
s 1j "Actually, I was wondering that too... she's been acting weird all day, so either something's up or it's that time of the month."
"Good, it's not just me."
mc "Glad you noticed."
mc "I think we should ignore it for now, she clearly doesn't walk to talk about it, so let's ignore it unless it gets worse."
s 2j "Yeah your probably right."
"I just remembered how what happened when i walked in, so I decide to ask her about it."
mc "Also, what where you guys talking about today when I walked in?"
s 1l "N-nothing."
"It's obvious she doesn't want me knowing, but after school maybe I can manage to get it out of her."
"Not like I have anything better to do."
mc "He, do you mind if I come over to your house after school?"
s 1r "Not at all!"
mc "Alright."
hide sayori
hide natsuki
hide yuri
hide monika
"The rest of the day is pretty much normal, with Sayori getting embarassed over something and Natsuki getting mad at Monika for something dumb."
"The bell rings, the day ends and me and Sayori head out."
show bg house
"We make it to Sayori's place, and head inside."
show bg sayori_bedroom
show sayori 2bi at t11
play music t9
s "Sorry it's so dirty..."
mc "Don't worry about it, I'm not much better."
show sayori 1ba at t11
s "Fair enough."
"I cut right to the chase."
mc "Sayori..."
s 1bc "Yeah?"
mc "Answer me honestly... what were you guys talking about when I came in?"
s 5ba "Uhh..."
"Sayori looks away."
s "W-well, the thing is..."
s "I, uh..."
s "I..."
"..."
s "Fuck it... I love you, [player]. I really do..."
show sayori 1bp at t11
hide sayori with moveoutleft
"Sayori averts her eyes, and runs out of the room faster than I can process what happened."
mc "Sayori..."
play music t1
scene white
show splash_warning "just kidding" with Dissolve(0.5, alpha=True)
$ pause(1.0)
show splash_warning "or am i?" with Dissolve(0.1, alpha=True)
play music t9
$ pause(0.3)

show bg sayori_bedroom
show sayori 3bu at t11
s "Well... I suppose there's no hiding it anymore."
s "I've been going through a tough depression for a few years... after a close friend..."
"I nod."
"How in the fuck did I never realize?"
mc "Sayori..."
"What do I say?"
"I need to help her..."
mc "Look. I know it's not as simple as just cheering up, but I want you to know that I'll be there for you for as long as you need."
s 4bu "T-thanks, [player]."
s "Thanks so much."
mc "Of course, Sayori."
hide sayori
"I wish there was more I could do to help... but I suppose we'll just have to see what happens."
"As much as I wish I could stay, the adult life is busy."
"I go home, and go to bed." 
show bg bedroom
"Damn, this day was weird."
show bg class_day with wipeleft
"Its a new day, which is really scary and really exciting at the same time."
"I still havent really processed what sayori said to me."
"I rush through my classes just to see sayori, its a sense of urgency i have never experienced before. "
"It's extremely bizzare."
show bg corridor
"Finally It's time to see the club members."
show bg club_day
mc "Guess who is back?"
show monika 1a at t41
"Your here everyday."
show sayori 1a at t42
"Yeah."
show natsuki 1a at t43
"Im tired."
"The fact that was out of place tells me she was pretty tired."
show yuri 1a at t44 
"But im glad you are here, you have never missed a day!"
mc "thank you yuri."
"Now that i think of it, she is right, i have never missed a day."
m 3bu "well everyone..."
m "today we will be writing Poems!"
"this is what we do alomost everyday. but im fine with it"
hide sayori
hide natsuki
hide yuri
hide monika
label Game_Poem_1:
menu:
    "for who will you write the poem for?"
    "Sayori":
        $ For_Sayori = True
        "i will write a poem only for the person i care for most in this club."
        "well... i guess sayori likes cute things? thats all i can really think of."
        "i think i got a idea..."
    "Yuri":
        $ For_Yuri = True
        "i will write one for yuri because i like her writing style."
        "this is gonna take awhile..."
        "but i think it will turn out okay."
    "Monika":
        $ For_Monika = True
        "maybe i can impress the president of the club, that would be kinda cool."
        "guess I gotta use 100% of my brain to impress her."
    "Natsuki":
        $ For_Natsuki = True
        "This is pretty much the easy route, i dont wanna think too hard."
"alright lets go show  these poems to people."
menu:
    "who shouldi show it to first?"
    "Sayori":       
    if For_Sayori = True:
        s 1n "Ohhhh, This One is My Favorite!!"
        mc "Im glad you like it Sayori."
        s 1s "Of course I do!, I like Everything you do!"
        mc "you know I wrote it for you, right?"
        s 1m "Ehh, You did?"
        mc "of course i did, after all your my favorite person!"
        s 1j "Ehhh? Not Even your family?"
        mc "Sayori... you know my family wasent ever really there, even when they were, they were very dissaproving of everything i do, so yes."
        s 1v "I... im sorry..."
        mc "its alright Sayori, i see why you said that."
        s 1u "ill make sure im the best person i can be for you.."
        mc "Sayori... you know you already are, you are already perfect.."
        s 2u "is that really true?"
        mc "yes, of course it is."
        s 1t "Thank you [player]."
        mc "Your welcome Sayori."
        call Game_Poem_1
    if For_Sayori = False:
        s 1n "woww, this is pretty good!"


        call Game_Poem_1

    "Yuri":
    "Monika":
    "Natsuki":
    "Done":   
end label:     
















