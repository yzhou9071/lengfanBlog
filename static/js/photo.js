(function( $ ) {
	var $container = $('.masonry-container');
	$container.imagesLoaded( function () {
		$container.masonry({
			columnWidth: '.item',
			itemSelector: '.item'
		});
	});
})(jQuery);

if(screen.width <= 768){
	$(".photoShow").css("left","3.7%");
	$(".photoShow").css("width","92.6%");
	$(".photoShelter").css("top","37%");
	$(".photoShelter").css("height","63%");
}
if(screen.width <= 480){
	$(".photoShelter").css("top","0%");
	$(".photoShelter").css("height","100%");
	$(".photoShelter p").css("font-size","0.67em");
}

var currentItem;

$(".item").click(function(){
	currentItem = $(this);
	$(".photoBig").attr("src",currentItem.find("img").first()[0].src);
	$(".photoDesFont").text(currentItem.find("p").first().text());
	$(".ds-thread").attr("data-thread-key","photo-" + currentItem.find("strong").first().text());
	$(".photoPopup").show();
	$(".photoShow").show();
});

$(".photoLeft").click(function(){
	if(currentItem.prev().find("img").first()[0]){
		currentItem = currentItem.prev();
		$(".photoBig").attr("src",currentItem.find("img").first()[0].src);
		$(".photoDesFont").text(currentItem.find("p").first().text());
		$(".ds-thread").attr("data-thread-key","photo-" + currentItem.find("strong").first().text());
	}else{
		alert("已经最新，坐等更新！");
	}
});

$(".photoRight").click(function(){
	if(currentItem.next().find("img").first()[0]){
		currentItem = currentItem.next();
		$(".photoBig").attr("src",currentItem.find("img").first()[0].src);
		$(".photoDesFont").text(currentItem.find("p").first().text());
		$(".ds-thread").attr("data-thread-key","photo-" + currentItem.find("strong").first().text());
	}else{
		alert("最后一张,谢谢关注！");
	}
});

$(".photoPopup").click(function(){
	$(".photoPopup").hide();
	$(".photoShow").hide();
});

$(".photoBig").click(function(){
	$(".photoPopup").hide();
	$(".photoShow").hide();
});

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
