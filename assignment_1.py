
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11774797
student_name   = 'Jacob Shevlin - Krell'
#
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data
    def data_set(new_seed = randint(0, 99999)):
        return raw_data(new_seed) # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.
def visualise_data(reports):
 # <--- Replace this statement with your solution
    cell_size = 80 # pixels
#1A WORK
    
    def draw_symbols():
        
        def draw_ingot():

                forward(17.5)
                pendown()
                fillcolor("silver")
                pencolor("dark grey")
                begin_fill()#Top of Ingot Start
                forward(52)
                left(100)
                forward(20)
                left(80)
                forward(52)
                left(100)
                forward(20)
                end_fill()#Top of Ingot End
                
                #Leftmost Side of Ingot Start
                fillcolor("slate gray")
                begin_fill()
                right(40)
                forward(9)
                right(140)
                forward(20)
                right(40)
                forward(9)
                penup()
                end_fill()#Leftmost Side of Ingot End
                
                #Front Side of Ingot Start
                pendown()
                right(140)
                forward(20)
                fillcolor("azure4")
                begin_fill()
                right(40)
                forward(9)
                left(120)
                forward(52)
                left(69)
                forward(9)
                end_fill()#Front Size of Ingot End
                left(110)
                forward(52)
                penup()
                
                #Shine on Ingot Start
                pensize(1)
                pencolor("antiquewhite")
                right(180)
                forward(52)
                left(120)
                forward(5)
                pendown()#Line 1
                forward(15)
                penup()
                left(90)
                forward(5)
                left(90)
                pendown()
                forward(12)
                penup()
                right(90)
                forward(5)
                right(90)
                forward(3)
                pendown()#Line 2
                forward(12)
                penup()
                left(90)
                forward(5)
                left(90)
                pendown()#Line 3
                forward(12)
                penup()
                right(90)
                forward(5)
                right(90)
                forward(5)
                pendown()#Line 4
                forward(12)
                penup()
                left(90)
                forward(5)
                left(90)
                pendown()#Line 5
                forward(10)
                penup()
                right(90)
                forward(5)
                right(90)
                forward(3)
                pendown()#Line 6
                forward(12)
                penup()#Shine on Ingot End
                
        def steel_balanced(x, y):
            setheading(0)
            penup()
            goto(x, y)
            speed(0.5)
        
            #Draws a square Start
            forward(2)
            right(90)
            forward(2)
            pendown()
            fillcolor("darkgoldenrod")
            pensize(2)
            begin_fill()
            pencolor("black")
            left(180)
            forward(40)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(34)
            end_fill()
            penup()#Draws a square End
            
            #Draw Ingot Start
            pensize(3)
            goto(x, y)
            setheading(270)
            forward(10)
            setheading(10)
            
            draw_ingot()
        
        def steel_increasing(x, y):
            setheading(0)
            penup()
            goto(x, y)
            speed(0.5)
        
            #Draws a square Start
            forward(2)
            right(90)
            forward(2)
            pendown()
            fillcolor("chartreuse4")
            pensize(2)
            begin_fill()
            pencolor("black")
            left(180)
            forward(40)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(34)
            end_fill()
            penup()#Draws a square End
            
            #Draw Ingot Start
            pensize(3)
            goto(x, y)
            setheading(270)
            forward(30)
            setheading(0)
            forward(17.5)
            setheading(45)
            
            draw_ingot()
            
        def steel_decreasing(x, y):
            setheading(0)
            penup()
            goto(x, y)
            speed(0.5)
        
            #Draws a square Start
            forward(2)
            right(90)
            forward(2)
            pendown()
            fillcolor("coral3")
            pensize(2)
            begin_fill()
            pencolor("black")
            left(180)
            forward(40)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(76)
            right(90)
            forward(34)
            end_fill()
            penup()#Draws a square End
            
            #Draw Ingot Start
            pensize(3)
            goto(x, y)
            setheading(0)
            forward(5)
            setheading(90)
            forward(20)
            setheading(325)
            
            draw_ingot()
            
    
        def draw_symbols_left_description():
            steel_balanced(x = -660, y = 0)
            steel_increasing(x = -660, y = 160)
            steel_decreasing(x = -660, y = -160)
        
            pencolor("black")
            goto(-660, 60)
            pendown()
            write("Symbol depicting the\nvalue of steel\nstocks staying at \n the same value", align = "left", font = ("Arial",8, "bold"))
            #write description for steel_balencing
        
            penup()

        
            goto(-660, 220)
            pendown()
            write("Symbol depicting an\nincrease in the\nvalue of steel\nstocks", align = "left", font = ("Arial",8, "bold"))
            #write description for steel_increasing

            penup()
        
        
            goto(-660, -100)
            pendown()
            #write description for steel_decreasing
            write("Symbol depicting a\ndecrease in the\nvalue of steel\nstocks", align = "left", font = ("Arial",8, "bold"))
            penup()

        draw_symbols_left_description()
        
        
        month_to_cell = {
            'January': (-400, 0), 'February': (-320, 0), 'March': (-240, 0),
            'April': (-160, 0), 'May': (-80, 0), 'June': (0, 0),
            'July': (80, 0), 'August': (160, 0), 'September': (240, 0),
            'October': (320, 0), 'November': (400, 0), 'December': (480, 0)
            }
        
            # Mapping of month names to their numerical order
        # month_order = {
        # 'January': 1, 'February': 2, 'March': 3, 'April': 4,
        # 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9,
        # 'October': 10, 'November': 11, 'December': 12
        #     }
        
        # reports.sort(key=lambda report: month_order[report[0]])
        processed_data = {}
            
        for report in reports:
            month, value = report
                
            coordinates = month_to_cell[month]
            processed_data[month] = (value, coordinates)
            
            # Process the data set
        for report in reports:
            month, value = report
            x, y = month_to_cell[month] # Get coordinates based on the month

            # Decide which symbol to draw based on the value
            if value > 0:
                steel_increasing(x,y) # Draw symbol for increase
                steel_increasing(x, y + 80) # Draw symbol for increase
                if value > 1:
                    steel_increasing(x, y+160)
                    if value > 2:
                        steel_increasing(x, y+240)
            if value < 0:
                steel_decreasing(x, y) # Draw symbol for decrease
                steel_decreasing(x, y-80) # Draw symbol for decrease
                if value < -1:
                    steel_decreasing(x, y-160)
                    if value < -2:
                        steel_decreasing(x, y-240)
            if value == 0:
                steel_balanced(x, y) # Draw symbol for balance
                

        adjusted_profits = sum(min(max(value, -3), 3) for month, value in reports)

            

        print(f"Total profits: {adjusted_profits}")
        
        goto(-660, -240)
        pencolor("slate gray")
        pendown()
        write('Estimated Profits $: '+str(adjusted_profits) + " Billion", align = "left", font = ("Arial", 11, "bold"))
            
        #     # Constants for drawing
        # start_x = -400  # Starting X position for January
        # cell_size = 80  # Size of each cell/grid
        # y_limit = 240  # Maximum/Minimum Y position
        
        # # Initial positions and variables
        # current_x = start_x
        # current_y = 0  # Start at 0 for "January"

        # # Sort reports by month order
        # month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # reports.sort(key=lambda report: month_order.index(report[0]))
        
        # # Function definitions for drawing symbols (steel_balanced, steel_increasing, steel_decreasing) remain the same

        # # Iterate over sorted reports and draw symbols at calculated positions
        # for report in reports:
        #     month, value = report
            
        #     # Decide the symbol based on the value
        #     if value > 0:
        #         steel_increasing(current_x, current_y)
        #         # Update Y position, ensure it does not exceed y_limit
        #         current_y = min(current_y + cell_size, y_limit)
        #     elif value < 0:
        #         steel_decreasing(current_x, current_y)
        #         # Update Y position, ensure it does not go below -y_limit
        #         current_y = max(current_y - cell_size, -y_limit)
        #     else:  # value == 0
        #         steel_balanced(current_x, current_y)
            
        #     # Move to the next position for the subsequent month
        #     current_x += cell_size  # Move right by one cell for the next month


        
    draw_symbols()
        
        
                

        

            
            
        
            
        
            
    
            



        

    
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
#
# ***** You can add arguments to this function call to modify
# ***** features of the drawing canvas such as the background
# ***** and line colours, etc
create_drawing_canvas(canvas_title = "Visualised Steel Stocks", # Ignore the title
                          background_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          write_instructions = False) # Skip writing instructions


# Create the data set and pass it to the student's function
#
# ***** While developing your Task 1B code you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
#
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
