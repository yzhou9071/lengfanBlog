function pageInit(){
	resetPageView();
	$(window).scroll(showGotoTop);
	$(window).resize(showGotoTop);
	showGotoTop();
	showImageBox();
	showShare();
	showComments();
	showEdit();
}

function resetPageView() {
	$('#nav a[href="' + location.pathname + '"]').parent().addClass('active');
	$('table').addClass('table table-bordered table-striped');

	$('.menu-open, .menu-close').click(function() {
		$('.menu-open').toggle();
		$('.navs, .contents').toggleClass('push-right');
	});
	$('.posts-type div').click(function() {
		var type = $(this).data('type');
		$.cookie('posts-type', type, {expires: 365});
		switchTo(type);
	});
	switchTo($.cookie('posts-type'));
	$('.contents').removeClass('hidden');
}

function switchTo(type) {
	type = type === 'tile' ? 'tile' : 'list';
	$('.contents > ul').removeClass('posts-tile posts-list').addClass('posts-' + type);
}

function showGotoTop() {
	var $gotoTop = $('.goto_top'),
		$bdshare = $('#bdshare');

	if ($(document).scrollTop() > 0) {
		$gotoTop.fadeIn('slow');
		$bdshare.fadeOut('slow');
	} else {
		$gotoTop.fadeOut('slow');
		$bdshare.fadeIn('slow');
	}
}

function showImageBox() {
	$('#post').imagebox({
		direction: 'vertical'
	});
}

function showShare() {
	$('#bdshell_js').attr('src', 'http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000');
}

function showComments() {
	if (location.pathname !== "/" && location.pathname.indexOf("/index") === -1) {
		$('#comments').removeClass('hidden');
	}
}

function showEdit() {
	if (location.pathname !== "/" && location.pathname.indexOf("/index") === -1) {
		$('h2').append('<a class="edit-post" href="https://github.com/wenzhixin/blog/edit/master/html/posts' + location.pathname + '.md" title="编辑文章（纠正错误）"><i class="glyphicon glyphicon-edit"></i></a>');
	}
}

pageInit();

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
