from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Task Manager API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/tasks")
def create_task(task: schemas.TaskBase, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# READ
@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


# UPDATE
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.TaskBase, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)


# DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)