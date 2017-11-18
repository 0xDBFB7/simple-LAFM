![](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
![](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)

I'm not entirely sure why I made this thing. I don't really have much of a use for it.

This is a very, very simple, very crude Laser Atomic Force Microscope. It costs about $10 to build, though it does require a precision voltmeter (something that can give you at least three decimal places). Something with a 10-bit ADC would work. I used a GW-Instek GDM-8251A bench multimeter, which gives me 5 sig figs.

This is *not* a high-resolution, precision instrument. This is something I designed and built in <3 hours. It's very rough around the edges (ha). The X and Y resolution is limited to the resolution of whatever X-Y gantry you're using. The output drifts over time, creating an angled surface. 

First, print out the afm.stl file with a 3d printer. It looks like it won't work, but actually it's quite printable.

You'll need a 5mw laser diode, and a constant voltage source for it. I ran mine at 2.3v, drawing 0.008 amps. Push the laser into the optical path like so:

![Like so.](https://raw.githubusercontent.com/username/projectname/laser.png)

*WARNING* Lasers are dangerous. Be extremely careful with reflections. 

Cut out a piece of standard aluminum foil in this shape:

![Like so.](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)

The bottom hole takes a ~10mm long 4-40 screw and washer - this affixes one end of the cantilever probe ridgidly. Ensure that the cantilever isn't touching any part of the optical enclosure.




