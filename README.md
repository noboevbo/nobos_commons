# nobos commons

This repository contains code that I use in several of my projects. Included is among other things:

- Data structures for human representations (skeleton, bounding boxes, etc.), these increase (in my opinion) the readability compared to dictionaries etc. clearly. You can easily access joints etc. via an object structure. e.g. human.skeleton.joints.hip.x. However, this has a negative effect on the performance. If only a few skeletons have to be processed, the performance loss can be tolerated, so I still use the approach everywhere in my code, except for the training of models.
- Input providers as a standard interface for (camera) sensor input data
- Cache: A simple mechanism to cache function results by using a @cache decoration.
- Feature vector generators: Process to generate feature vectors for neural network input from e.g. 2D human poses.
- Joint augmenter: Augmentation code for 2D human joints.

The repository is publicly accessible, but it's mainly used for my private projects, so I can't guarantee a stable state. Changes to the code are possible at any time.