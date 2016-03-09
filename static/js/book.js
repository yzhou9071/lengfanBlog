if(screen.width <= 768){
	$(".photoShelter").css("top","37%");
	$(".photoShelter").css("height","63%");
}
if(screen.width <= 480){
	$(".photoShelter").css("top","0%");
	$(".photoShelter").css("height","100%");
	$(".photoShelter p").css("font-size","0.67em");
}
$("#photoHeader").click(function(){
	$(".photoShelter").show();
	setTimeout(function(){
		$(".photoShelter").hide();
	},3000);
});
$(".carousel-img-width").mouseover(function(){
	$(".photoShelter").show();
});
$(".carousel-img-width").mouseout(function(){
	$(".photoShelter").hide();
});
