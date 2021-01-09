# Bumblebee
[![PyPI](https://img.shields.io/pypi/v/eyecu_bumblebee.svg)](https://pypi.python.org/pypi/eyecu_bumblebee)
[![Downloads](http://pepy.tech/badge/eyecu_bumblebee)](https://pepy.tech/project/eyecu_bumblebee) \
![Bumblebee image](./docs/bumblebee.png)

Bumblebee provides high level components to construct training pipelines for videos conveniently.


- [Install](#install)
- [Motivation](#motto)
- [Our Websites](#our-websites)
- [Examples](#examples)
    - [A pipeline with basic elements](#a-pipeline-with-basic-elements)
    - [Using Manager API](#using-manager-api)
    - [Read limited section of video](#read--limited-section-of-video)
    - [Iterate frames with frame numbers](#iterate-frames-with-frame-numbers)
    - [Iterate frames in batches](#iterate-frames-in-batches)
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


if __name__ == "__main__":
    
    video_path = "/path/to/video.mp4"

    # Create a source
    file_stream = sources.FileStream(video_path)

    # Add an effect
    goto = effects.GoTo(file_stream)

    END_OF_VIDEO = file_stream.get_duration()
    goto(END_OF_VIDEO)

    # Create a dataset
    single_frame = datasets.Single(file_stream)

    last_frame = single_frame.read()

```

### Using Manager API

```python
from bumblebee import *


if __name__ == "__main__":
    
    # Create a training manager
    manager = managers.BinaryClassification(
        ["path/to/video_dir","path/to/another_dir"],
        ["path/to/labels"]
    )

    number_of_epochs = 300
    
    for epoch,(frame_no,frame,prob) in manager(number_of_epochs):
        # Use data stuff
        ...    

```


### Read  limited section of video
```python
from bumblebee import *


if __name__ == "__main__":
  
    video_path = "/path/to/video.mp4"
    start_frame = 35
    end_frame = 40
    
    file_stream = sources.FileStream(video_path)
    
    limited_stream = effects.Start(file_stream,start_frame)
    limited_stream = effects.End(limited_stream,end_frame)

    single_frame = datasets.Single(file_stream)

    for frame in single_frame:
        ...  

```

### Iterate frames with frame numbers
```python
from bumblebee import *


if __name__ == "__main__":
  
    video_path = "/path/to/video.mp4"
    
    file_stream = sources.FileStream(video_path)
    
    single_frame = datasets.Single(file_stream)
    current_frame = effects.CurrentFrame(file_stream)
    
    
    for frame_ind,frame in zip(current_frame,single_frame):
        ...  

``` 



### Iterate frames in batches

```python
from bumblebee import *


if __name__ == "__main__":
  
    video_path = "/path/to/video.mp4"
    batch_size = 64
    
    file_stream = sources.FileStream(video_path)
    
    batch = datasets.Batch(file_stream)
    
    for frames in batch:
        ...  

``` 

## Team
This project is currently developed and maintained by [ovuruska](https://github.com/ovuruska).


## License
Bumblebee has MIT license. You can find further details in [LICENSE](LICENSE).

