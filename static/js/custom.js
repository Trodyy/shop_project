function sendProductComment(productId) {
    let productComment = $('#product-comment').val()

    $.get('/products/add-product-comment' , 
        {
        comment : productComment ,
        product_id : productId
        }
    ).then(res =>
       window.location.reload()
    )
}