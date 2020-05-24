// Gmsh project created on Sat May 16 17:18:00 2020
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 20};
//+
Point(2) = {20, 0, 0, 20};
//+
Point(3) = {0, 10, 0, 20};
//+
Point(4) = {20, 10, 0, 20};
//+
Line(1) = {3, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 4};
//+
Line(4) = {4, 3};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
