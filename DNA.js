process.stdin.resume();
process.stdin.setEncoding('utf8');

var freq = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
};
process.stdin.on('data', function (chunk) {
    for (var i = 0; i < chunk.length; i++) {
        c = chunk[i];
        freq[c] += 1;
    }
});

process.stdin.on('end', function () {
    process.stdout.write([freq['A'], freq['C'], freq['G'], freq['T']].join(' ') + '\n');
});
