var temp = "";

function disableInput() {
    var field = document.getElementById("prior_params");
    
    if (field.value != "") {
	temp = field.value;
    }

    field.style.display = "none";
    field.value = "";
}

function enableInput() {
    document.getElementById("prior_params").style.display = "inline";
    document.getElementById("prior_params").value = temp;
}
