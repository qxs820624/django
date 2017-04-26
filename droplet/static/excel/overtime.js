
var records_th = 2;    //需要修改为实际的标题行的序号，从0开始 --qxx第三行为标题行
var winWidth = 0;
var winHeight = $(window).height(); //页面可视区域高度
var ipage = 1;
var ilisted = 0;
var ilabor = 0;
var idialect = 0;
var myurl = window.location.search;
var employeeid = myurl.substring(myurl.lastIndexOf('=')+1, myurl.length);
var tabname ="dialect";
//JavaScript Document
$(function(){
	//调用函数，获取数值
	setBodyProperty(true);
	findDimensions();
	var tab_content_len=winHeight-155;
	$("#tab_content").css("width",winWidth);   //ss.style.width=wb+"px";
	$("#tab_content").css("height",tab_content_len);   //ss.style.height=tab_content_len+"px";
	// console.log("winWidth:"+winWidth+", tab_content_len:"+tab_content_len);
	// window.onresize=findDimensions;
	window.resizeBy(winWidth,winHeight);
	$("#tab_nav li").each(function(itab_nav,item){
		// console.log("itab_nav:" + itab_nav);
		$(item).click(function () {
			$(this).siblings().removeClass("selected");
			$("#tab_content>div").hide();
			$(this).addClass("selected");
			$($(this).attr("action-data")).show();
			tabname = $(this).attr("action-data");
			$("#tab_content>div").each(function(jtab_content,itemtab_content){
			// console.log("j:" + jtab_content + "item" + $(itemtab_content) + " ---- " + $("#tab_content").height()+":"+ $(itemtab_content).height());
				$(itemtab_content).find("div").eq(1).height($("#tab_content").height()-$(itemtab_content).find("div").eq(0).height());
				proc_click();
			});
		})
	});
// $(window).scroll(function() {
// console.log("tab_content_len:"+tab_content_len);
$("#tab_content>div").each(function(iitemtab_content,item){
		// console.log("iitemtab_content:" + iitemtab_content);
		// var ret = new Array(3);
	$(item).find("div").eq(1).height($("#tab_content").height()-$(item).find("div").eq(0).height());
	$(item).find("div").eq(1).scroll(function() {
			// console.log("div scroll ilisted:" + ilisted + ", ilabor:" + ilabor + ", idialect:"+idialect);
		onMouseScroll(item);
			// console.log("div scroll ilistedilisted:" + ilisted + ", ilabor:" + ilabor + ", idialect:"+idialect);
	});
	$(item).click(function () {
		onMouseScroll(item);
			// console.log("click ilisted:" + ilisted + ", ilabor:" + ilabor + ", idialect:"+idialect);
	});
	});
	proc_click();
});

function onMouseScroll(item){
	var winH = $(window).height(); //页面可视区域高度
var pageH = $(document.body).height();
var scrollT = $(".table-body").scrollTop(); //滚动条top
	// alert(scrollT);
var aa = (winH - pageH - scrollT) / winH;
	$(".info").hide();
var divid = $(item).attr("id");
	if (divid == "undefined") {
		return;
	};
// console.log(divid);
	// console.log("winWidth:" + winWidth+ ",hight:" + winHeight + ",aa:" + aa);
	switch(divid.replace("tbody","")){
		case "listed":
			if (ilisted == -1) {
				// $(".info").show().html("别滚动了，已经到底了。。。");
				// return;
				return ;
			}
			ilisted++;
			ipage = ilisted;
			break;
		case "labor":
			if (ilabor == -1) {
				// $(".info").show().html("别滚动了，已经到底了。。。");
				return ;
			}
			ilabor++;
			ipage = ilabor;
			break;
		case "dialect":
			if (idialect == -1) {
				// $(".info").show().html("别滚动了，已经到底了。。。");
				return ;
			}
			// console.log(idialect);
			idialect++;
			ipage = idialect;
			break;
		default:
			return;
			break;
	};
if (aa < 0.05) {
		var str1 = self.location;
		var str = new String(str1);
		// console.log(str1);
		ibasename = str.lastIndexOf("/");
		// console.log(ibasename);
		var dirpath=str.substring(0,ibasename+1);
		// console.log(dirpath);
		var url=dirpath+"webexceloper.php";
		// console.log(url);
		var recordsnum = 9;
		var fixcloumn = 6;
		var sumcloumn = 2;
		// console.log("divid:" + divid);
		var tab_cloumn = [];
		// console.log("employeeid: " + employeeid);
		$.post(url, {"page": ipage, "id": divid, "employeeid": employeeid}, function(jsondata) {
		// $.getJSON("webexceloper.php", {page: ipage, id: divid}, function(jsondata) {
			// console.log("jsondata: " + jsondata);
			if(jsondata){
				if (jsondata.indexOf("bottom") != -1) {
					switch(divid.replace("tbody","")){
						case "listed":
							ilisted = -1;
							break;
						case "labor":
							ilabor = -1;
							break;
						case "dialect":
							idialect = -1;
							break;
					};
					$(".info").show().html("别滚动了，已经到底了。。。");
					return;
					// console.log("别滚动了，已经到底了 ilisted:" + ilisted + ", ilabor:" + ilabor + ", idialect:"+idialect);
				};
				$.each($.parseJSON(jsondata), function(index, array) {
					if ((typeof(array.recordsnum) == "undefined") && (typeof(array.serialno) == "undefined")) {
						console.log("empty line");
						return ;
					}else if (typeof(array.recordsnum) != "undefined") {
						recordsnum = array.recordsnum;
						fixcloumn = array.fix_cloumns;
						sumcloumn = array.sum_cloumn;
						table_cloumn = array.table_cloumn;
						// console.log("table_cloumn:" + table_cloumn);
						return ;
					};
					var tableID = "table"+divid;
					// console.log("tableID:" + tableID);
					// var tableObj=document.getElementById(tbodyID); //js 写法
					var tableObj = $("#"+tableID);      // jquery写法
					// console.log("tableObj:" + tableObj);
					if(tableObj==null)
					{
						alert("Table not Exist!");
						return;
					};
					var trtag = "#"+tableID+" tr";
					// console.log(trtag);
					var rowCount = $(trtag).length;
					var cellCount = tableObj.find("tr").eq(0).find("th").length + tableObj.find("tr").eq(0).find("td").length ;
					// console.log("rowCount:" + rowCount + ",cellCount:" + cellCount + ",AllcellCount:" + AllcellCount); //
					var bodyObj=document.getElementById("tbody"+divid); //js 写法
					// var bodyObj = $("#tbody"+divid);
					if(bodyObj == null)
					{
						alert("Body of Table not Exist!");
						return;
					};
					var newRow = bodyObj.insertRow(rowCount++);
					var rowHTML = "<tr>";

					var cellVal = array[table_cloumn[0]];
					var cellHTML = "<th class='record w1' scope=col>"+cellVal + "</th>";
					rowHTML += cellHTML;

					var cellVal = array[table_cloumn[1]];
					var cellHTML = "<th class='record w2' scope=col>"+cellVal + "</th>";
					rowHTML += cellHTML;

					for(var j=2;j<cellCount;j++)
					{
						var cellVal = array[table_cloumn[j]];
						if (j < fixcloumn) {
							var cellHTML = "<th class='record' scope=col>"+cellVal + "</th>";
						}else if (j > cellCount - sumcloumn - 1) {
							// console.log(j);
							var cellHTML = "<td scope=col >" + array[table_cloumn[j]] + "</td>";
						}else{
							var colorindex = j -  fixcloumn + 1;
							// console.log("colorindex: " + colorindex + array["color"+colorindex]);
							var cellHTML = '<td class='+array["color"+colorindex] + ' width=50 height=10 scope=col>' + array[table_cloumn[j]] + '</td>';
						};
						rowHTML += cellHTML;
					}
					rowHTML += "</tr>";
					// console.log(rowHTML);
					newRow.innerHTML = rowHTML;

				});
				proc_click();
			}else {
				$(".info").show().html("别滚动了，已经到底了。。。");
				return ;
		}
		});
}
}

function findDimensions() //函数：获取尺寸
{
	//获取窗口宽度
	if (window.innerWidth){
		winWidth = window.innerWidth;
	}
	else if ((document.body) && (document.body.clientWidth)){
		winWidth = document.body.clientWidth;
	}
	//获取窗口高度
	if (window.innerHeight){
		winHeight = window.innerHeight;
	}
	else if ((document.body) && (document.body.clientHeight)){
		winHeight = document.body.clientHeight;
	}
	//通过深入Document内部对body进行检测，获取窗口大小
	else if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth)
	{
		winHeight = document.documentElement.clientHeight;
		winWidth = document.documentElement.clientWidth;
	}
}

function toggle(id){
	var tb=document.getElementById(id);
	if(tb.style.display=='none')
		tb.style.display='block';
	else
		tb.style.display='none';
}

function send(gettype)
{
	if(!check()){
		return false;
	}
	var wenben = GetForm("wenben");
	var ajaxdata = ""
	ajaxdata += "&wenben="+wenben;

	$.ajax({
		type: "post",
		url : "tj.php",
		data: ajaxdata,
		success: function(html){
				$(".getcode").css("display","block");
				$("#codebox").val(html);
		}
	});
}

function submittoserver(){
	// alert("导出到服务器");
	objpassword = document.getElementsByName('password')[0];
	$.post(self.location,{'exporttoserver':'1','password':objpassword.value},function(data){alert(data);});
}
function submittolocal(){
	// alert("导出到服务器");
	objpassword = document.getElementsByName('password')[0];
	$.post(self.location,{'exporttolocal':'1'},function(data){location.href=data;});//alert("请保存");
}

function initdb(initfile){
	// alert("导出到服务器");
	$.post(self.location,{'initfile':initfile},function(){alert("数据库替换完毕");});//alert("请保存");
}

function refreshpage(){
	$.post(self.location,{'refresh':'1'},function(data){alert(data);});
}
function clear()
{
	document.write("");
}

function basename(str1)
{
str2="/"

var s = str1.lastIndexOf(str2);
if (s==-1) {
str2="\\"
var s = str1.lastIndexOf(str2);
}
if (s==-1) alert("字符串非法")
else{
return(str1.substring(s+1,str1.length));
}
return ""
}

function proc_click(){
	$(".info").hide();
	$("tr:even").css("background-color","dakgray");
	$("tr:odd").css("background-color","silver");
	$("tr td:not(:nth-last-child(1)):not(:nth-last-child(2))").click(function(){

		if($(this).children('input').length > 0){
			return;
		}
		console.log('proc_click tabname is '+ tabname);
		//取出表格中原有的内容
		var data=$(this).text();
		//将内容设置为空
		$(this).html('');
		var td=$(this);
		//创建一个表格
		var inp=$('<input type="text">');
		td.parent("tr").children("td").eq(-1).readonly=true;
		td.parent("tr").children("td").eq(-2).readonly=true;
		inp.val(data);
		inp.css("background-color",$(this).css("background-color"));
		inp.css("border-width","0px");
		inp.css("width",$(this).css("width"));
		//在表格中放一个input表单
		inp.appendTo($(this));
		//表单放入表格后触发焦点事件
		inp.trigger('focus');
		//全选内容
		inp.trigger('select');
		//添加键盘事件
		if (!Array.prototype.indexOf)
		{
		Array.prototype.indexOf = function(elt /*, from*/)
		{
		var len = this.length >>> 0;

		var from = Number(arguments[1]) || 0;
		from = (from < 0)
			? Math.ceil(from)
			: Math.floor(from);
		if (from < 0)
		from += len;
		for (; from < len; from++)
		{
		if (from in this &&
			this[from] === elt)
			return from;
		}
		return -1;
		};
		}

		inp.keydown(function(event){
			switch(event.keyCode){
				case 13:
					td.html($(this).val());
					fillcell(td,data);
					break;
				case 27:
					td.html(data);
					break;
			}
		}).blur(function(){
			td.html($(this).val());
			fillcell(td,data);
		});
	});
	$("tr td").change(function(){
		td = $(this);
		//td.css({'background':'#800080 '});  //== purple
		var thcolor =td.attr('class');
		var varcolor = thcolor.indexOf("red") != -1 ? "red":"yellow";
		if (thcolor.indexOf("red") != -1) {
			thcolor = "red";
		}else{
			thcolor = "yellow";
		};
		td.css({'background':thcolor});
	});
	$("tr td").mouseover(function(event) {
		var td = $(this)
		var tds=td.parent("tr").children("td");
		tds.css({'color':'#0D0'});  //== #00DD00
	});
	$("tr td").mouseleave(function(event) {
		var td = $(this)
		var tds=td.parent("tr").children("td");
		tds.css({'color':'#000'});  //== #00DD00
	});
}
//填充表格并自动计算
function fillcell (td,data) {
	// var jswebtab = document.getElementById("webtab").getAttribute("class");
	// var jswebtab = window.location.hash
	var jswebtab = tabname;
	// 鼠标事件
	var thcolor =td.attr('class');
	var varcolor = thcolor.indexOf("red") != -1 ? "red":"yellow";
	var newData = td.text();
	if (newData != data) {
		// if(validvalue.indexOf(newData) == "-1"){
		if (newData < 0 || newData > 1) {
			// inp.val(data);
			alert('需要0~1之间的数字');
			// alert("加班时间只能是0,0.5,1中的一个");
			td.html(data);
			return;
		}
		// alert(tdtext +  ";"  + tdcolor);
		if ( thcolor.indexOf("red") != "-1") {
			var redcloumnindex = -1
			if(newData != data){
				var inc = newData - data
				// alert("old:" + data + ", new:" + newData  + " increased: " + inc)
				var oldred = td.parent("tr").children("td").eq(redcloumnindex).text()
				// alert("blur oldred "+oldred);
				var newred = parseFloat(oldred) +parseFloat(inc)
				// alert("blur newred "+newred);
				td.parent("tr").children("td").eq(redcloumnindex).text(newred)
				// td.parent("tr").children("td").eq(redcloumnindex).css({'background':'#800080'}) //purple   0D0:green
				td.parent("tr").children("td").eq(redcloumnindex).css({'background':varcolor})
				// var newnewred = td.parent("tr").children("td").eq(redcloumnindex).text()
				// alert("oldred: " + oldred + ", newred " + newred  + "newnewred:" + newnewred)
			}
		}else if ( thcolor.indexOf("yellow") != "-1") {
			var yellowcloumnindex = -2
			if(newData != data){
				var inc = newData - data
				//alert("old:" + data + ", new:" + newData  + " increased: " + inc)
				var oldyellow = td.parent("tr").children("td").eq(yellowcloumnindex).text()
				var newyellow = parseFloat(oldyellow) +parseFloat(inc)
				td.parent("tr").children("td").eq(yellowcloumnindex).text(newyellow)
				//td.parent("tr").children("td").eq(yellowcloumnindex).css({'background':'#800080'}) //purple
				td.parent("tr").children("td").eq(yellowcloumnindex).css({'background':varcolor}) 
				var newnewred = td.parent("tr").children("td").eq(yellowcloumnindex).text()
				//alert("oldyellow: " + oldyellow + ", newyellow " + newyellow  + "newnewred:" + newnewred)
			}
		}
		//alert(td.attr("background"))
		//利用Ajax将数据传给服务器
		//获取一行所有的列对象
		var tds=td.parent("tr").children("td");
		var ths=td.parent("tr").children("th");
		var tdnum = tds.length;

		var s=ths.eq(0).text();
		//var i1= $(this).attr('background');
		var senddata='{"webtabname":"'+jswebtab + '",';
		var senddata= senddata + '"serialno":"' + s + '",';
		for (var i = 0; i < tdnum-2; i++) {
			var senddata = senddata + '"records'+(i+1)+'":"' + tds.eq(i).text() + '",';
		};
		senddata = senddata + '"yellowrecords":"' + tds.eq(i++).text() + '",';
		senddata = senddata + '"redrecords":"' + tds.eq(i).text()+'"}';
		console.log(senddata);
		// alert(self.location); //设置或获取 href 属性中跟在问号后面的部分
		// alert(window.location.search); //设置或获取 href 属性中跟在问号后面的部分
		// alert(window.location.hash);   // 设置或获取 href 属性中在井号“#”后面的分段
		// console.log("webtabname:"+jswebtab);
		var data = JSON.parse(senddata);
		console.log(data);
		$.post(self.location,data,function(data){});
	}; //if (newData != data)
}


function stop(){
	return false;
}

function enable(){
	return true;
}

function setBodyProperty(vFlag){
	if (vFlag) {
		window.onselectstart=stop;			//禁用选择
		window.oncopy=stop;      			//禁止复制
		window.onpaste=stop;   				//禁止粘贴
		window.oncut=stop;   				//禁止剪切
		window.ondragstart=stop;   			//禁止拖拉
		document.oncontextmenu=stop;		//禁止右键
		// document.onkeydown=stop;			//禁止键盘
		// document.onmousedown=stop;			//禁止鼠标
	}else{
		window.onselectstart=enable;			//禁用选择
		window.oncopy=enable;      			//禁止复制
		window.onpaste=enable;   				//禁止粘贴
		window.oncut=enable;   				//禁止剪切
		window.ondragstart=enable;   			//禁止拖拉
		document.oncontextmenu=enable;		//禁止右键
		document.onkeydown=enable;			//禁止键盘
		document.onmousedown=enable;			//禁止鼠标
	};
}
