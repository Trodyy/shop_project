function sendProductComment(productId) {
    let productComment = $('#product-comment').val()
    let parentId = $('#parent_id').val()
    console.log(parentId)
    $.get('/products/add-product-comment' , 
        {
        comment : productComment ,
        product_id : productId , 
        parent_id : parentId
        }
    ).then(res => {
       $('#comment_area').html(res)
       $('#parent_id').val('')
       $('#product-comment').val('')

       if (parentId !== '') {
        document.getElementById("single_comment_" + parentId).scrollIntoView({behavior: "smooth"});
    } else {
        document.getElementById('comment_area').current.scrollIntoView({behavior: "smooth"});
    }
    }
    )
}


function fullParentProduct(commentId) {
    $('#parent_id').val(commentId);
    document.getElementById('product-comment').scrollIntoView({behavior: "smooth"});
}
