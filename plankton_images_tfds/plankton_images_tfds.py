"""plankton_images_tfds dataset."""

import tensorflow_datasets as tfds

# TODO(plankton_images_tfds): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
"""

# TODO(plankton_images_tfds): BibTeX citation
_CITATION = """
"""

#balanced:https://onedrive.live.com/download?cid=F8F193065B261D91&resid=F8F193065B261D91%21334&authkey=AFm4LZlpbDrEZuU1
#raw:https://onedrive.live.com/download?cid=F8F193065B261D91&resid=F8F193065B261D91%21333&authkey=ALYWgksDbN2eUow
#new(balanced with cyano):https://onedrive.live.com/download?cid=F8F193065B261D91&resid=F8F193065B261D91%21335&authkey=ACNNJtyJOFj-uvg
#new(balanced and all jpg):https://onedrive.live.com/download?cid=F8F193065B261D91&resid=F8F193065B261D91%21337&authkey=AJxKFRwRrEvbymE
_URL = ("https://onedrive.live.com/download?cid=F8F193065B261D91&resid=F8F193065B261D91%21337&authkey=AJxKFRwRrEvbymE")


class PlanktonImagesTfds(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for plankton_images_tfds dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(plankton_images_tfds): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=["0", "1"]),  
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=("image", "label"),  # e.g. ('image', 'label')
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(plankton_images_tfds): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    path = dl_manager.download(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={"archive": dl_manager.iter_archive(path)},
        ),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    # TODO(plankton_images_tfds): Yields (key, example) tuples from the dataset
    no_count, o_count = 0, 0
    for fname, fobj in archive:
      if not fname.endswith(".jpg"):
        continue
      label = fname.split("/")[-2]
      if label == "0":
        no_count += 1
      else:
        o_count += 1
      record = {
          "image": fobj,
          "image/filename": fname,
          "label": label,
      }
      yield fname, record
    print("There are",no_count,"non-HAB examples and",o_count,"HAB examples.")
