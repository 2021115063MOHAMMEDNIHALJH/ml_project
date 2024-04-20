$(document).ready(function(){
    $('#irisForm').submit(function(e){
        e.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: 'classify.php',
            data: formData,
            success: function(response){
                $('#result').html('<b>Classification Result:</b> ' + response);
            }
        });
    });
});
