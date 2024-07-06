This is official implementation of Self-supervised learning for denoising of multidimensional MRI data (https://doi.org/10.1002/mrm.30197).

This repository provides a demonstration of our proposed MD-S2S (multidimensional Self2Self) algorithm.

Purpose
To develop a fast denoising framework for high-dimensional MRI data based on a self-supervised learning scheme, which does not require ground truth clean image.

Theory and Methods
Quantitative MRI faces limitations in SNR, because the variation of signal amplitude in a large set of images is the key mechanism for quantification. In addition, the complex non-linear signal models make the fitting process vulnerable to noise. To address these issues, we propose a fast deep-learning framework for denoising, which efficiently exploits the redundancy in multidimensional MRI data. A self-supervised model was designed to use only noisy images for training, bypassing the challenge of clean data paucity in clinical practice. For validation, we used two different datasets of simulated magnetization transfer contrast MR fingerprinting (MTC-MRF) dataset and in vivo DWI image dataset to show the generalizability.

Results
The proposed method drastically improved denoising performance in the presence of mild-to-severe noise regardless of noise distributions compared to previous methods of the BM3D, tMPPCA, and Patch2self. The improvements were even pronounced in the following quantification results from the denoised images.

Conclusion
The proposed MD-S2S (Multidimensional-Self2Self) denoising technique could be further applied to various multi-dimensional MRI data and improve the quantification accuracy of tissue parameter maps.
