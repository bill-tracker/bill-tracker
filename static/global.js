

/* -------------- nav click functionality ------------------- */

$('.navbar-collapse a').click(function(e){
	
	var clickedLink = $(this);
	var clickedLi = clickedLink.parent();
	var lis = $('.navbar-collapse li');

	var searchTerm = clickedLink.text().toLowerCase();
	console.log('run ajax for ' + searchTerm + ' here.');
	lis.removeClass('active');
	clickedLi.addClass('active');

	e.preventDefault();

    switch (searchTerm) {
        case "content": window.location = "/bills";
             break;
        case "subject": window.location = "/subjects";
             break;
        case "author": window.location = "/authors";
             break;
        default: break;
    }


});







/* -------------- search functionality ------------------- */







/* -------------- single bill view functionality ------------------- */

var lastClicked;

function toggleForm(sentence)
{
	var submissionForm = document.getElementById("submission");

	if (submissionForm.style.visibility != "visible")
	{
		submissionForm.style.visibility = "visible";
		sentence.style.backgroundColor = "yellow";
		lastClicked = sentence;
	}
	else
	{
		submissionForm.style.visibility = "hidden";
		lastClicked.style.backgroundColor = "inherit";
	}
}

function submitAnnotation(text)
{
	var annotationText = text.value;
	var submissionForm = document.getElementById("submission");

	submissionForm.style.visibility = "hidden";
	lastClicked.style.backgroundColor = "inherit";
	alert(annotationText + " submitted as annotation for sentence " + lastClicked.id + ".");
	text.value = "";

}




/* ------------ move annotation sidebar to bootstrap column  --------------- */

if ( $('.billarea').length ) {

	setTimeout(function(){


		// move sidebar annotations into bootstrap column
		var sidebar = $('.annotations-list-uoc').detach();
		$('#submission').append(sidebar);

		// give sidebar height (it's contents are absolute so it has none)
		var billAreaHeight = $('.billarea').height();
		$('#submission').css('height',billAreaHeight + 'px');

		



		// makes an annotations array (with y values equal to the corresponding highlights' y values)
		var annotations = {};

		// init vars for annotation y pos calculations
		var basePos = $('.billarea').offset().top;
		var offset = 7; // about half of highlight height (this gets top of annotation to top of highlight)
		var annotations = [];
		var test;

		// annotation y pos calculations
		$('.annotator-wrapper .annotator-hl').each(function(index){

			var highlightId = $(this).attr('data-annotation-id');

			// prevents duplicate id entries (where highlight is broken into two with same id)
			if ( annotations.length && (annotations[index - 1].id == highlightId) ) {
				return;
			}

			var highlightPos = $(this).offset().top;
			var annotationSelector = '#submission #annotation-' + highlightId;
			var highlightTop = highlightPos - basePos - offset;
			var annotationHeight = $(annotationSelector).height();

			var annotationTop = null;

			if (index==0) {
					
				annotationTop = highlightTop;					

			} else {

				var prevIndex = index - 1;
				var prevAnnotation = annotations[prevIndex];
				var targetTop = highlightTop;
				var targetBot = highlightTop + annotationHeight;
				var prevTop = prevAnnotation.topY;
				var prevBot = prevAnnotation.botY;

				if ( (targetTop > prevTop) && (targetTop < prevBot) || (targetBot > prevTop) && (targetBot < prevBot) ) {
					annotationTop = prevBot + 15;
				} else {
					annotationTop = targetTop;
				}

			}

			annotations.push({
				id: highlightId,
				highlightY: highlightTop,
				annotationHeight: annotationHeight,
				topY: annotationTop,
				botY: annotationTop + annotationHeight
			});	

			$('#submission #annotation-' + highlightId).css('top', annotationTop + 'px');

		});

		// function compare(a,b) {
		// 	if (a.top < b.top) {
		// 		return -1;
		// 	}
		// 	if (a.top > b.top) {
		// 		return 1;
		// 	}
		// 	return 0;
		// }
		// annotations.sort(compare);




		/*
		var annotationLocations = [];

		// places annotations so they don't overlap
		for (var i = 0; i < annotations.length; i++) {

			var thisAnnotation = annotations[i];
			var targetTop = thisAnnotation.topY;
			var targetBot = thisAnnotation.botY;
			var actualTop = null;

		    if (i > 0) {
		    	
				var j = i - 1;
				var prevAnnotation = annotationLocations[j];
				var prevTop = prevAnnotation.topY;
				var prevBot = prevAnnotation.botY;

				if ( (targetTop > prevTop) && (targetTop < prevBot) || (targetBot > prevTop) && (targetBot < prevBot) ) {
					actualTop = prevBot + 15;
				} else {
					actualTop = targetTop;
				}

				annotationLocations.push({
					id: thisAnnotation.id,
					topY: targetTop,
					botY: actualTop + targetBot - targetTop
				});

			} else {

				actualTop = targetTop;
				annotationLocations.push({
					id: thisAnnotation.id,
					topY: targetTop,
					botY: actualTop + targetBot - targetTop
				});
			}

		    $('#submission #annotation-' + annotations[i].id).css('top', actualTop + 'px');

		}
		*/



	},1000);

}