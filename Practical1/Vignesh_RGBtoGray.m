clc;
clear all;
close all;

% Read the image
I = imread('Avengers.jpg');

% Getting dimensions
[rows, cols, channels] = size(I);

% Ensure the image is RGB
if channels ~= 3
    error('Input image is not RGB');
end

% Convert to double for accuracy
I = double(I);

% Extract R, G, B channels
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);

% Average method for grayscale
gray = (R + G + B) / 3;

% Convert to uint8 for display
gray = uint8(gray);

% Show the result
imshow(gray);
title('Grayscale Image');
