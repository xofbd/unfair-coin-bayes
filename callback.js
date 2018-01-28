// gamma function
function gamma(n) {
    n -= 1;
    if (n == 0 || n == 1)
	return 1;
    for (var i = n - 1; i >= 1; i--) {
	n *= i;
    }
    return n;
 }

// beta function
function beta(a, b) {
    return gamma(a)*gamma(b)/gamma(a + b)
}

// flip coin function
function flip_coin(Pi, a, b) {
    var prob = Math.random();

    if (prob < Pi) {
	return [a + 1, b];
    }
    return [a, b + 1];
}

// get data sources from Callback args
var d1 = s1.data;
var d2 = s2.data;

// unpack variables from data sources
var x = d1['x'];
var p = d1['p'];
var params = d2['params'];

// update exponent
var updated_params = flip_coin(0.75, params[0], params[1])
var a = params[0];
var b = params[1];

// update probability
for (i = 0; i < x.length; i++) {
    p[i] = Math.pow(x[i], a - 1)*Math.pow(1 - x[i], b - 1)/beta(a, b)
}

// emit update to data sources
s1.change.emit();
s2.change.emit();
