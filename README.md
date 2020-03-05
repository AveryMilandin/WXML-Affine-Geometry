# WXML-Affine-Geometry
This repository contains code for working with the affine space F<sub>3</sub><sup>n</sup> where F<sub>3</sub> is the field with three elements. The provided GUI, affineGUI.py allows the user to see a visual representation of F<sub>3</sub><sup>n</sup> for any n from 1 to 6. It also allows the user to view subsets of F<sub>3</sub><sup>n</sup> by either typing them in in binary or by manually editing the state by checking checkboxes corresponding to desired points. The 4Dcaps.txt file was produced by code written by Dr. Robert Won and is used in Verifier. The caps we are using for this project are the maximal 2-caps in F<sub>3</sub><sup>4</sup>. The other files, invertibleMatrices and verifier, verify that all 2-caps produced by flat-elim-search are affinely equivalent.

## Example Maximal 2-caps
2-caps are defined as sets of vectors in F<sub>3</sub><sup>n</sup> such that no three points are collinear and no four points are coplanar. A 2-cap is maximal if it is of maximum possible size. The following are examples of maximal 2-caps in 2, 3, and 4 dimensions as expressed by affineGUI

### 2 Dimensions
![](results/2D2cap.PNG)
</br>notice that adding any fourth point would cause all 4 points to be coplanar since F<sub>3</sub><sup>2</sup> is itself a plane.

### 3 Dimensions
![](results/3D2cap.PNG)
</br> Lines and planes become a bit difficult to visualize in 3 dimensions, but if any point were added to this set there would be three points collinear, four points coplanar, or both.

### 4 Dimensions
![](results/4D2cap.PNG)
</br>Attempting to visualize lines and planes in 4 dimensions is hopeless, but 2-caps of this type are the ones we are interested in for this project.

## Running the Code
Cloning this repository and running any of the files from the correct directory should work as long as invertibleMatrices is run before Verifier. This is due to the fact that verifier needs the file that is output by invertibleMatrices, and that file is too large for GitHub.
</br> These algorithms take under 2 hours in total to verify that all 2-caps in F<sub>3</sub><sup>4</sup> are affinely equivalent. flat-elim search generates the necessary caps in about 45 minutes. invertibleMatrices takes 40 minutes, and verifier takes 15 minutes on a decent laptop.

## Goals
1) Generate invertible matrices as needed in Verifier instead of in invertibleMatrices. This would avoid needing to work with a 3.5 Gb file and would not slow down the overall verification time.
2) Solve the same problem for maximal 3-caps in F<sub>3</sub><sup>4</sup>. 3-caps are sets of points with no 3 points collinear, no 4 points coplanar, and no 5 points in the same solid.
