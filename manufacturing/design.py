# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:45:46 2018

@author: danaukes
"""

import foldable_robotics
import foldable_robotics.dxf 
import numpy
import matplotlib.pyplot as plt
import shapely.geometry as sg
from foldable_robotics.layer import Layer
from foldable_robotics.laminate import Laminate
import foldable_robotics.manufacturing
import foldable_robotics.parts.castellated_hinge1
from foldable_robotics.dynamics_info import MaterialProperty
import idealab_tools.plot_tris
foldable_robotics.resolution=8
from math import pi, sin,cos,tan
import idealab_tools.text_to_polygons
import foldable_robotics.pdf
import foldable_robotics.pdf

def build_segments(desired_width,desired_segment_length,desired_gap):
    num = (desired_width-desired_gap)/(desired_gap+desired_segment_length)
    num = round(num)
    unmodified_width = num*(desired_gap+desired_segment_length)+desired_gap
    frac = desired_width/unmodified_width
    
    beg = (numpy.r_[:num] * (desired_gap+desired_segment_length)+desired_gap)*frac
    end = (numpy.r_[:num] * (desired_gap+desired_segment_length)+desired_gap+desired_segment_length)*frac
    segs = [((a,0),(b,0)) for a,b in zip(beg,end)]
    return segs

def build_segmented_hinge(desired_width,desired_segment_length,desired_gap):
    hinge1 = build_segments(desired_width,desired_segment_length,desired_gap)
    hinge2 = [sg.LineString(item) for item in hinge1]
    hinge3 = Layer(*hinge2)
    return hinge3

def create_bodies(filename, layername, num_layers):
    body = foldable_robotics.dxf.read_lwpolylines(filename,layer=layername, arc_approx = 10)

    bodies = [Layer(sg.Polygon(item)) for item in body]
    body = bodies.pop(0)
    for item in bodies:
        body ^= item
    body = body.to_laminate(num_layers)
    return body

def place_hinges(filename,layername,hinge):
    hinge_lines = foldable_robotics.dxf.read_lines(filename,layer=layername)
    hinge1 = Layer().to_laminate(len(hinge))
    for p3,p4 in hinge_lines:
        hinge1|=hinge.map_line_stretch((0,0),(1,0),p3,p4)
    return hinge_lines,hinge1

def place_cuts(filename,layername,thickness,num_layers):
    cut_lines = foldable_robotics.dxf.read_lines(filename,layer=layername)
    cut_lines += foldable_robotics.dxf.read_lwpolylines(filename,layer=layername, arc_approx = 10)
    
    cuts = Layer()
    for item in cut_lines:
        cuts |= Layer(sg.LineString(item))
    cuts<<=thickness/2
    cuts = cuts.to_laminate(num_layers)
    return cuts    

def place_holes(filename, layername,num_layers):
    holes = foldable_robotics.dxf.read_circles(filename,layer='holes')
    
    holes2 = []
    for center, radius in holes:
        holes2.append(sg.Point(*center).buffer(radius))
    holes_layer = Layer(*holes2)
    holes_lam = holes_layer.to_laminate(num_layers)  
    return holes_lam

def hinge_width_calculator(desired_degrees,thickness):
    theta = (180-desired_degrees)*pi/180
    w=thickness/tan(theta)
    return w

def polys_to_layer(l1):
    l1 = [sg.Polygon(item) for item in l1]
    l11 = Layer(l1.pop(0))
    for item in l1:
        l11 ^= Layer(item)
    return l11
    
def output_pdf(filename,design2,x,y,layers_separate = True):
    design2 = design2.translate(x,y)
    design2=design2.scale(1/25.4,1/25.4)
    design2=design2.scale(foldable_robotics.pdf.ppi,foldable_robotics.pdf.ppi)
    if isinstance(design2,Laminate):
        if not layers_separate:
            p=foldable_robotics.pdf.Page(filename+'.pdf')
            for d in design2:
    #        d = design2[0]
                for item in d.exteriors()+d.interiors():
                    p.draw_poly(item)
            p.close()
        else:
            for ii,d in enumerate(design2):
                p=foldable_robotics.pdf.Page(filename+'{0:03f}.pdf'.format(ii))
                for item in d.exteriors()+d.interiors():
                    p.draw_poly(item)
                p.close()

    elif isinstance(design2,Layer):
        p=foldable_robotics.pdf.Page(filename+'.pdf')
        for item in design2.exteriors()+design2.interiors():
            p.draw_poly(item)
        p.close()
        
def build_layer_numbers(num_layers, prop=None):
    prop = prop or {'family':'Arial','size':text_size}
    layer_ids = []
    for ii in range(num_layers): 
    
        l = idealab_tools.text_to_polygons.text_to_polygons('Layer '+str(ii),prop=prop)
        layer_ids.append(l)
    
    layer_ids = [polys_to_layer(item) for item in layer_ids]
    layer_id = Laminate(*layer_ids)
    return layer_id
        
filename = 'input_files/legpieces4-1.DXF'
jig_diameter = 5
text_size = jig_diameter
support_width = 1
kerf = .05

w=hinge_width_calculator(150,1.1)
hinge = foldable_robotics.parts.castellated_hinge1.generate()
hinge = hinge.scale(1,w)
#w=.1
#hinge = build_segmented_hinge(1,.05,.2)<<.01
#hinge = hinge.scale(1,100*w/2)
#hinge = hinge.to_laminate(1)

NUMLAYERS = len(hinge)

#hinge = hinge.scale(1,.1)

arc_approx = 10

body = create_bodies(filename,'body',NUMLAYERS)

hinge_lines_down,hinges_down = place_hinges(filename,'hinges_down',hinge)
hinge_lines_up, hinges_up = place_hinges(filename,'hinges_up',hinge)
hinge_lines = hinge_lines_down+hinge_lines_up
all_hinges = hinges_down|hinges_up
all_hinges <<=.1
#
cuts = place_cuts(filename,'cuts',.02,NUMLAYERS)


holes = place_holes(filename,'holes',NUMLAYERS)


hole,dummy = foldable_robotics.manufacturing.calc_hole(hinge_lines,.1)
hole = hole.to_laminate(NUMLAYERS)
hole = foldable_robotics.manufacturing.cleanup(hole,.025,resolution = 4)

design2 = body- hole - all_hinges - cuts - holes


layer_id = build_layer_numbers(NUMLAYERS)

design_outer = foldable_robotics.manufacturing.unary_union(design2)
placement_holes = (design_outer<<20).bounding_box()
points = ((numpy.array(list(set(placement_holes.exteriors()[0])))/2).round(-1))*2
layer_id = layer_id.translate(*(points.min(0)+numpy.array([10,-text_size/2])))
geoms = [sg.Point(item) for item in points]
placement_holes2 = Layer(*geoms)
placement_holes2<<=(jig_diameter/2)
sheet = (placement_holes2<<10).bounding_box()
placement_holes2=placement_holes2.to_laminate(NUMLAYERS)
sheet=sheet.to_laminate(NUMLAYERS)


keepout =  foldable_robotics.manufacturing.keepout_laser(design2)
second_pass_scrap = sheet-keepout

#Why is the center cut out of every hinge?

first_pass_scrap = sheet - design2-second_pass_scrap
first_pass_scrap = foldable_robotics.manufacturing.cleanup(first_pass_scrap,.00001)

support = foldable_robotics.manufacturing.support(design2,foldable_robotics.manufacturing.keepout_laser,support_width,support_width/2)

#Calculate the web by using only the material which can be cut, minus a gap determined by the support width.  Is that the only material you can use?

web = (sheet-(keepout<<support_width)-placement_holes2)-layer_id

supported_design = web|design2|support

#cut_line = keepout<<kerf


cut_material = (keepout<<.1)-keepout

final_cut = sheet - keepout

remaining_material = supported_design-cut_material


bottom_left = numpy.array(list(sheet[0].bounding_box().geoms[0].exterior.coords)).min(0)
top_right = numpy.array(list(sheet[0].bounding_box().geoms[0].exterior.coords)).max(0)

x = -bottom_left[0]
y = foldable_robotics.pdf.page_height*25.4-top_right[1]

x = x+10
y = y-10



#output_pdf('design2',design2,x,y,layers_separate=False)
#output_pdf('supported_design',supported_design,x,y,layers_separate=True)
#output_pdf('final_cut',final_cut[0],x,y,layers_separate=False)
supported_design.export_dxf('output_files/supported_design')
final_cut[0].export_dxf('output_files/final_cut')

design2.plot(new=True)
plt.title('design')
supported_design.plot(new=True)
plt.title('supported design')
final_cut.plot(new=True)
plt.title('final cut')


#hinge.plot(new=True)
#body.plot(new=True)
#plt.savefig('f0.png')
#all_hinges.plot(new=True)
#plt.savefig('f4.png')
#cuts.plot(new=True)
#plt.savefig('f5.png')
#holes.plot(new=True)
#plt.savefig('f6.png')
#hole.plot(new=True)
#plt.savefig('f7.png')
#design2.plot(new=True)
#plt.savefig('f9.png')
#second_pass_scrap.plot(new=True)
#plt.savefig('f10.png')
#first_pass_scrap.plot(new=True)
#plt.savefig('f11.png')
#first_pass_scrap.plot(new=True)
#plt.savefig('f12.png')
#support.plot(new=True)
#plt.savefig('f13.png')
#supported_design.plot(new=True)
#plt.savefig('f14.png')
#cut_line.plot(new=True)
#plt.savefig('f15.png')
#cut_material.plot(new=True)
#plt.savefig('f16.png')
#remaining_material.plot(new=True)
#plt.savefig('f17.png')

render = design2
render = design2.simplify(1)
render=foldable_robotics.manufacturing.cleanup(render,.05)
m = MaterialProperty.make_n_blank(NUMLAYERS,thickness = .1)
mi=render.mesh_items(m)
idealab_tools.plot_tris.plot_mi(mi)
