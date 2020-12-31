# Bumblebee
[![PyPI](https://img.shields.io/pypi/v/eyecu_bumblebee.svg)](https://pypi.python.org/pypi/eyecu_bumblebee)
[![Downloads](http://pepy.tech/badge/eyecu_bumblebee)](https://pepy.tech/project/eyecu_bumblebee) \
![Bumblebee image](./docs/bumblebee.png)

## Install

```
pip install eyecu_bumblebee
```

## Motto

Everything should be made as simple as possible, but no simpler. - Albert Einstein

## Our Websites

[EyeCU Vision](https://eyecuvision.com/) \
[EyeCU Future](https://eyecufuture.com/) 


## Example

```python
from bumblebee import *

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

## Architecture Diagram

![Architecture](docs/bumblebee_arch_diagram.png)

