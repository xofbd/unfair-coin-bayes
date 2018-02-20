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
    return gamma(a)*gamma(b)/gamma(a + b);
}

// coin flip function
function flip_coin(Pi, a, b) {
    prob = Math.random();
    if (prob < Pi) {
	return [a + 1, b];
    }
    return [a, b + 1];
}

// get data sources from Callback args
var d1 = s1.data;
var d2 = s2.data;
var d3 = s3.data;

// unpack variables from data sources
var x = d1['x'];
var p = d1['p'];
var params = d2['params'];
var ys = d3['y'];

// update shape parameters
var updated_params = flip_coin(params[0], params[1], params[2]);
params[1] = updated_params[0];
params[2] = updated_params[1];
var a = params[1];
var b = params[2];

// update probability and patch coordinates
for (i = 0; i < x.length; i++) {
    p[i] = Math.pow(x[i], a - 1)*Math.pow(1 - x[i], b - 1)/beta(a, b);
    ys[i] = p[i]
}

// update reported stats
var mode = (a - 1)/(a + b- 2);
var variance = a*b/(Math.pow(a + b, 2)*(a + b + 1));
var mode_str = numeral(mode).format('0.[0000000]');
var variance_str = numeral(variance).format('0.[0000000]');

div.text = `<b>True Probability:</b> ${params[0]}<br> \n\
<b>Number of Heads:</b> ${a-1}<br>\
<b>Number of Tails:</b> ${b-1}<br> \n\
<b>Mode:</b> ${mode_str}<br> \n\
<b>Variance:</b> ${variance_str}`;

// emit update to data sources
s1.change.emit();
s2.change.emit();
s3.change.emit();
