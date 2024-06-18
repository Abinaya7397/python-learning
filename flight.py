def ticket():
    print("counter 1 :")
    tic=input("result the ticket checking : ")
    con=input("do you want contine press yes :")
    if con =="yes":
        print("if the contion is true na go an counter 2")
        ticket()
    else:
        print("sorry! invalid ticket")
def covid_19():
    print("counter two check covid 19 ")
    vac=input("test the covid result :")
    if vac=="positive":
        print(" okay! give the certificate")
        covid_19()
    else:
        print("not allowed! ")
def innegration_checking():
    print("chech your visa and pasport")
    visa=input("test vis : ")
    if visa== "true":
        print("okay! give ang profe")
        innegration_checking()
    else:
        print("visa is duplicate!")
def bag_wait_checking():
    print("check the bag wait  is only 200kg")
    bag=int(input("kg of bag wait : "))
    if bag==200:
        print('okay! no charge')
        bag_wait_checking()
    else :
        print("bless give a charge amt 200")
def boarding_pass_checking():
    print("seal verification and seat allocation")
    seal=input(" seal the visa and pasport : ")
    if seal =="yes":
        print("allocate the seat no 45")
        boarding_pass_checking()
    else:
        print(" not allowed the flight so you can go ") 
        def main() :               
         print("***ariport checking***")
         print("'ncounter 1: ticket \ncounter 2: covid 19 \ncounter 3 :innegration checking \ncounter 4 : bag wait checking \ncounter 5 : boardong pass check")
         user=int(input("enter a counter : "))
         if user==1:
           ticket()
         elif user==2:
           covid_19()
         elif user==3:
             innegration_checking()
         elif user==4:
            bag_wait_checking()
         elif user==5:
            boarding_pass_checking()
         else:
             print("sorry! pless enter the counter 1 2 3 4 5 only")
        main()
ticket()
covid_19()
innegration_checking()
bag_wait_checking()
boarding_pass_checking()



