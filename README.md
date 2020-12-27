# Bumblebee

![Bumblebee image](./docs/bumblebee.png)

## Install

```
pip install eyecu_bumblebee
```

## Our Website

[EyeCU Vision](https://eyecuvision.com/) \
[EyeCU Future](https://eyecufuture.com/) \


## Architecture Diagram

![Architecture](docs/bumblebee_arch_diagram.png)




## Example Pipeline


```python
from bumblebee import *

if __name__ == "__main__":

    VIDEO_PATH = "/path/to/video.mp4" # Path to video
    
    # Create a source
    file_stream = sources.FileStream(VIDEO_PATH)
    
    # Add goto effect
    goto        = effects.GoTo(file_stream)
    
    # Add some transformers
    data        = transfomers.GrayScale(file_stream)
    data        = transfomers.Normalization(data)

    
    END_OF_VIDEO = file_stream.get_duration()
    # Goto end of video
    goto(END_OF_VIDEO) 
    
    # Create a dataset
    dataset = datasets.SingleFrame(data)
    
    # Last frame of video
    last_frame = dataset.read()

```