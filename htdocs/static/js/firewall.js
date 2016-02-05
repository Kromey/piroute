$( function() {
	/* Global Site Scripts */
	var activenav = $('body').data('active-nav');
	if('none' != activenav) {
		var target = '#nav-' + activenav;
		$(target).addClass('active');
	};

	/* Progress Bars */
	$('div.progress-bar').each(function () {
		var val = parseFloat($(this).attr('aria-valuenow'));
		var max = parseFloat($(this).attr('aria-valuemax'));

		$(this).css('width', (val/max*100) + '%').css('min-width', '2.5em');

		if(val < 70) {
			$(this).addClass('progress-bar-success');
		} else if(val < 85) {
			$(this).addClass('progress-bar-warning');
		} else {
			$(this).addClass('progress-bar-danger');
		}

		if(max > 100) {
			var maxline = 100 / max*100;
			var gradient = 'linear-gradient(to right, transparent ';
			gradient += maxline;
			gradient += '%, #FFC0CB ';
			gradient += maxline;
			gradient += '%)';

			$(this).parent().css('background-image', gradient);
		}
	});

	/* Firewall Rules Table */
	$('#new-port-button').click(function() {
		var new_form = $('#form-__prefix__-row').clone(true);
		var new_idx = $('#id_form-TOTAL_FORMS').val();

		var updateElementIndex = function(elm, idx) {
			if(elm.attr('for')) {
				elm.attr('for', elm.attr('for').replace('__prefix__', idx));
			}
			if(elm.attr('id')) {
				elm.attr('id', elm.attr('id').replace('__prefix__', idx));
			}
			if(elm.attr('name')) {
				elm.attr('name', elm.attr('name').replace('__prefix__', idx));
			}
		};

		updateElementIndex(new_form, new_idx);
		new_form.find('*').each(function(){updateElementIndex($(this), new_idx)});

		$('#ruleform_table').append(new_form);
		$('#id_form-TOTAL_FORMS').val(parseInt(new_idx)+1);
		new_form.find('td').fadeTo(400, 0.7, function(){ $(this).fadeTo(400, 1.0) });
	});

	/* Select Custom Widget */
	$('div.selectcustombox>:first-child').change(function() {
		var elem = $(this);
		var custom = elem.parent().data('custom');
		var target = elem.next();

		if(elem.val() == custom) {
			target.slideDown();
		} else {
			target.slideUp();
		}
	}).change();
});
