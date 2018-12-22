#!/usr/bin/env python3
# Final Project
# Anna Kovneva
# Nov 29,2016
#This program will combine different features to produce a final Birth Test

import webbrowser
import turtle
import akovneva_finalchyr_para #import chinese year para
import akovneva_bypara #import of birthtest paragraphs
import akovneva_finalhtml_stuff #import stuff for CSS
import akovneva_wezpara #import western zodiac para

#sequence(ask user for data)
fname=turtle.textinput("Name","What is your name?\n")
month=int(turtle.numinput("Month","Enter your birth month \n",1,minval=1, maxval=12))
day=int(turtle.numinput("Day","Enter your birthday day \n",1,minval=1, maxval=31))
year=int(turtle.numinput("Year","Enter your birth year \n",1997,minval=1950, maxval=2010))

first_sum = (month + year + day)

#GUI design
turtle.speed(0)
turtle.pencolor('pink') 
turtle.bgcolor('black') 
x = 0 
turtle.down() 
while x < 120:  #create first object
    turtle.fd(200)     
    turtle.rt(70)
    turtle.rt(11.1111) 
    x = x+1
turtle.up() #move towards second object
turtle.fd(200)
turtle.rt(40)
turtle.down()
y = 0 
turtle.down()
while y < 100: #create second object
    turtle.fd(200)     
    turtle.rt(70)
    turtle.rt(11.1111) 
    y = y+1
turtle.pencolor('blue')

#iteration(first  digit sum to a single digit)
accum = 0
for x in str(first_sum):
    accum = accum + int(x)
second_sum = accum
accum2 = 0
for x in str(second_sum):
    accum2 = accum2 + int(x) 
accum3 = 0
third_sum = accum2
for x in str(third_sum):
    accum3 = accum3 +int(x)

#definitions
paragraph = accum3

#use function to find the chinese number and paragraph
def chyr_calc(x):
    chyr_num=((x - 1899)% 12)
    return chyr_num
result_chyr= chyr_calc(year)
result_para= akovneva_finalchyr_para.cyr_dict[result_chyr]

#obtain western zodaic para info using if and else if 
if month == 1 and day >= 20 or month==2 and day<= 18:
        wzod=akovneva_wezpara.wzpara11
elif month == 2 and day >=19 or month== 3 and day<=20:
        wzod=akovneva_wezpara.wzpara12
elif month == 3 and day >=21 or month== 4 and day<=19:
        wzod=akovneva_wezpara.wzpara1
elif month == 4 and day>=20 or month== 5 and day<=20:
        wzod=akovneva_wezpara.wzpara2
elif month == 5 and day >=21 or month== 6 and day<=21:
        wzod=akovneva_wezpara.wzpara3
elif month == 6 and day >= 22 or month== 7 and day<=22:
        wzod=akovneva_wezpara.wzpara4
elif month == 7 and day>= 23 or month== 8 and day<=22:
        wzod=akovneva_wezpara.wzpara5
elif month == 8 and day>= 23 or month== 9 and day<=22:
        wzod=akovneva_wezpara.wzpara6
elif month == 9 and day>=23 or month== 10 and day<=23:
        wzod=akovneva_wezpara.wzpara7
elif month == 10 and day>= 24 or month== 11 and day<=22: 
        wzod=akovneva_wezpara.wzpara8
elif month == 11 and day>=23 or month== 12 and day<=21:
        wzod=akovneva_wezpara.wzpara9
elif month == 12 and day>=22 or month== 1 and day<=19:
        wzod=akovneva_wezpara.wzpara10
    
#prints all content into the GUI 
turtle.penup()
turtle.goto(50,100)
turtle.pendown()
line1=("Hello, "+fname+" your birth number is "+str(accum3)+". \n"+akovneva_bypara.color_dict[paragraph])
turtle.write(line1,False,align= "center", font=('Arial', 10, 'bold'))
line2=("Your chinese zodaic animal is a "+result_para)
turtle.penup()
turtle.goto(-20,-240)
turtle.pendown()
turtle.write(line2,False,align= "center",font=('Arial', 10, 'bold'))
turtle.penup()
turtle.goto(30,-170)
turtle.pendown()
line3=(wzod)
turtle.write(line3,False,align= "center",font=('Arial', 10, 'bold'))

#opens/runs to webpage
fhw= open("akovneva_final.html", 'w')
fhw.write(akovneva_finalhtml_stuff.tophtml)
fhw.write(str(line1))
fhw.write(akovneva_finalhtml_stuff.endline1)
fhw.write(akovneva_finalhtml_stuff.startline2)
fhw.write(line2)
fhw.write(akovneva_finalhtml_stuff.endline2)
fhw.write(akovneva_finalhtml_stuff.startline3)
fhw.write(line3)
fhw.write(akovneva_finalhtml_stuff.bthtml)
fhw.close()
webbrowser.open_new("akovneva_final.html")


#writes to log file
fh = open("akovneva_final.log", 'a')
fh.write(line1)
fh.write("\n")
fh.write(line2)
fh.write(line3)
fh.write("\n")
fh.close()


turtle.done()

