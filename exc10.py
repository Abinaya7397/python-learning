print("****online food order****")
print("categery : \nveg  \nnon veg")
print("in veg  =curd rice, lemon rice, tomato rice  \n in non veg =chiken rice,egg rice,tandoori")
your_list=input("enter a categery : ")
your_item=input("enter a categery chooies : ")
how_many=int(input("enter a number : "))
one_curd_rice=50
one_lemon_rice=40
one_tomato_rice=60
one_chiken_rice=160
one_egg_rice=100
one_tendoori=200
categery=["veg","non veg"]
veg=["curd rice","lemon rice","tomato rice"]
nonveg=["chiken rice","egg rice","tendoori"]
if your_list in categery:
    if your_list =="veg":
        if your_item =="lemon rice":
           print(f"yes! {your_item} is avalible and cost of lemon rice  {one_lemon_rice}")
           lemonrice=one_lemon_rice*how_many
           gst=lemonrice*20/100
           total_price=lemonrice+gst
           print(f" your lemonrice price with gst {total_price}")
        elif your_item =="curd rice":
           print(f"yes! {your_item} is avalible and cost of curd rice  {one_curd_rice}")
           curdrice=one_curd_rice*how_many
           gst=curdrice*20/100
           total_price=curdrice+gst
           print(f" your curdrice price with gst {total_price}")
        elif your_item =="tomato rice":
           print(f"yes! {your_item} is avalible and cost of tomato rice  {one_tomato_rice}")
           tomatorice=one_tomato_rice*how_many
           gst=tomatorice*20/100
           total_price=tomatorice+gst
           print(f" your tomatorice price with gst {total_price}")
        elif your_list == "non veg":
         if  your_item == "chiken rice":
           print(f"yes! {your_item} is avalible and cost of chiken rice  {one_chiken_rice}")
           chikenrice=one_chiken_rice*how_many
           gst=chikenrice*10/100
           total_price=chikenrice+gst
           print(f" your chikenrice price with gst {total_price}")
        elif  your_item == "egg rice":
           print(f"yes! {your_item} is avalible and cost of egg rice  {one_egg_rice}")
           eggrice=one_egg_rice*how_many
           gst=eggrice*10/100
           total_price=eggrice+gst
           print(f" your eggrice price with gst {total_price}")
        elif  your_item == "tendoori":
           print(f"yes! {your_item} is avalible and cost of chiken rice  {one_chiken_rice}")
           tendoori=one_tendoori*how_many
           gst=tendoori*10/100
           total_price=tendoori+gst
           print(f" your tendoori price with gst {total_price}")
   
   
       



