# Website -> Summary -> Image
This is a simple project that takes a website, summarizes it, and then creates an image of the summary. The image is created using runway's stable diffusion 1.5 and the summary is created using the jac_nlp's cl_summer module.

## How to use
add the follwing environment variables to environment
```bash
export HUGGINGFACE_API_KEY=<your_huggingface_api_key>
```
Install necessary packages
```bash
pip install -r requirements.txt
```
Create jaseci-server instance
```bash
jsserv runserver 5001
```
Run JSCTL and run the following commands
```bash
jsctl -m
jaseci> jac build main.jac
jaseci> login http://localhost:5001 # Input email and password, keep the token
jaseci> actions load local jac/text-to-image.py
jaseci> actions load module jac_nlp.cl_summer
jaseci> sentinel register main.jir -set_active true -mode ir
```
Set the Jaseci Token in another terminal
```bash
export JASECI_TOKEN=<your_jaseci_token>
```
Run the streamlit frontend
```bash
streamlit run app.py
```



