
jQuery(function($) {
function show_reply_form(event) {
	var $this = $(this);
	var comment_id = $this.data('comment-id');

	$('#id_parent').val(comment_id);
	$('#form-comment').appendTo($this.closest('.media-body'));
};

function cancel_reply_form(event) {
	$('#id_comment').val('');
	$('#id_parent').val('');
	$('#form-comment').appendTo($('#wrap-form-comment'));
}

$.fn.ready(function() {
	$('.comment_reply_link').click(show_reply_form);
	$('#cancel_reply').click(cancel_reply_form);
})
var star = document.getElementById("star");
var star_li = star.getElementsByTagName("li");
var star_word = document.getElementById("star_word");
var result = document.getElementById("result");
var rating = document.getElementById("id_rating");
var i = 0;
var j = 0;
var len = star_li.length;
var word = ['worst','worse','normal',"well","best"]

for(i=0; i<len; i++){
star_li[i].index = i;
	
	star_li[i].onmouseover = function(){
	star_word.style.display = "block";
		star_word.innerHTML = word[this.index];
		for(i=0; i<=this.index; i++){
		star_li[i].className = "act";
		
		}
	}

	star_li[i].onmouseout = function(){
	star_word.style.display = "none";
		for(i=0; i<len; i++){
		star_li[i].className = "";
		}
	}
	
	star_li[i].onclick = function(){
	result.innerHTML = (this.index+1)+" stars";
	rating.innerHTML = (this.index+1);
	}
	
}
});

function setAuthenticatedUser() {
$('#div_id_name').hide();
$('#div_id_email').hide();
$('#div_id_url').hide();
}
