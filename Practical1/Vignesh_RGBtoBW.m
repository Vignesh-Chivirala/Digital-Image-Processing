clc;
clear all;
close all;

% Read the RGB image
I = imread('Avengers.jpg');

% Get image dimensions
[rows, cols, channels] = size(I);

% Ensure it's an RGB image
if channels ~= 3
    error('Image is not RGB');
end 

% Convert to double for accuracy
I = double(I);

% Extract R, G, B channels
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);

% Average method for grayscale
gray = (R + G + B) / 3;

% Normalize grayscale to [0, 1]
gray = gray / 255;

% Thresholding to get BW image
threshold = 0.5;
bw = gray > threshold;  % Logic (1 for white, 0 for black)

imshow(bw);
title('Black & White Image');
