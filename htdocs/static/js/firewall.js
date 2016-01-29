$( function() {
	var activenav = $('body').data('active-nav');
	if('none' != activenav)
	{
		var target = '#nav-' + activenav;
		$(target).addClass('active');
	}

	var ruleFormTemplate = $('#form-__prefix__-row');
	var ruleFormContainer = $('#ruleform_table');
	var totalFormsField = $('#id_form-TOTAL_FORMS');

	$('#new-port-button').click(function() {
		var new_form = ruleFormTemplate.clone(true);
		var new_idx = totalFormsField.val();

		updateElementIndex(new_form, new_idx);
		new_form.find('*').each(function(){updateElementIndex($(this), new_idx)});

		ruleFormContainer.append(new_form);
		totalFormsField.val(parseInt(new_idx)+1);
		new_form.find('td').fadeTo(400, 0.7, function(){ $(this).fadeTo(400, 1.0) });
	});

	var updateElementIndex = function(elm, idx) {
		if(elm.attr('for'))
		{
			elm.attr('for', elm.attr('for').replace('__prefix__', idx));
		}
		if(elm.attr('id'))
		{
			elm.attr('id', elm.attr('id').replace('__prefix__', idx));
		}
		if(elm.attr('name'))
		{
			elm.attr('name', elm.attr('name').replace('__prefix__', idx));
		}
	};

	$('div.selectcustombox>:first-child').change(function() {
		var elem = $(this);
		var custom = elem.parent().data('custom');
		var target = elem.next();

		if(elem.val() == custom)
		{
			target.slideDown();
		} else {
			target.slideUp();
		}
	}).change();
});
