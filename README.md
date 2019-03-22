# python-dance
This is another project that I had to complete for my python course in college.

This was an introduction into being able to write code for little arduino powered cars that were available to our class. This code was transmitted via bluetooth to the drone, which then carried out the task we were to give it.

At the beginning of the program, we import what is known as Myro. This is the system that was used to translate the code we were to type to a language that the drones were able to read and understand.

In the first two definition, named "yoyo" and "wiggle", are defining the steps that the drone will read, and what they will tell the drone what to do when it gets to the steps that are to come.

Next we will define "dance". This will be where the previous two definitions will come into play. In this definition, we will be telling the drone how to move. The first yoyo will be telling the drone to move half a rotation forward then waiting half a second. A unit is half a rotation of the drone's wheel. The next yoyo will do the opposite of the first and move the drone backwards half a unit then waiting half a second. The next step, wiggle, will move the drone to its right half a unit, waiting one second, then move back to its left twice for half a unit with a one second wait time in between each movement. Finally, to round out the movements, the drone will move back to its right for half a unit then waiting for one second before moving onto the next step of code.

After all of that has been defined, we will define the main function. This is the driver of the program that calls everything together. At the start of this, we get the program to print a phrase into the command prompt to tell you what is about to happen. After this, the previously mentioned definition "dance" takes effect and what has been defined there is executed. After that is finished, another message stating that the program has finished will display in the command prompt and the program will terminate.
