function ditail_comment(blogid){
     var commentText=$('#note').val()
     var email=$('#email').val()
     var name=$('#name').val()
     var replaceid=$('#replaceId').val()
     // var captcha=$('#g-recaptcha-response').val()
     $.get('add-comment/',{
     'comment':commentText,
     'blog_id':blogid,
     'email':email,
     'user':name,
     'replace':replaceid,
     // 'captcha':captcha
     }).then(
         res=>{
             $('comment_list').html(res);
             location.reload()
         }
     )

}

function replace(commentId){
    $('#replaceId').val(commentId)
    document.getElementById('replace_comment').scrollIntoView({behavior:"smooth"});
    if (commentId){
        document.getElementById('replace_comment').style.display = 'block';
    }else {
        document.getElementById('replace_comment').style.display = 'none';
    }
}
function scroll_comment(){
    document.getElementById('replace_comment').scrollIntoView({behavior:"smooth"});
}
