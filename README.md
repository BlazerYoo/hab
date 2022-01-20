# hab
 
Harmful algal bloom (HAB) species detection

Classify plankton as a HAB-causing species or not based on images.

## Files
Files in `plankton_images_tfds` is [tfds](https://www.tensorflow.org/datasets/api_docs/python/tfds) dataset format which allows the following:

```python
# Import and initialize dataset
import plankton_images_tfds
# load dataset the first time
ds, info = tfds.load('plankton_images_tfds', as_supervised=True, with_info=True)
```

`hab.ipynb` is Jupyter Notebook with data loading, hyperparameter optimization, k-fold cross validation and training, testing, and evaluation pipeline.

## License

Read the [AGPL-3.0 License](https://github.com/BlazerYoo/hab/blob/main/LICENSE)