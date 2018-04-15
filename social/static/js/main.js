"use strict";

const ADM_RE = /[0-9]{3}-?[0-9]{2}-?[0-9]{4}/;
const KEYS_RE = /\w|\s/i;
const ADVERBS = ["exactly", "specifically", "seriously"];
const URLS = [
  "https://www.consumer.ftc.gov/articles/0272-how-keep-your-personal-information-secure",
  "https://ist.mit.edu/security/protecting_data"
];
const WARNINGS = [
  "Why are you doing this?",
  "Please stop.",
  "Stop typing.",
  "You need to stop this.",
  "Consider your actions.",
  "You're doing yourself no good."
];
function* warnings() {
  var index;
  while (true) {
    index = Math.floor(Math.random() * WARNINGS.length);
    yield WARNINGS[index];
  }
}
const warnGen = warnings();

(function(f) {
  if (
    document.attachEvent
      ? document.readyState === "complete"
      : document.readyState !== "loading"
  ) {
    f();
  } else {
    document.addEventListener("DOMContentLoaded", f);
  }
})(onloadFunction);

function onloadFunction() {
  var mainForm = document.getElementById("main-form");
  var socInput = document.getElementById("soc-inp");
  var socErr = document.getElementById("soc-err");

  mainForm.addEventListener("submit", function(e) {
    e.preventDefault();
    var inp = socInput.value;
    if (inp.search(ADM_RE) !== -1) {
      let adv = ADVERBS[Math.floor(Math.random() * ADVERBS.length)];
      alert(`What ${adv} is wrong with you?`);
    }
  });
  socInput.addEventListener("keyup", function(e) {
    if (window.getSelection().toString() !== "") {
      return;
    }
    if (!KEYS_RE.test(e.key)) {
      return;
    }
    var rep = [];
    var val = socInput.value.replace(/\D/g, "").split("");
    if (val.length === 9) {
      return;
    }
    val.forEach(function(elem, i) {
      rep.push(elem);
      if (i === 2 || i === 4) {
        rep.push("-");
      }
    });
    if (rep[rep.length - 1] === "-") {
      rep.pop();
    }
    socInput.value = rep.join("");

    if (socErr.classList.contains("invisible")) {
      socErr.classList.remove("invisible");
    }
    socErr.innerHTML = warnGen.next().value;
    e.preventDefault();
  });
}
