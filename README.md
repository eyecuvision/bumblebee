# Bumblebee
[![PyPI](https://img.shields.io/pypi/v/eyecu_bumblebee.svg)](https://pypi.python.org/pypi/eyecu_bumblebee)
[![Downloads](http://pepy.tech/badge/eyecu_bumblebee)](https://pepy.tech/project/eyecu_bumblebee) \
![Bumblebee image](./docs/bumblebee.png)

Bumblebee provides high level components to construct training pipelines for videos conveniently.


- [Install](#install)
- [Motivation](#motto)
- [Our Websites](#our-websites)
- [Examples](#examples)
    - [A Pipeline with basic elements](#a-pipeline-with-basic-elements)
    - [Using Manager API](#using-manager-api)
    
- [Team](#team)
- [License](#license)



## Install

```
pip install eyecu_bumblebee
```

## Motivation

Everything should be made as simple as possible, but no simpler. - Albert Einstein

## Our Websites

[EyeCU Vision](https://eyecuvision.com/) \
[EyeCU Future](https://eyecufuture.com/) 


## Examples

### A pipeline with basic elements

```python
from bumblebee import *

#


if __name__ == "__main__":
    
    VIDEO_PATH = "/path/to/video.mp4"

    # Create a source
    file_stream = sources.FileStream(VIDEO_PATH)

    # Add an effect
    goto = effects.GoTo(file_stream)

    # Add some transformers
    data = transformers.GrayScale(file_stream)
    data = transformers.Normalization(data)

    END_OF_VIDEO = file_stream.get_duration()
    goto(END_OF_VIDEO)

    # Create a dataset
    single_frame = datasets.SingleFrame(data)

    last_frame = single_frame.read()

```

### Using Manager API

```python
from bumblebee import *

#


if __name__ == "__main__":
    
    VIDEO_PATH = "/path/to/video.mp4"

    # Create a source
    file_stream = managers.BinaryClassification(
        ["path/to/video_dir","path/to/another_dir"],
        ["path/to"]
    )

    number_of_epochs = 300
    
    for epoch,(frame,prob) in manager(number_of_epochs):
        # Use data stuff
        ...    

```

## Team
This project is currently developed and maintained by [ovuruska](https://github.com/ovuruska).


## License
Bumblebee has a MIT license. You can find further details in [LICENSE](LICENSE).

