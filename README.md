# Before anything, you have to install fastapi and uvicorn using "pip":
pip install fastapi
pip install uvicorn

# To run the app you have to type:
uvicorn main:app --reload
(if that didnt work try)
python3 -m uvicorn main:app --reload

# To open the results:
Go on your browser and search
http://localhost:8000/docs

Now when you added the tast yopu can view it alone by typing this
http://localhost:8000/todos/(Task ID)
example:
http://localhost:8000/todos/1
