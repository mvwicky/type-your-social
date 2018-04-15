'use strict'

var RE = /[0-9]{3}-?[0-9]{2}-?[0-9]{4}/;
var ADVERBS = ['exactly', 'specifically'];


document.getElementById('main-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var inp = document.getElementById('social').value;
    if (inp.search(RE) !== -1) {
        let adv = ADVERBS[Math.floor(Math.random()*ADVERBS.length)];
        alert(`What ${adv} is wrong with you?`);
    }
});