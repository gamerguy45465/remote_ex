Date: 1.16.25 - Subject: Starting Out. Here I start a journal where I will be going over what I did and learned this semester. 
It's going to be great!


Date: 1.17.25 - Subject: Discrete Math. Alright, so I have been working on my discrete mathematics homework today trying to figure Out
combinations and permutations. It's easy so far, because after all, I did use both of these a ton when I was in Probability and Statistics.
However, Professor Stander has stated that next time we meet in class, we will go over permutations and combinations that allow for repeats to
happen, which he mentioned would be a lot harder. I can't remember if we used combinations and permutations where repeats were allowed in
stats, but hopefully it comes to me fast. Maybe when we start on the topic it will occur to me wether or not I have used it before.

Date: 1.21.25 - Subject: Ideas. Today during class we came up with some ideas for a project that we are going to do throughout the semester.
We each gave an idea based on a "What if..." question, and then organized those ideas into Categories based on if it was a feature or an app idea. We then choose one idea for an app and 5-8 ideas for features. We are going to be doing a Music Social Media app, but have agreed that we will expand it to other things as soon as we get the music portion of it done. We want it to be highly secured, and so we plan on adding lots of design that have to do with encryption and what not. We also want it to stand out from other social media platforms, and we decided the way we are going to do this is through personalization. Users will be able to personalize their feed, page, and tab bar to fit their very needs and what they want to do with it. This is some of the things that we agreed to do in class.

Date: 1.21.25 - Subject: Sensors & Actuators. I would like to share a simple problem that I was trying to do in Sensors in actuators, that I was having trouble setting up until I came to a very basic realization. The Problem states that you are working with a resistance strain guage that has a resistance of 197 ohms, and a resistance change of 4 ohms. You place that in a Wheatstone bridge, where all the other 3 resistances will be 197 ohms. You then find that the maximum guage current is 0.21 A. The question wants you to find the maximum bridge excitation voltage. Instinctively, the first thing I thought to do was use ohms law, since we are given the Resistance of the Guage upfront and are also told what the current it. I use ohms law, which is V = IR to solve it and get 41.37 Volts. As it turns out, that was not correct, and so I did some overthinking, and some research. Throughout my research, I noticed something that I forgot to take into account, and that was the Guage Factor. You see, in addition to the resistance, we were also given the resistance change, which was 4 ohms. That means that we would have to calculate the guage factor using the formual GF = (dR/R)/strain. We can assume the strain to be 0.01, and I think that's because in this scenario, it would approach zero (referring to my knowledge of limits), although I'm not entirely sure why we can assume the strain to be this little (just what I was told). We then calculate the guage factor to be 2.030456853. We then do what we did before, which was use Ohms law to calculate the Voltage which was 41.37 Volts, but then we multiply that by the guage factor we just got, and get a final answer of 81.9 Volts, which as it turns out, that is the correct answer. Just wanted to share what I learned today from doing homeword in another class. 

Date: 1.23.25 - Subject: Flask Assignment. I've just completed the flask assignment. Most of the stuff I already knew (html for the most part) except for flask itself. I've never used flask, and it feels like a networking tool (which that's what it technically is) that you can use to run html code, and a web server. It's pretty cool. That's all.

Data: 1.26.25 - Subject: C++ Integration. Since I am more confortable with C++ (since it's the language that I use the most) I have decided that
in our projects, whenever I write code, I am going to integrate C++ with the Python code that we write. I will do this with Dynamic Libraries
(.so files) and with the ctypes pip package for python. I have been experimenting with this, and so far it is very possible to do without
interupting the work of everybody else. All it requires is linking the Dynamic Link Library that I created from C++ to the python file, and then
calling whatever function I created. It works like this:

###c++
#include <iostream>

extern "C" // This is important when doing this in C++, otherwise it won't work and I would have to use C instead
{
    void Hello()
    {
        std::cout << "Hello World!" << std::endl;
    }

}


###python 
from ctype import cdll

lib = cdll.LoadLibrary("./libfile.so")

lib.Hello()


This is a simple example, because it reality there would be a lot more going on than this, but this is just the basic idea. 
This is going to allow me to create external libraries in C++, and use them in our projects. Hopefully this will alsogive my teammates 
an efficient interface, where if they ever need these functions, they can just add the .so files to whatever python source file they are working
in and then just call these functions. Of course, that's nothing special because they would be able to do that anyway in a python file, but the
point I am trying to make is this does not hinder on my collegues in any way, and as a result I can legally write all of the code that I am 
assigned to write in C++ instead of python, since I am more used to C++ than Python.



Date: 1.31.25 - Subject: Gamma Categories. In an online learning environment (which I am doing on my own time) I just learned about Gamma Categories, named after someone named Erick Gamma and not the greek letter Gamma. Gamma Categories are different categories of design patterns,
main, of which we may learn about in this class. These categories include Creational Patterns, Structural Patterns, and Behavioral Patterns. Creational Patters have to do with the creating and construction of objects. Structural Patterns are concerned with class members and are also concerned with wrappers that mimic the underlying class interface (they are also what stress the importance of good api design). Finally, Behavioral Patterns are Patterns that don't follow a central theme, and are all different. 


Date: 2.9.25 - Subject: Builder Pattern. I have been studying design patterns on my own time, where I have been learning about the builder patter. The Builder pattern is useful when you want to separate the construction of a component from the representation of the component, in order to have the construction be represented by multiple representations. For example, say I want to build an HTML generator. Instead of generating a bunch of tags and whatnot, I could just make a class along with a bunch of subclasses so that all I would need to do is call the class in order to create the component everytime. That way it is easier and less work to do.


Date: 3.2.25 - Subject: Flask. Just been going over flask. Been learning how to work with forms in flask. Learning forms will most likely help in our project, and what I do to learn flask will help me to be more proficient in our project, especially with solving problems and whatnot.

Date: 3.8.25 - Subject: More Flask. Not much to say here, just learning more flask. The project is coming together very well. So yeah.
