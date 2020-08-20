
import pyttsx3
pyttsx3.speak("Welcome to my program to see Status of Top 10 worst affected countries by COVID19")
print("Welcome to my program to see Status of Top 10 worst affected countries by COVID19")
print()

pyttsx3.speak("Press 1 for status of USA")
print("Press 1 for status of USA")
pyttsx3.speak("Press 2 for status of Brazil")
print("Press 2 for status of Brazil")
pyttsx3.speak("Press 3 for status of India")
print("Press 3 for status of India")
pyttsx3.speak("Press 4 for status of Russia")
print("Press 4 for status of Russia")
pyttsx3.speak("Press 5 for status of South Africa")
print("Press 5 for status of South Africa")
pyttsx3.speak("Press 6 for status of Peru")
print("Press 6 for status of Peru")
pyttsx3.speak("Press 7 for status of Mexico")
print("Press 7 for status of Mexico")
pyttsx3.speak("Press 8 for status of Colombia")
print("Press 8 for status of Colombia")
pyttsx3.speak("Press 9 for status of Chile")
print("Press 9 for status of Chile")
pyttsx3.speak("Press 10 for status of Spain")
print("Press 10 for status of Spain")




print()
print()
a=int(input("Please enter your Choice:"))
print()
print()
pyttsx3.speak("Please wait")
print("Please Wait......")

from covid import Covid
covid = Covid()

#for usa -------------
us = covid.get_status_by_country_name("US") 
conf ={
    key:us[key] 
    for key in us.keys() and {'confirmed'}}                               

act ={
    key:us[key] 
    for key in us.keys() and {'active'}}

rec ={
    key:us[key] 
    for key in us.keys() and {'recovered'}}

det ={
    key:us[key] 
    for key in us.keys() and {'deaths'}}

to ={
    key:us[key] 
    for key in us.keys() and {'confirmed' , 
                                'active'  ,  
                                'recovered'  ,
                                'deaths' }
}                               



#for brazil------------
b = covid.get_status_by_country_name("Brazil") 
  
conf2 ={
    key:b[key] 
    for key in b.keys() and {'confirmed'}}                               

act2 ={
    key:b[key] 
    for key in b.keys() and {'active'}}

rec2 ={
    key:b[key] 
    for key in b.keys() and {'recovered'}}

det2 ={
    key:b[key] 
    for key in b.keys() and {'deaths'}}

to2 ={
    key:b[key] 
    for key in b.keys() and {'confirmed' , 
                                'active'  ,  
                                'recovered'  ,
                                'deaths' }
}                               




#for india------------
i = covid.get_status_by_country_name("India") 
  
conf3 ={
    key:i[key] 
    for key in i.keys() and {'confirmed'}}                               

act3={
    key:i[key] 
    for key in i.keys() and {'active'}}

rec3 ={
    key:i[key] 
    for key in i.keys() and {'recovered'}}

det3 ={
    key:i[key] 
    for key in i.keys() and {'deaths'}}

to3 ={
    key:i[key] 
    for key in i.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered'  ,
                                'deaths' }
}                               



#for russia-----------
r = covid.get_status_by_country_name("Russia") 
  
conf4 ={
    key:r[key] 
    for key in r.keys() and {'confirmed'}}                               

act4={
    key:r[key] 
    for key in r.keys() and {'active'}}

rec4 ={
    key:r[key] 
    for key in r.keys() and {'recovered'}}

det4 ={
    key:r[key] 
    for key in r.keys() and {'deaths'}}

to4 ={
    key:r[key] 
    for key in r.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for south africa--------
sa = covid.get_status_by_country_name("South Africa") 
conf5 ={
    key:sa[key] 
    for key in sa.keys() and {'confirmed'}}                               

act5 ={
    key:sa[key] 
    for key in sa.keys() and {'active'}}

rec5 ={
    key:sa[key] 
    for key in sa.keys() and {'recovered'}}

det5 ={
    key:sa[key] 
    for key in sa.keys() and {'deaths'}}

to5 ={
    key:sa[key] 
    for key in sa.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for peru-------------
p= covid.get_status_by_country_name("Peru") 
conf6 ={
    key:p[key] 
    for key in p.keys() and {'confirmed'}}                               

act6 ={
    key:p[key] 
    for key in p.keys() and {'active'}}

rec6 ={
    key:p[key] 
    for key in p.keys() and {'recovered'}}

det6 ={
    key:p[key] 
    for key in p.keys() and {'deaths'}}

to6 ={
    key:p[key] 
    for key in p.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for mexico----------
m = covid.get_status_by_country_name("Mexico") 
conf7 ={
    key:m[key] 
    for key in m.keys() and {'confirmed'}}                               

act7 ={
    key:m[key] 
    for key in m.keys() and {'active'}}

rec7 ={
    key:m[key] 
    for key in m.keys() and {'recovered'}}

det7 ={
    key:m[key] 
    for key in m.keys() and {'deaths'}}

to7 ={
    key:m[key] 
    for key in m.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for colombia---------
c = covid.get_status_by_country_name("Colombia") 
conf8 ={
    key:c[key] 
    for key in c.keys() and {'confirmed'}}                               

act8 ={
    key:c[key] 
    for key in c.keys() and {'active'}}

rec8 ={
    key:c[key] 
    for key in c.keys() and {'recovered'}}

det8 ={
    key:c[key] 
    for key in c.keys() and {'deaths'}}

to8 ={
    key:c[key] 
    for key in c.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for chile-------------
ch = covid.get_status_by_country_name("Chile") 
conf9 ={
    key:ch[key] 
    for key in ch.keys() and {'confirmed'}}                               

act9 ={
    key:ch[key] 
    for key in ch.keys() and {'active'}}

rec9 ={
    key:ch[key] 
    for key in ch.keys() and {'recovered'}}

det9 ={
    key:ch[key] 
    for key in ch.keys() and {'deaths'}}

to9 ={
    key:ch[key] 
    for key in ch.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               



#for spain--------------
s = covid.get_status_by_country_name("Spain") 
conf10 ={
    key:s[key] 
    for key in s.keys() and {'confirmed'}}                               

act10 ={
    key:s[key] 
    for key in s.keys() and {'active'}}

rec10 ={
    key:s[key] 
    for key in s.keys() and {'recovered'}}

det10 ={
    key:s[key] 
    for key in s.keys() and {'deaths'}}

to10 ={
    key:s[key] 
    for key in s.keys() and {'confirmed' , 
                                'active' ,  
                                'recovered' ,
                                'deaths' }
}                               








pyttsx3.speak("Press 1 to see Confirmed cases")
pyttsx3.speak("Press 2 to see Active cases")
pyttsx3.speak("Press 3 to see Recovered cases") 
pyttsx3.speak("Press 4 to see Deaths ")
pyttsx3.speak("Press 5 to see Total cases")


if a==1:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf)
    elif b==2:
            print(act)
    elif b==3:
            print(rec)
    elif b==4:
            print(det)
    elif b==5:
            print(to)
    else:
        print("INVALID CHOICE!!!!")
elif a==2:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf2)
    elif b==2:
            print(act2)
    elif b==3:
            print(rec2)
    elif b==4:
            print(det2)
    elif b==5:
            print(to2)
    else:
        print("INVALID CHOICE!!!!")

elif a==3:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf3)
    elif b==2:
            print(act3)
    elif b==3:
            print(rec3)
    elif b==4:
            print(det3)
    elif b==5:
            print(to3)
    else:
        print("INVALID CHOICE!!!!")
elif a==4:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf4)
    elif b==2:
            print(act4)
    elif b==3:
            print(rec4)
    elif b==4:
            print(det4)
    elif b==5:
            print(to4)
    else:
        print("INVALID CHOICE!!!!")
elif a==5:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf5)
    elif b==2:
            print(act5)
    elif b==3:
            print(rec5)
    elif b==4:
            print(det5)
    elif b==5:
            print(to5)
    else:
        print("INVALID CHOICE!!!!")
elif a==6:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf6)
    elif b==2:
            print(act6)
    elif b==3:
            print(rec6)
    elif b==4:
            print(det6)
    elif b==5:
            print(to6)
    else:
        print("INVALID CHOICE!!!!")
elif a==7:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf7)
    elif b==2:
            print(act7)
    elif b==3:
            print(rec7)
    elif b==4:
            print(det7)
    elif b==5:
            print(to7)
    else:
        print("INVALID CHOICE!!!!")
elif a==8:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf8)
    elif b==2:
            print(act8)
    elif b==3:
            print(rec8)
    elif b==4:
            print(det8)
    elif b==5:
            print(to8)
    else:
        print("INVALID CHOICE!!!!")
elif a==9:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf9)
    elif b==2:
            print(act9)
    elif b==3:
            print(rec9)
    elif b==4:
            print(det9)
    elif b==5:
            print(to9)
    else:
        print("INVALID CHOICE!!!!")
elif a==10:
    print("Press 1 to see Confirmed cases")
    print("Press 2 to see Active cases")
    print("Press 3 to see Recovered cases") 
    print("Press 4 to see Deaths ")
    print("Press 5 to see Total cases")
    print()
    print()
    b=int(input("Please enter your Choice:"))
    if b==1:
            print(conf10)
    elif b==2:
            print(act10)
    elif b==3:
            print(rec10)
    elif b==4:
            print(det10)
    elif b==5:
            print(to10)
    else:
        print("INVALID CHOICE!!!!")
else:
    print("INVALID CHOICE!!!!")

print()
print()
pyttsx3.speak("thank for using this program")
print("Thank You")
print()
print()
x=int(input("Press any number to exit this program:"))
print()
if x==0:
    exit()
else:
    exit()



