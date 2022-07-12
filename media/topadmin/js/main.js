$(document).ready(function() {

	// copy of link in tops on topadmin
		$(".site-url").html(window.location.origin);
		$(".top-url-input").each(function(index, element) {
			$(element).html(" " + window.location.origin + $(element).parent().find("a").attr("href"));
		})

		$(".top-url-copy").click(function() {
			let topUrlInput = $(this).parent().find(".top-url-input");
			/*topUrlInput.attr("value", (window.location.origin + $(this).parent().find("a").attr("href")));*/
			topUrlInput.select();
			document.execCommand('copy');
		});

	// select settings
	$('select.selectfilter, select.selectfilterstacked').each(function(index, el) {
		let formId = $(el).parent().parent().children('.form-input-default').attr('value');
		$(el).attr('id', formId)
		$(el).parent().css("width", "100%");
		const data = $(el).data();
		SelectFilter.init($(el).attr('id'), data.fieldName, parseInt(data.isStacked, 10));
	
	});
		
	});