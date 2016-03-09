function updateAboutDetailNum(downloadTitle){
	$.get(
			"updateAboutDetailNum/",
			{downloadTitle:downloadTitle},
			function(ret){
			}
			);
}
