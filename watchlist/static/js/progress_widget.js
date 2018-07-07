/*
 * Adds plus and minus buttons to the progress widget
 */

function zeroPad(num, places) {
    const zero = places - num.toString().length + 1;
    return new Array(+(zero > 0 && zero)).join("0") + num;
}

function incrementProgress(textInput, incrementAmount) {
    let showNumberStr = textInput.value;
    incrementAmount = typeof(incrementAmount) !== 'undefined' ? incrementAmount : 1;
    let prefix = "";

    // First check to see if there is a season (e.g. 2-03)
    if (showNumberStr.search("-") !== -1) {
        const split = showNumberStr.split("-");
        showNumberStr = split.pop();
        prefix = split.join("-") + "-";
    }

    let showNumber = parseInt(showNumberStr, 10);

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
    const progress_input_class = 'input.progress';

    $(progress_input_class).after(function() {
        // Expect Django STATIC_PREFIX to be defined by the template
        const STATIC_URL = typeof(STATIC_PREFIX) !== 'undefined' ? STATIC_PREFIX : '/STATIC_URL-is-undefined/';

        const base_js = "javascript:incrementProgress(document.getElementById(\"" + this.id + "\")";
        const plus_js = base_js + ")";
        const minus_js = base_js + ", -1)";

        // TODO: build with DOM API instead?
        const plus_img = "<img src='" + STATIC_URL + "img/go-up.png' alt='Increment'>";
        const minus_img = "<img src='" + STATIC_URL + "img/go-down.png' alt='Decrement'>";
        const plus_html = "<a class='progress-button' href='" + plus_js + "'>" + plus_img + "</a>";
        const minus_html = "<a class='progress-button' href='" + minus_js + "'>" + minus_img + "</a>";

//        var buttons_html = "<div class='progress-buttons'>" + minus_html + plus_html + "</div>";
//        return buttons_html;
        return minus_html + plus_html;
    });

    // Add a class to the parent elements so we can style them
    $(progress_input_class).parent().addClass('progress');
});
