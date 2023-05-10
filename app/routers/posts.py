from app import oauth2
from .. import schema, models, database,oauth2
from typing import Optional,List
from fastapi import FastAPI, HTTPException,Depends,Response,status,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func


router = APIRouter(prefix='/posts',tags=['Posts'])

@router.get("",response_model=List[schema.PostDetail])
def get_posts(db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)
              ,limit:int = 3,offset:int = 0,search:Optional[str] = ""):#
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Posts,func.count(models.Votes.posts_id).label('votes')).join(models.Votes,models.Posts.id == models.Votes.posts_id,isouter=True).group_by(
        models.Posts.id).filter(models.Posts.title.contains(search)).limit(limit).offset(offset).all()
    return posts
     
@router.post('',status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_posts(post:schema.PostCreate,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(f"""INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) returning * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Posts(user_id = current_user.id,**post.dict())
    db.add(new_post);db.commit();db.refresh(new_post)
    return new_post

@router.get('/{id}',response_model=schema.Post)
def get_post(id:int,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(f"""SELECT * FROM posts where id = %s""",(str(id)))
    # posts = cursor.fetchone()
    posts = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not posts :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID not found")
    elif current_user.id != posts.user_id:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,detail="Un Authorized")
    return posts

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int,db: Session = Depends(database.get_db),user_id:int = Depends(oauth2.get_current_user)):
    # cursor.execute(f"""DELETE FROM posts WHERE id = %s returning * """,(str(id),))
    # del_posts = cursor.fetchone()
    # conn.commit()
    del_posts = db.query(models.Posts).filter(models.Posts.id == id)
    if del_posts.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID not found")
    elif user_id.id != del_posts.first().user_id:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,detail="Un Authorized")
    del_posts.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}')
def update_posts(id:int,post:schema.PostCreate,db: Session = Depends(database.get_db),user_id:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts set title = %s,content = %s, published = %s where id = %s returning *""",
    #                (post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_q = db.query(models.Posts).filter(models.Posts.id == id)
    updated_posts = post_q.first()
    if updated_posts is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"ID {id} not found")
    elif updated_posts.user_id != user_id.id:
        print(updated_posts.user_id,user_id.id)
        return HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,detail=f"Un Authorized")
    post_q.update(post.dict(),synchronize_session=False)
    db.commit()
    return post_q.first()
