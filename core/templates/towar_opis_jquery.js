	$(".show_towar").mouseover(function(e){
		id=e.target.id.split('_');
		$.ajax({url:"/ajax/towar/"+id[1],success:function(result){
			$("#float").html(result);
			$("#float").show();
		}});
	});
	$(".show_towar").mousemove(function(e){
		var pos=$(this).position();
		$("#float").css({position: "absolute",
						top: e.pageY+"px",
						left: (e.pageX+20)+"px"})
	});
	$(".show_towar").mouseout(function(e){
		$("#float").hide();
	});
	$("#float").mouseover(function(){
		$("#float").hide();
	});