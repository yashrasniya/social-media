import React, {useEffect, useState} from 'react';

function HandelError(status){
if(status===403){
alert('you are not login')
window.location.href = "http://127.0.0.1:8000/login";
}
if(status===500){
alert('server side error')
}
}

export function Comments(props){
const [post,setPost]=useState([])
const [comment,setComment]=useState([])
const [likeButStyle,setLikeButStyle]=useState('btn-outline-primary')
const [doLike,setDoLike]=useState(post.is_like?true:false)


        useEffect(()=>{
    const myCallback=(responce)=>{
    console.log(responce)
    setPost(responce)
    setComment(responce.post_comment)
    }
    dataFinder(myCallback)
    },[])
    const {id,likes,photo, post_description}=post
const [countLike,setCountLike]=useState(likes)
    function doChange(data){
        data.preventDefault()
        let temp=[...comment]
        const myFormData= new FormData(data.target)
        myFormData.append('post',id)
        handleCommentAction(myFormData,false,'POST','api/post/do_comment',(responce,status)=>{
        if (status === 200){
            temp.unshift(responce)
            setComment(temp)
            data.target.reset()}
            else{
            HandelError(status)
            alert("there is an error")
            }})

    }

    function handleLike(){
    console.log(doLike)
    if (doLike){
        handleCommentAction(JSON.stringify({id: post.id,action:"unlike" }),true,'POST','api/post/action',(responce,status)=>{
        if(status===200){
        setLikeButStyle('btn-primary')
        setCountLike(responce.likes)
        setPost(responce)
        setDoLike(false)
        }else{
         HandelError(status)
        }
        })

    }
    else{
    handleCommentAction(JSON.stringify({id: post.id,action:"like" }),true,'POST','api/post/action',(responce,status)=>{
        if(status===200){
        setLikeButStyle('btn-outline-primary')
        setDoLike(true)
        setPost(responce)
        setCountLike(responce.likes)}else{
        HandelError(status)

        }
        })
    }
    }

return (
 <div className=" mb-1 col-md-4 mx-auto ">
<div className="col m-3 ">
<div className="card  ">
<img src={photo} className="card-img-top m-1"/>
    <div className="row m-3">
    <div className="col-9 ">
<h4 className="card-text col-auto">{post_description}</h4></div>
<div className="col-3 text-right">
<button className={'btn '+likeButStyle} onClick={handleLike}>{likes} like</button>
</div>
        </div>

<div>

<div className=" p-2 m-3 card">
        <form onSubmit={(event)=>{
        doChange(event)
        }}>


                <div className="row m-2">
            <div className="col">
            <input type="text" name="comment" className="col-12 mt-1 border rounded-pill"  required={true}></input></div>
        <div className="col-auto text-right  ">
<div className="text-right">
            <input type="submit" name="DoComment"  className="btn border rounded-pill"  value="comment"></input>
            </div>
            </div>
                </div>
</form>
<CommentRender comments={comment}/>


</div>

            </div>

</div>
    </div>
</div>
    )
}

function handleCommentAction(data,json,method,endpoint,callback){

        const xhr= new XMLHttpRequest()
        const csrftoken = getCookie('csrftoken');
        xhr.responseType='json'
        console.log(data,endpoint)
        xhr.open(method,`http://127.0.0.1:8000/${endpoint}`)
        if (json){xhr.setRequestHeader("Content-Type","application/json")}
        if (csrftoken){
            console.log("csrf token")
            xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
            xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
            xhr.setRequestHeader("X-CSRFToken" ,csrftoken)
            }
        xhr.onload=function(){
            const serverResponse =xhr.response
            const status =xhr.status
            console.log(serverResponse)
            callback(serverResponse,status)


        }
        xhr.onerror=function(e){
        console.log(e)
        }

        xhr.send(data)

    }

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function dataFinder(myCallback){
const xhr= new XMLHttpRequest()
        xhr.responseType='json'
        let url=window.location.href
        console.log(url.split(":"))

        let id=url.split("=")[1]
        xhr.open('GET',`http://127.0.0.1:8000/api/post/data/${id}`)
        xhr.onload=function(){
            const serverResponse =xhr.response
            myCallback(serverResponse)
    }
    xhr.onerror=function(e){
    console.log(e)
    }
        xhr.send()}


function CommentRender(props){

if (props.comments!=undefined){
const {comments}=props
return(comments.map((comments,index) => {
        return(<Render comment={comments} key={index} /> )})
)
}

return(<h4>hi</h4>)
}

function Render(props){
    const {comment}=props
    console.log(comment.is_like)
    let action;


    if(comment.is_like){action='unlike'}else{action='like'}

    const[Like,setLike]=useState({doLike:comment.is_like,text:action})

    function handleCommentLiking(id){
        let data;
        console.log(id)
            if (Like.doLike){
            
            
                data={id:id,action:Like.text}


                handleCommentAction(JSON.stringify(data),true,'POST','api/post_comment/action',(response,status)=>{

                if(status===200){setLike({doLike : false,text:"like"})}else(HandelError(status))
                }

            )

        }else{
            data={id:id,action:Like.text}

            handleCommentAction(JSON.stringify(data),true,'POST','api/post_comment/action',(response,status)=>{

            if(status===200){setLike({doLike : true,text:"unlike"})}else(HandelError(status))

            }
            )

        }

}

return(<div className='m-2 card p-2' id={comment.comment}>
<div className='row'>
<div className='col-10  '>
<div className='text-left'>
<p className='text-left' >{comment.comment} </p>
</div>
</div>
<div className='col '>
<button className='btn' onClick={(e)=>handleCommentLiking(comment.id)}>
<a  className='text-right' name='like-button' post-id="+comment.id+" >{Like.text}</a></button>
</div>
</div>
</div>)

}
