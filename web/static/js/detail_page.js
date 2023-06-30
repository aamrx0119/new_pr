console.log('hellllloooo')
$('.bookmark').submit(function(e){
    e.preventDefault()
    const post_id = $(this).attr('id')
    
    const url = $(this).attr('action')
    const x =$('.which-is').attr('d')
    const trim = $.trim(x)


    
    $.ajax({
        type :'POST',
        url : url,
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'post_id':post_id,

        },

        success: function(response) {
            if (trim === 'M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z'){
                $('.which-is').attr({'d':
                'M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zM6 6a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1H6z'})
                console.log('work successfuly')
            } else{
                $('.which-is').attr({'d':
                'M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z'})
                
            }
        },

        error: function(response) {
            console.log('error', response)
        }


    })


});

