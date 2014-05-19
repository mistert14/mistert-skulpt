var myCodeMirror
var xTriggered = 0;

function GetQueryStringParams(sParam)
    {
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
      {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
      }
    }

function s(e) {
    alert(e);
}

function outf(text) {
   var mypre = document.getElementById("output");
   mypre.innerHTML = mypre.innerHTML + text;
}


function builtinRead(x)
{
    
    if (Sk.builtinFiles == undefined || Sk.builtinFiles["files"][x] == undefined) {
        //alert(x+' -> '+Sk.builtinFiles["files"][x]);
		if ((x == 'src/lib/toto/__init__.js') || (x == 'src/lib/toto2/__init__.py')){
		    var url = x.replace('src/lib/','http://mrt2.no-ip.org/skulpt/plugins/');
		    
			//alert('voir module en: ' + url);
			$.ajax({
			    type:'GET',
                url: url,
            }).done(function(data) {
			    
				Sk.builtinFiles["files"][x] = data
                runit();				
			    return Sk.builtinFiles["files"][x]
		    }).error(function(data) {
			    throw new Sk.builtin.ImportError("No module named " + a);
			});
		    
		} else {
		    throw "File not found: '" + x + "'";
		}	
	} else {	
        return Sk.builtinFiles["files"][x];
    }

	
		
    
}

function runit() {
     $("#mycanvas").focus();
     $("#boutons").html("&nbsp;");
     var prog = document.getElementById("code_edit").value;
     var mypre = document.getElementById("output");
     mypre.innerHTML = '';
     Sk.canvas = "mycanvas";
     Sk.pre = "output";
     Sk.configure({output:outf, read:builtinRead, error:s});
   try {
      Sk.importMainWithBody("<stdin>",false,prog);
   } catch (e) {
      alert(e);
}
}

  $(function() {

    $("#mycanvas").focus();

    $( "#mouse" ).hide();
    $( "#editor" ).hide(); 

    myCodeMirror = CodeMirror.fromTextArea(document.getElementById('code'), {
        lineNumbers: true,
        gutters: ["CodeMirror-linenumbers", "breakpoints"]
    });

    window.onkeydown = function( event ) {
		$( "#editor" ).val(event.which);
	}

    window.onkeyup = function( event ) {
		$( "#editor" ).val('');
	}
    
    $( "#mycanvas" ).click(function( event ) {
        var x=event.clientX-$( "#mycanvas" ).offset().left;
        var y=event.clientY-$( "#mycanvas" ).offset().top; 
		$('#mouse').html(x+':'+y);
	});

    var page = GetQueryStringParams('id');
        if (!page) {
                page = 'default';
        }
        
   
    $.ajax({
        type: "GET",
        url: "give-python.php",
        data: { id: page, sender: "codeskulptor-MrT" }
    }).done(function( msg ) {

          myCodeMirror.setValue(msg);
          $('#code').html(msg);
          update();
        
    });


    $("#code_edit").hide();

    update = function() {

             $("#code_edit").html('')
             code = myCodeMirror.getValue();
             $("#code_edit").html(code);
             runit()
    }


    $('#run').click( function() {
        update();
    })
    //$('.chk').change( function() {
        //update();
    //})
    //update();
 })



