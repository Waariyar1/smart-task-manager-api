from sqlalchemy.orm import Session
import models, schemas


def create_task(db: Session, task: schemas.TaskBase):
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def update_task(db: Session, task_id: int, task: schemas.TaskBase):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db.commit()
        db.refresh(db_task)

    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if db_task:
        db.delete(db_task)
        db.commit()

    return {"message": "Task deleted successfully"}