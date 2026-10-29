from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI()



class Tea(BaseModel):
  id: int
  name: str
  origin: str


#annotations used with pydantic
teas: List[Tea]=[]


@app.get("/")  #decorator
def read_page():  #function
  return {"message":"Welcome home"}


@app.get("/teas")  #decorator
def get_teas():    #function
  return teas

  
@app.post("/teas")
def add_tea(tea:Tea):
  teas.append(tea)
  return tea


@app.put("/teas/{tea_id}")
def update_tea(tea_id: int,updated_tea: Tea):
  for index,tea in enumerate(teas):
    if(tea.id==tea_id):
      teas[index]=updated_tea
      return update_tea
  return {"error":"Tea not found"}


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
  for index,tea in enumerate(teas):
    if(tea.id==tea_id):
      deleted=teas.pop(index)
      return deleted
  return {"error":"we cant find such tea object"} 
