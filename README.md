# Vehicle Analyzer API

Takes image and returns:

The total number of cars present in the image.
The number of red cars in the image.
A textual description summarizing the content of the image.

Response has following structure

<pre> ```json { "total_cars": 10, "red_cars": 3, "description": "The image depicts a busy urban street with several vehicles, including three trees, pedestrians, amidst tall buildings." } ``` </pre>


## Setup

```bash
git clone https://github.com/yourusername/vehicle-analyzer.git
cd vehicle-analyzer
poetry install

running poetry run uvicorn main:app --reload
