# Before anything, you have to install fastapi and uvicorn using "pip":
<br>pip install fastapi
<br>pip install uvicorn
<br>
# To run the app you have to type:
<br>uvicorn main:app --reload
<br>(if that didnt work try)
<br>```python3 -m uvicorn main:app --reload```
<br>
# To open the results:
<br>Go on your browser and search
<br>http://localhost:8000/docs
<br>
<br>Now when you added the tast yopu can view it alone by typing this
<br>http://localhost:8000/todos/(Task-ID)
<br>example:
<br>http://localhost:8000/todos/1
