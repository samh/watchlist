/*
 * Adds plus and minus buttons to the progress widget
 */

function zeroPad(num, places) {
    var zero = places - num.toString().length + 1;
    return new Array(+(zero > 0 && zero)).join("0") + num;
}

function incrementProgress(textInput, incrementAmount) {
    var showNumberStr = textInput.value;
    incrementAmount = typeof(incrementAmount) != 'undefined' ? incrementAmount : 1;
    var prefix = "";

    // First check to see if there is a season (e.g. 2-03)
    if (showNumberStr.search("-") != -1) {
        var split = showNumberStr.split("-");
        showNumberStr = split.pop();
        prefix = split.join("-") + "-";
    }

    var showNumber = parseInt(showNumberStr, 10);
    
    showNumber += incrementAmount;
    if (showNumber < 0) {
        showNumber = 0;
    }

    if (isNaN(showNumber)) {
        return;
    }

    textInput.value = prefix + zeroPad(showNumber, showNumberStr.length);
}

$(document).ready(function(){
    $("input.progress").after(function() {
        // Expect Django STATIC_URL to be defined by the template
        STATIC_URL = typeof(STATIC_URL) != 'undefined' ? STATIC_URL : '/STATIC_URL-is-undefined/';

        var base_js = "javascript:incrementProgress(document.getElementById(\"" + this.id + "\")";
        var plus_js = base_js + ")";
        var minus_js = base_js + ", -1)";

        // TODO: build with DOM API instead?
        var plus_img = "<img src='" + STATIC_URL + "img/go-up.png' alt='Increment'>";
        var minus_img = "<img src='" + STATIC_URL + "img/go-down.png' alt='Decrement'>";
        var plus_html = "<a href='" + plus_js + "'>" + plus_img + "</a>";
        var minus_html = "<a href='" + minus_js + "'>" + minus_img + "</a>";

        return minus_html + plus_html;
    });
});
