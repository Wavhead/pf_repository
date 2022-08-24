import random
import time

def choiceGame():
    user_choice = ""

    print("Welcome to the Choose Your Own Adventure Game!")
    time.sleep(1)

    print("The rules are as follows:")
    time.sleep(1)

    print("1. When prompted, you will choose one of the choices you are given.")
    time.sleep(1)

    print("2. When a question doesn't have a choice you will answer as you see fit.")
    time.sleep(1)

    print("3. To make a choice you input the number next to the choice you wish to choose.")
    time.sleep(1)

    print("4. Finally, the choices you make can have consequences that might not be appearant.")
    time.sleep(1)

    print("-------------------------------------------------------------------------------------------")
    print("The Choose Your Own Adventure Game is now starting!")
    time.sleep(1)
    print("MISSON: Survive the day!")
    time.sleep(1)

    print("You're woken up by your alarm, it's 7:00 in the morning.")
    time.sleep(1)
    user_choice = input("(1)Get up or (2)Sleep : ")

    if user_choice == "1":
        print("You get out of bed...")
        time.sleep(1)
        user_choice = input("Go to work? (1)y / (2)n : ")

        if user_choice == "1":
            print("You go to work...")
            time.sleep(1)
            print("When you arrive, at work you're tired...")
            time.sleep(1)
            user_choice = input("Do want (1)Coffee or (2)not? : ")

            if user_choice == "1":
                print("You get a cup of coffee...")
                time.sleep(1)
                print("You're ready for work!")
                time.sleep(1)
                user_choice = input("Do you go to (1)your desk or (2)visit coworkers? : ")

                if user_choice == "1":
                    print("You sit down at your desk...")
                    time.sleep(1)
                    user_choice = input("Do you (1)start working or (2)not? : ")

                    if user_choice == "1":
                        print("You open your worksheet and start checking boxes...")
                        time.sleep(1)
                        print("Your job is to decide who to concider hiring at your company...")
                        time.sleep(1)

                        applicant_ID = random.randint(0, 3)
                        if applicant_ID == 0:
                            print("The first applicant is a 97 year old man")
                            time.sleep(1)
                            print("They don't know what a computer is")
                            time.sleep(1)
                            print("And applied for this job on accident")
                            time.sleep(1)
                            user_choice = input("Do you (1)hire them or (2)not? : ")

                            if user_choice == "1":
                                print("You approve their application...")
                                time.sleep(1)
                                print("Having worked very hard, you lean back in your chair")
                                time.sleep(1)
                                print("Suddenly you get a call from The Boss")
                                time.sleep(1)
                                user_choice = input("Do you (1)answer the phone or (2)not? : ")

                                if user_choice == "1":
                                    print("You answer the phone...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("After a lenghty rant from your boss they hang up...")
                                    time.sleep(1)
                                    print("Your applicant somehow manage to install 720 viruses on a company computer...")
                                    time.sleep(1)
                                    print("AND YOU'RE FIRED!")
                                    #####################################
                                    ### GAME OVER #######################
                                    #####################################

                        elif applicant_ID == 1:
                            print("The first applicant is a 21 year old woman")
                            time.sleep(1)
                            print("They have experience in wordpress and html")
                            time.sleep(1)
                            print("And have been applying to this job for the past 5 years")
                            time.sleep(1)
                            user_choice = input("Do you (1)hire them or (2)not? : ")

                            if user_choice == "1":
                                print("You approve their application...")
                                time.sleep(1)
                                print("Having worked very hard, you lean back in your chair")
                                time.sleep(1)
                                print("Suddenly you get a call from The Boss")
                                time.sleep(1)
                                user_choice = input("Do you (1)answer the phone or (2)not? : ")

                                if user_choice == "1":
                                    print("You answer the phone...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("After a short speech from your boss they hang up...")
                                    time.sleep(1)
                                    print("Your applicant managed to find a privacy breach on your company website that made all your passwords public...")
                                    time.sleep(1)
                                    print("P.S. You got a promotion!")
                                    time.sleep(1)
                                    print("Your now in charge of choosing who gets a promotion a your company...")
                            
                        elif applicant_ID == 2:
                            print("The first applicant is a 31 year old man")
                            time.sleep(1)
                            print("They have a background in server managment")
                            time.sleep(1)
                            print("And want to have access to your company's main servers")
                            time.sleep(1)
                            user_choice = input("Do you (1)hire them or (2)not? : ")

                            if user_choice == "1":
                                print("You approve their application...")
                                time.sleep(1)
                                print("Having worked very hard, you lean back in your chair")
                                time.sleep(1)
                                print("Suddenly you get a call from The Boss")
                                time.sleep(1)
                                user_choice = input("Do you (1)answer the phone or (2)not? : ")

                                if user_choice == "1":
                                    print("You answer the phone...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("After a lenghty rant from your boss they hang up...")
                                    time.sleep(1)
                                    print("Your applicant was sent by a rival company and has bricked your servers...")
                                    time.sleep(1)
                                    print("AND YOU'RE FIRED!")
                                    #####################################
                                    ### GAME OVER #######################
                                    #####################################
                            
                        elif applicant_ID == 3:
                            print("The first applicant is a 8 year old girl")
                            time.sleep(1)
                            print("They have used a phone")
                            time.sleep(1)
                            print("And have been sending spam applications to various tech companies like yours")
                            time.sleep(1)
                            user_choice = input("Do you (1)hire them or (2)not? : ")

                            if user_choice == "1":
                                print("You approve their application...")
                                time.sleep(1)
                                print("Having worked very hard, you lean back in your chair")
                                time.sleep(1)
                                print("Suddenly you get a call from The Boss")
                                time.sleep(1)
                                user_choice = input("Do you (1)answer the phone or (2)not? : ")

                                if user_choice == "1":
                                    print("You answer the phone...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("After a lenghty rant from your boss they hang up...")
                                    time.sleep(1)
                                    print("Your applicant has replaced your company homepage with a picture of a cat, and deleted all your packups...")
                                    time.sleep(1)
                                    print("AND YOU'RE FIRED!")
                                    #####################################
                                    ### GAME OVER #######################
                                    #####################################

                elif user_choice == "2":
                    print("You walk over to Dave...")
                    time.sleep(1)
                    print("He starts talking to you about how the temperature of water determines its taste...")
                    time.sleep(1)
                    print("You suddenly remember why you don't talk to Dave often")
                    time.sleep(1)
                    print("You start waling back to your desk when you get a call from The Boss...")
                    time.sleep(1)
                    print("YOU'RE FIRED!")

            elif user_choice == "2":
                print("You dont need coffee...")
                time.sleep(1)
                print("The moment you sit down in your chair, you fall asleep")
                time.sleep(1)
                print("YOU'RE FIRED!")
                #####################################
                ### GAME OVER #######################
                #####################################

        elif user_choice == "2":
            print("You go to the pub...")
            time.sleep(1)
            print("At exactly 8:01 you get a call from The Boss...")
            time.sleep(1)
            print("YOU'RE FIRED")
            #####################################
            ### GAME OVER #######################
            #####################################

    elif user_choice == "2":
        print("You stay in bed...")
        time.sleep(1)
        print("At exactly 8:01 you get a call from The Boss...")
        time.sleep(1)
        print("YOU'RE FIRED")
        #####################################
        ### GAME OVER #######################
        #####################################

choiceGame()