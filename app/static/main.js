$(function() {
	$(window).resize(hideHeader);
});

var x = document.body.clientWidth;

function hideHeader() {
	var y = document.body.clientWidth;

	if (x <= 700 && y > 700) {
		$('.u-expand').css('display', 'inline-block');
	} else if (y <= 700 && x > 700) {
		$('.u-expand').css('display', 'none');
	}

	x = y;
}

function change(min_width=700) {
	if (document.body.clientWidth <= min_width) {
		if ($('.u-expand').css('display') == 'block')
			$('.u-expand').css('display', 'none');
		else
			$('.u-expand').css('display', 'inline-block');
	} else {
		document.location.href = '/';
	}
}

// function place(elem, count=4, percent=100, margin=0, padding=0, max_width=1500, min_width=425) {
// 	var head = document.head || document.getElementsByTagName('head')[0];
// 	var style = document.getElementsByTagName('style')[0] || document.createElement('style');

// 	var ots = margin * 2 + padding * 2;
// 	var re = (max_width - min_width) / (count - 1);
// 	var obl = max_width * percent / 100;

// 	var css = elem + " > div {margin: " + margin + "px; padding: " + padding + "px;}\n@media all and (max-width: " + min_width + "px) {" + elem + " {width: 100%;} " + elem + " > div {width: calc(100% - " + ots + "px);}}\n";

// 	for (var i = 0; i < count-1; i++) {
// 		css += "@media all and (min-width: " + ~~(min_width + re * i) + "px) {" + elem + " {width: " + percent + "%; margin-left: " + (100 - percent) / 2 + "%;} " + elem + " > div {width: calc(" + 100 / (i + 2) + "% - " + ots + "px);}}\n";
// 	}

// 	css += "@media all and (min-width: " + max_width + "px) {" + elem + " {width: " + obl + "px; margin-left: calc(50vw - " + obl / 2 + "px);} " + elem + " > div {width: " + (obl / count - ots) + "px;}}";

// 	style.appendChild(document.createTextNode(css));

// 	head.appendChild(style);
// }