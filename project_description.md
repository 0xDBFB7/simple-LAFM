Project: Simple Atomic Force Microscope
===
Status: Completed.
-------

#### Date started: 2017-??-??
#### Date finished: 2017-??-??
#### Date written: 2017-08-13


Background:
---

##NOTE: This is not a "real" AFM. The resolution of this device is not nearly sufficient to measure very fine details.

AFM scopes use a small cantilever brought in very close proximity to a surface to be measured. The deflection of the cantilever is measured, which determines something about the surface of the material. 

Description:
---

Figured I'd give this a try - this was one of those projects that I had very little time to do research on, just watched a few videos and read one paper. I knew I wouldn't get stellar results, considering that the best resolution my 3d printer can effectively do is about 0.05 mm, and that I couldn't possibly create the fancy optics and micro-miniture probes that standard devices can.

I 3d printed a partially light-tight enclosure, with a mount for a 5mw laser diode and a CDS cell at a long boom. I cut a small 4-40 screw hole in the bottom to affix the probe cantilever. I dropped the CDS cell through and glued it in place. With the laser powered with 2.1v, drawing 0.004a, I got about 1-2 Mohm across the photoresistor. 

I cut a small cantilever probe out of a sheet of standard aluminum foil, trying to produce a sharp point.

First results seemed promising.

By moving the probe slightly by hand, I could change the resistance of the CDS cell.

I mounted the sensor to my RepRap, and wrote a bit of python that raster scans the printer, logging the CDS's resistance at each point.

I put a piece of plastic on the bed, and put a thick scratch in it.

A "surface" of sorts was created, with many small bumps. Interestingly, the surface always sloped upwards. Some thermal effect? Strange.

After greatly increasing laser power (2.3v, 0.008a), the CDS readings became much more stable.
