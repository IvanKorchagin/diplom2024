
$(document).ready(function(){
    $('#contactForm').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            url: '',
            type: 'POST',
            data: $(this).serialize(),
            success: function(data){
                $('#successMessage').text(data.success);
                $('#successModal').modal('show'); 
                $('#contactForm')[0].reset(); 
            },
            error: function(xhr){
                $('#successMessage').text(xhr.responseJSON.error);
                $('#successModal').modal('show'); 
            }
        });
    });
});

$(document).ready(function(){
    $('#callForm').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            url: '',
            type: 'POST',
            data: $(this).serialize(),
            success: function(data){
                $('#successMessage').text(data.success);
                $('#successModal').modal('show'); 
                $('#callForm')[0].reset(); 
            },
            error: function(xhr){
                $('#successMessage').text(xhr.responseJSON.error);
                $('#successModal').modal('show'); 
            }
        });
    });
});
