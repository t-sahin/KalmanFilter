# KalmanFilter

This is a Kalman Filter module designed to work with [ur-whitelab/arc-vision/arcvision/tracker.py](https://github.com/ur-whitelab/arc-vision/blob/master/arcvision/tracker_processor.py). Kalman Filtering is a tracking method that can excellently reduce sensor noise in a system. For the specific purpose in which it's designed, it has unique measurement noise covariance matrices that would vary per system. 

In the development of this tracking method, several sources were used to gain better overall understanding of Kalman Filtering and in its eventual python implementation. These sources are:
- [How a Kalman Filter Works, in Pictures](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)
- [Understanding the Basis of the Kalman Filter Via a Simple and Intuitive Derivation, by Ramsey Faragher](http://www.cl.cam.ac.uk/~rmf25/papers/Understanding%20the%20Basis%20of%20the%20Kalman%20Filter.pdf)
- [Kalman Filtering (Demo), by Andrew D. Straw](http://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html)
- [Implementation of Kalman Filter with Python Language, by Mohamed Laaraiedh](https://arxiv.org/pdf/1204.0375.pdf) 
