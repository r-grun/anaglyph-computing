# anaglyph-computing: (Re-)Creation of anaglyph images from/to stereo pairs

This repository contains the project to convert stereo images to anaglyphs as well as the scripts and models to reproduce
the original images.


### Data sources & Literature

- [1] X. Liu, S. Iwase, and K. M. Kitani, "StereOBJ-1M: Large-scale Stereo Image Dataset for 6D Object Pose Estimation," Sep. 2021. [Online]. Available: http://arxiv.org/pdf/2109.10115
- [2] Y. Hua et al., "Holopix50k: A Large-Scale In-the-wild Stereo Image Dataset," Mar. 2020. [Online]. Available: http://arxiv.org/pdf/2003.11172


## Project structure
The project is split into several sections to encapsulate different functionality.

All image data is stored under `/data`.
The folder should contain all stereo images.
Created anaglyphs are stored under `/data/anaglyphs` and utilize the same name as the original stereo image with the suffix `*_anaglyph`.

Code to compute stereo pairs and create anaglyphs is stored under `/src/anaglyph_creation`.
Due to different source formats, stereo pairs first have to be combined into a single image file.
For example, stereo pairs from [1] are already in the correct file format.
However, source stereo images from [2] are split into _right_ and _left_ images and have to be concatenated into a single image first. 
With the stereo images, anaglyphs are being created.