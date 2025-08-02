clc;
clear all;
close all;

% Read the image
I = imread('Avengers.jpg');

% Get dimensions
[rows, cols, channels] = size(I);

% Check if it's an RGB image
if channels ~= 3
    error('Input image is not RGB');
end

% Red Plane
Ired = I;
Ired(:,:,2) = 0;  
Ired(:,:,3) = 0;   

% Green Plane
Igreen = I;
Igreen(:,:,1) = 0; 
Igreen(:,:,3) = 0; 

% Blue Plane 
Iblue = I;
Iblue(:,:,1) = 0;  
Iblue(:,:,2) = 0;  

% Display all three images
figure;

subplot(1,3,1);
imshow(Ired);
title('Red Plane');

subplot(1,3,2);
imshow(Igreen);
title('Green Plane');

subplot(1,3,3);
imshow(Iblue);
title('Blue Plane');
