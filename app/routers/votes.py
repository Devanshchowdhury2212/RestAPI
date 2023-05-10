from app import oauth2
from .. import schema, models, database,oauth2
from typing import Optional,List
from fastapi import FastAPI, HTTPException,Depends,Response,status,APIRouter
from sqlalchemy.orm import Session


router = APIRouter(prefix='/vote',tags=['Votes'])

@router.post('',status_code=status.HTTP_201_CREATED)
def vote(votepost:schema.votepost,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    post = db.query(models.Posts).filter(models.Posts.id == votepost.post_id).first()
    if post is None:raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Does not Exists")
    votes_query = db.query(models.Votes).filter(models.Votes.posts_id == votepost.post_id ,models.Votes.user_id == current_user.id)
    if votepost.dir:
        if votes_query.first():
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail=f"Already Voted on Post {votepost.post_id} with User id {current_user.id}")
        #Add to the the table
        new_vote = models.Votes(user_id = current_user.id,posts_id = votepost.post_id)
        db.add(new_vote);db.commit();db.refresh(new_vote)
        return {"vote":new_vote}
    else:
        if not votes_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Vote previously on Post {votepost.post_id} with User id {current_user.id}")
        votes_query.delete(synchronize_session=False);db.commit()
        return Response(status_code=status.HTTP_200_OK)