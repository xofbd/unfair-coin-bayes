var temp = "";
var param_a = "";
var param_b = "";

function prepareUniform() {
    storeParams();
    updateParams("1", "1");
    disableInput();
}

function prepareBeta() {
    enableInput()
    updateParams(param_a, param_b)
}

function disableInput() {
    var field = document.getElementById("prior-params");
    
    if (field.value != "") {
	temp = field.value;
    }

    field.style.display = "none";
    field.value = "";
}

function enableInput() {
    document.getElementById("prior-params").style.display = "inline";
    document.getElementById("prior-params").value = temp;
}

function updateParams(param_a, param_b) {
    document.getElementById("param_a").value = param_a;
    document.getElementById("param_b").value = param_b;
}

function storeParams() {
    param_a = document.getElementById("param_a").value;
    param_b = document.getElementById("param_b").value;
}
