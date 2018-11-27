#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:10:48 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

# This script will take the md10.pdb and the original pdb from RCSB database, 
# align them and output the aligned_ligand.pdb

import __main__

__main__.pymol_argv=[ 'pymol', '-qc'] # load pymol quietly and with GUI

import sys, time, os

import pymol

pymol.finish_launching()

# read the sturectures

pymol.cmd.load(sys.argv[1]+".pdb", "original")

pymol.cmd.load(sys.argv[1]+"_md10.pdb","md10")


#align the original pdb to the md10.pdb

pymol.cmd.align("original","md10")

pymol.cmd.select("ligand","resn "+'JIN')

pymol.cmd.save("ligand.pdb","ligand")

pymol.cmd.quit()
