import numpy as numpy
import matplotlib.pyplot as matplot #Importing necessary libraries
def main(): #Defining function for user inputs
    try:
        numberofsteps = int(input("Enter the number of steps: ")) #Asking the user to enter value for number of steps only accepting integer values
        sizeofsteps = float(input("Enter the size of steps: ")) #Asking the user to enter value for size of steps only accepting floating values
    except ValueError: #Exception Handling
        print("Invalid input. Please enter valid numeric values.") #Output if neither a floating or integer value has been inputted for the corresponding value
        return
    x, y = BrownianMotion(numberofsteps, sizeofsteps) #Calling BrownianMotion function with parameters previously defined
    PlottingMotion(x, y) #Plots the Brownian Motion with parameters previously defined
def BrownianMotion(numberofsteps, sizeofsteps): # Defining the function for the motion + inputting the parameters of the function
    # Simulating Brownian motion
    x = numpy.zeros(numberofsteps) #Initialising the array for the horizontal displacement as 0
    y = numpy.zeros(numberofsteps) #Initialising the array for the vertical displacement as 0
    for counter in range(1, numberofsteps):  #Loop iterates through from 1 to number of steps 
        angle = numpy.random.uniform(0, 2 * numpy.pi) #Angle of which particle moves is generated randomly with each angle having an equal chance of being selected as it is a random walk model
        x[counter] = x[counter-1] + sizeofsteps * numpy.cos(angle) #Horizontal displacement updates using previous X value and a product of the random angle and the size of each step using the cosine value as cosine is used to calculate horizontal displacement
        y[counter] = y[counter-1] + sizeofsteps * numpy.sin(angle) #Vertical displacement updates using previous Y value and a product of the random angle and the size of each step using the sine value as sine is used to calculate vertical displacement
    return x, y #Outputting the values
def PlottingMotion(x, y): #Defining the function for plotting
    # Plotting Brownian motion trajectory
    matplot.figure(figsize=(8, 8)) #Defining size of figure to be generated
    matplot.plot(x, y, label='Brownian Motion') #Plotting vertical and horizontal displacements using the x and y positions + label for the legend
    matplot.scatter(x[0], y[-0], color='red', marker='o', label='Start Position') #Highlighting starting position of particle with a O marker
    matplot.scatter(x[-1], y[-1], color='red', marker='x', label='End Position') #Highlighting final position of particle with a X marker 
    matplot.title('Simulating Brownian Motion of a Particle') #Defining title
    matplot.xlabel('Horizontal Displacement of Particle') #Defining x axis label
    matplot.ylabel('Vertical Displacement of Particle') ##Defining y axis label
    matplot.legend() #Defining legend
    matplot.show() #Displays the plot
if __name__ == "__main__":
    main()