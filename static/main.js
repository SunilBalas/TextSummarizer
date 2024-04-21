$('#inputText').bind('focusout', () => {
    var text = $('#inputText').val().trim();
    validateText(text);
});

function summarize() {
    var text = $('#inputText').val().trim();

    if (validateText(text)) {
        $('#summarizeBtn').prop("disabled", true);
        $('#inputText').prop("disabled", true);
        $('.loading-container').removeClass('d-none');
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'text=' + encodeURIComponent(text),
        })
        .then(response => response.text())
        .then(summary => {
            summarizedText = JSON.parse(summary);

            $('#summarizeBtn').prop("disabled", false);
            $('#inputText').prop("disabled", false);
            $('.loading-container').addClass('d-none');
            $('#summarizedText').text(summarizedText?.text).removeClass('d-none');
        })
        .catch(error => console.error('Error:', error));
    }
}

function validateText(text) {
    if (text === null || text === "") {
        $("#errorText").text("Please enter the text !").removeClass('d-none').addClass('d-block');
        $('#summarizedText').text("").addClass('d-none');
        return false;
    } 
    else if (text.length > 2000) {
        $("#errorText").text("Text should be less than 2000 characters !").removeClass('d-none').addClass('d-block');
        $('#summarizedText').text("").addClass('d-none');
        return false;
    }
    $("#errorText").text("").removeClass('d-block').addClass('d-none');
    return true;
}